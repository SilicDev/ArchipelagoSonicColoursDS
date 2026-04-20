import asyncio
import enum
from argparse import Namespace
import time
from typing import TYPE_CHECKING, Any, Dict
from collections.abc import Sequence

from pymem import pymem
import colorama
from CommonClient import ClientCommandProcessor, CommonContext, logger, get_base_parser, handle_url_arg, server_loop
from NetUtils import ClientStatus
from Utils import gui_enabled
from Options import Toggle

from .data import DataMaps, ItemNames, LocationNames
from .locations import location_table, lookup_id_to_name as location_id_to_name
from .items import item_table, unique_accessories_table, character_upgrade_table, stackables_set, lookup_id_to_name as item_id_to_name

if TYPE_CHECKING:
    import kvui

FLAGS_STRUCT_BASE_OFFSET = 0x0115B498
MAIN_BASE_OFFSET = 0x0166B418

YEN_OFFSET = 0x51050
GAME_FLAGS_OFFSET = 0x51058
CHARACTER_UNLOCK_FLAGS_OFFSET = 0x51064
GAME_PROGRESSION_FLAGS_OFFSET = 0x51071
CHARACTER_QUEST_FLAGS_OFFSET = 0x51073
BOSS_DEFEATED_FLAGS = 0x5107D
DUNGEON_FLAGS_OFFSET = 0x5124E
INVENTORY_OFFSET = 0x52570
EQUIPPED_ABILITIES_FLAGS_OFFSET = 0x58560
MAP_AREA_OFFSET = 0x585EC
MAP_ROOM_OFFSET = 0x585EF

PTR_FLAGS_STRUCT = [0x28, 0x8, 0x8]
OFFSET_AREA = 0xA0
OFFSET_AREA_RELOAD = 0xCD
OFFSET_IN_CREDITS = 0xCE
OFFSET_INGAME_TIME = 0x238
OFFSET_IS_DEAD = 0x360

class ConnectionStatus(enum.IntEnum):
    NOT_CONNECTED = 1
    CONNECTED = 2

class YohaneDeepblueCommandProcessor(ClientCommandProcessor):
    ctx: "YohaneDeepblueContext"

    def _cmd_kaboom(self) -> None:
        """
        Trigger a death.
        """
        self.ctx.on_deathlink({
            "time": time.time(),
            "source": self.ctx.player_names[self.ctx.slot],
            "cause": ""
        })
    
    def _cmd_debug(self) -> None:
        """
        Toggle debug logging.
        """
        self.ctx.debug_log = not self.ctx.debug_log
        if self.ctx.debug_log:
            logger.info("Enabled debug logging")
        else:
            logger.info("Disabled debug logging")

class YohaneDeepblueContext(CommonContext):
    game = "YOHANE THE PARHELION -BLAZE in the DEEPBLUE-"
    items_handling = 0b111  # full remote

    client_loop: asyncio.Task[None]

    last_connected_slot: int | None = None

    slot_data: dict[str, Any]

    connection_status: ConnectionStatus = ConnectionStatus.NOT_CONNECTED
    game_connected = False
    game_process: pymem.Pymem | None = None

    highest_processed_item_index: int = 0
    queued_locations: list[int]
    local_received_items: dict[str, int]
    local_accessories_enabled: int = 0

    last_map_area = -1
    last_map_room = -1
    in_parlor = False

    debug_log = True

    deathlink_enabled = False
    can_send_deathlink = False

    command_processor = YohaneDeepblueCommandProcessor

    def __init__(self, server_address: str | None = None, password: str | None = None) -> None:
        super().__init__(server_address, password)

        self.queued_locations = []
        self.local_received_items = {}
        self.slot_data = {}

    async def server_auth(self, password_requested: bool = False) -> None:
        await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game=self.game)

    async def game_watcher(self):
        while not self.exit_event.is_set():
            if self.game_connected and self.connection_status == ConnectionStatus.CONNECTED and self.game_process is not None:
                if (self.deathlink_enabled and "DeathLink" not in self.tags) or (not self.deathlink_enabled and "DeathLink" in self.tags):
                    await self.update_death_link(self.deathlink_enabled)
                try:
                    main_struct = self.get_base_address(MAIN_BASE_OFFSET)
                    if main_struct == -1:
                        logger.info("ERROR: Couldn't find main data struct!")
                        await asyncio.sleep(1)
                        continue
                    
                    map_area = self.game_process.read_uchar(main_struct + MAP_AREA_OFFSET)
                    map_room = self.game_process.read_uchar(main_struct + MAP_ROOM_OFFSET)
                    if self.last_map_area != map_area or self.last_map_room != map_room:
                        if self.debug_log:
                            logger.info("Entering room %d in area %d", map_room, map_area)
                        if self.last_map_area != map_area:
                            await self.send_msgs([{ # Update package for trackers
                                "cmd": "Bounce",
                                "slots": [self.slot],
                                "data": {
                                    "type": "MapUpdate",
                                    "mapId": map_area,
                                },
                            }])
                        self.last_map_area = map_area
                        self.last_map_room = map_room
                    game_flags = int(self.game_process.read_uchar(main_struct + GAME_FLAGS_OFFSET))
                    in_parlor = game_flags & 0x8 != 0
                    if in_parlor != self.in_parlor:
                        if in_parlor:
                            logger.info("Yohane safely arrived in her Fortune Parlor")
                        self.in_parlor = in_parlor
                    
                    dungeon_flags = int(self.game_process.read_uchar(main_struct + DUNGEON_FLAGS_OFFSET))
                    if self.slot_data["earlychikablocksmoved"] == Toggle.option_true and dungeon_flags & 0x2 == 0:
                        if self.debug_log:
                            logger.info("Setting Chika Block flags")
                        dungeon_flags |= 0x2
                        self.game_process.write_uchar(main_struct + DUNGEON_FLAGS_OFFSET, dungeon_flags)
                    
                    game_progression_flags = int(self.game_process.read_ushort(main_struct + GAME_PROGRESSION_FLAGS_OFFSET))
                    for location in DataMaps.character_rescue_flag_map:
                        if location in self.checked_locations:
                            game_progression_flags |= DataMaps.character_rescue_flag_map[location]
                        elif game_progression_flags & DataMaps.character_rescue_flag_map[location] != 0:
                            self.queued_locations.append(location_table[location])
                    game_progression_flags &= 0x7FFF
                    if ItemNames.boss_token in self.local_received_items and self.local_received_items[ItemNames.boss_token] >= 8:
                        game_progression_flags |= 0x8000 # Spawns Infernal Altar cutscene
                        game_flags |= 0x02
                    self.game_process.write_ushort(main_struct + GAME_PROGRESSION_FLAGS_OFFSET, game_progression_flags)
                    self.game_process.write_ushort(main_struct + GAME_FLAGS_OFFSET, game_flags)
                    
                    character_quest_flags = int(self.game_process.read_uint(main_struct + CHARACTER_QUEST_FLAGS_OFFSET))
                    for location in DataMaps.character_quest_flag_map:
                        if location in self.checked_locations:
                            continue
                        flag = DataMaps.character_quest_flag_map[location]
                        if character_quest_flags & flag != 0:
                            await self.send_msgs([{"cmd": "CreateHints", "locations": [location_table[location]]}])
                    character_quest_flags &= 0xDB6DB6FF # Disable collection flags

                    boss_defeated_flags = int(self.game_process.read_uint(main_struct + BOSS_DEFEATED_FLAGS))
                    for location in DataMaps.boss_defeated_flag_map:
                        if location in self.checked_locations:
                            continue
                        if boss_defeated_flags & DataMaps.boss_defeated_flag_map[location] != 0:
                            self.queued_locations.append(location_table[location])

                    character_unlock_flags = int(self.game_process.read_uint(main_struct + CHARACTER_UNLOCK_FLAGS_OFFSET))
                    character_unlock_flags &= 0xFFD5555F
                    for item in DataMaps.character_item_flags_map:
                        if item in self.local_received_items:
                            character_unlock_flags |= DataMaps.character_item_flags_map[item]
                            if item in DataMaps.character_item_to_quest_map.keys():
                                character_quest_flags |= DataMaps.character_item_to_quest_map[item]
                    self.game_process.write_uint(main_struct + CHARACTER_UNLOCK_FLAGS_OFFSET, character_unlock_flags)
                    self.game_process.write_uint(main_struct + CHARACTER_QUEST_FLAGS_OFFSET, character_quest_flags)

                    for item in character_upgrade_table.keys():
                        item_data = character_upgrade_table[item]
                        if item_data.code is not None: # events aren't real
                            offset = INVENTORY_OFFSET + (0x18 * item_data.code)
                            room = DataMaps.character_upgrade_to_area_room[item]
                            if item in self.local_received_items and (not (room[0] == map_area and map_room in room[1]) or location_table[room[2]] in self.checked_locations):
                                self.game_process.write_uchar(main_struct + offset, 1)
                            else:
                                self.game_process.write_uchar(main_struct + offset, 0)

                    for item in unique_accessories_table.keys():
                        item_data = unique_accessories_table[item]
                        if item_data.code is not None: # events aren't real
                            offset = INVENTORY_OFFSET + (0x18 * item_data.code)
                            if item in self.local_received_items:
                                self.game_process.write_uchar(main_struct + offset, 1)
                                if item == ItemNames.extra_accessory_slot:
                                    if self.local_received_items[item] > 1:
                                        self.game_process.write_uchar(main_struct + offset + 0x18, 1)
                                    else:
                                        self.game_process.write_uchar(main_struct + offset + 0x18, 0)
                            else:
                                self.game_process.write_uchar(main_struct + offset, 0)

                    cache: dict[int, int] = {}
                    for location in DataMaps.chest_location_map.keys():
                        if location in self.checked_locations:
                            continue
                        data = DataMaps.chest_location_map[location]
                        offset = data[0]
                        mask = data[1]
                        value = 0
                        if offset in cache:
                            value = cache[offset]
                        else:
                            value = int(self.game_process.read_uchar(main_struct + offset))
                            cache[offset] = value
                        if value & mask != 0:
                            self.queued_locations.append(location_table[location])
                            vanilla_item = DataMaps.chest_to_vanilla_content[location]
                            if vanilla_item in stackables_set:
                                offset = INVENTORY_OFFSET + (0x18 * item_table[vanilla_item].code)
                                value = int(self.game_process.read_uchar(main_struct + offset)) - 1 
                                self.game_process.write_uchar(main_struct + offset, value)
                                self.game_process.write_uchar(main_struct + offset - 0x10, value)
                        if location in [LocationNames.sandy_trap_room_chest, LocationNames.soarshoes_room_chest, LocationNames.gloves_of_might_room_chest]:
                            accessories_enabled = int(self.game_process.read_uchar(main_struct + EQUIPPED_ABILITIES_FLAGS_OFFSET))
                            accessories_enabled &= (0xF8 | self.local_accessories_enabled)
                            self.game_process.write_uchar(main_struct + EQUIPPED_ABILITIES_FLAGS_OFFSET, accessories_enabled)

                    flags_struct = _resolve_pointer(self, self.get_base_address(FLAGS_STRUCT_BASE_OFFSET), PTR_FLAGS_STRUCT)
                    if flags_struct == -1:
                        logger.info("ERROR: Couldn't find flags struct!")
                        await asyncio.sleep(1)
                        continue

                    is_dead = self.game_process.read_uchar(flags_struct + OFFSET_IS_DEAD)
                    if self.deathlink_enabled:
                        if not is_dead and not self.can_send_deathlink:
                            self.can_send_deathlink = True
                        elif is_dead and self.can_send_deathlink:
                            await self.send_death()
                            self.can_send_deathlink = False

                    while self.queued_locations:
                        location = self.queued_locations.pop(0)
                        self.locations_checked.add(location)
                        await self.check_locations({location})

                    new_items = self.items_received[self.highest_processed_item_index :]
                    for item in new_items:
                        self.highest_processed_item_index += 1
                        item_name = item_id_to_name[item.item]
                        if not item_name in self.local_received_items.keys():
                            self.local_received_items[item_name] = 1
                        else:
                            self.local_received_items[item_name] += 1
                        # receive item
                        accessories_changed = 0
                        if item_name == ItemNames.fallen_angels_soarshoes:
                            accessories_changed |= 0x01
                        elif item_name == ItemNames.gloves_of_might:
                            accessories_changed |= 0x02
                        elif item_name == ItemNames.sea_deitys_charm:
                            accessories_changed |= 0x04
                        if item_name in stackables_set:
                            offset = INVENTORY_OFFSET + (0x18 * item.item)
                            value = int(self.game_process.read_uchar(main_struct + offset)) + 1 # make bundles?
                            self.game_process.write_uchar(main_struct + offset, value)
                            self.game_process.write_uchar(main_struct + offset + 1, 0)
                            self.game_process.write_uchar(main_struct + offset - 0x10, value)
                        if accessories_changed != 0:
                            accessories_enabled = int(self.game_process.read_uchar(main_struct + EQUIPPED_ABILITIES_FLAGS_OFFSET))
                            accessories_enabled &= (0xFF - accessories_changed)
                            self.local_accessories_enabled |= accessories_changed
                            self.game_process.write_uchar(main_struct + EQUIPPED_ABILITIES_FLAGS_OFFSET, accessories_enabled | accessories_changed)

                    for new_remotely_cleared_location in self.checked_locations - self.locations_checked:
                        location_name = location_id_to_name[new_remotely_cleared_location]
                        if location_name in DataMaps.chest_location_map.keys():
                            data = DataMaps.chest_location_map[location_name]
                            offset = data[0]
                            mask = data[1]
                            value = int(self.game_process.read_uchar(main_struct + offset))
                            value |= mask
                            self.game_process.write_uchar(main_struct + offset, value)
                        elif location_name in DataMaps.character_rescue_flag_map.keys():
                            flag = DataMaps.character_rescue_flag_map[location_name]
                            game_progression_flags |= flag
                            self.game_process.write_ushort(main_struct + GAME_PROGRESSION_FLAGS_OFFSET, game_progression_flags)
                        elif location_name in DataMaps.boss_defeated_flag_map.keys():
                            flag = DataMaps.boss_defeated_flag_map[location_name]
                            boss_defeated_flags |= flag
                            self.game_process.write_uint(main_struct + BOSS_DEFEATED_FLAGS, boss_defeated_flags)
                        # other game collected item, clear location
                        pass

                    in_credits = self.game_process.read_uchar(flags_struct + OFFSET_IN_CREDITS)
                    if (in_credits != 0 or game_flags & 0x1 != 0) and not self.finished_game:
                        await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                        self.finished_game = True
                except Exception as e:
                    self.game_connected = False
                    logger.exception(e)
                pass # game specific logic
            elif not self.game_connected:
                logger.info("Connection to the game lost!")
                # connect game
                self.game_process = pymem.Pymem("game.exe")
                if self.game_process is not None:
                    self.game_connected = True
                pass
            else:
                # server disconnected?
                pass

            await asyncio.sleep(0.1)

    def on_package(self, cmd: str, args: dict) -> None:
        if cmd == "Connected":
            self.last_connected_slot = self.slot

            self.connection_status = ConnectionStatus.NOT_CONNECTED

            self.slot_data = args["slot_data"]
            self.highest_processed_item_index = 0
            self.locations_checked = set(args["checked_locations"])
            self.deathlink_enabled = self.slot_data.get("deathlink", False)

            self.connection_status = ConnectionStatus.CONNECTED
            self.connect_to_game()
    
    def on_deathlink(self, data: Dict[str, Any]) -> None:
        if self.game_process is not None:
            text = data.get("cause", "") # for ingame display
            flags_struct = _resolve_pointer(self, self.get_base_address(FLAGS_STRUCT_BASE_OFFSET), PTR_FLAGS_STRUCT)
            self.game_process.write_uchar(flags_struct + OFFSET_IS_DEAD, 1)
            self.game_process.write_uchar(flags_struct + OFFSET_AREA_RELOAD, 1)
            self.can_send_deathlink = False
        return super().on_deathlink(data)

    async def disconnect(self, *args: Any, **kwargs: Any) -> None:
        self.finished_game = False
        self.locations_checked = set()
        self.connection_status = ConnectionStatus.NOT_CONNECTED
        await super().disconnect(*args, **kwargs)
    
    def connect_to_game(self) -> None:
        try:
            self.game_process = pymem.Pymem("game.exe")
            if self.game_process is not None:
                self.game_connected = True
                logger.info("Successfully connected to %s.", self.game)
        except Exception as e:
            if self.game_connected:
                self.game_connected = False
            logger.info("%s is not open. If it is open run the launcher/client as admin.", self.game)
        pass

    def get_base_address(self, base_offset: int) -> int:
        if not self.game_connected or self.game_process is None:
            raise Exception("Must be connected to the game!")
        return _read_address(self, self.game_process.base_address + base_offset)


def launch_client(*args: Sequence[str]) -> None:
    parser = get_base_parser()
    parser.add_argument("--name", default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")

    launch_args = handle_url_arg(parser.parse_args(args))

    colorama.just_fix_windows_console()

    asyncio.run(main(launch_args))
    colorama.deinit()
    

async def main(args: Namespace) -> None:
    ctx = YohaneDeepblueContext(args.connect, args.password)
    ctx.auth = args.name
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    ctx.client_loop = asyncio.create_task(ctx.game_watcher(), name="Client Loop")

    await ctx.exit_event.wait()
    await ctx.shutdown()

def _read_address(ctx: YohaneDeepblueContext, address: int) -> int:
    if not ctx.game_connected or ctx.game_process is None:
        raise Exception("Must be connected to the game!")
    if ctx.game_process.is_64_bit:
        return int(ctx.game_process.read_longlong(address))
    else:
        return int(ctx.game_process.read_long(address))

def _resolve_pointer(ctx: YohaneDeepblueContext, base_address: int, pointer: list[int]) -> int:
    if not ctx.game_connected or ctx.game_process is None:
        raise Exception("Must be connected to the game!")
    address = base_address
    for offset in pointer:
        try:
            address = _read_address(ctx, address + offset)
        except Exception as e:
            logger.info("Failed to read value at address %x + %x", address, offset)
            return -1
    return address
