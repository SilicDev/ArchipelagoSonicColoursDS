
from typing import TYPE_CHECKING, Dict, Set, Tuple

from Options import Toggle
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

from .data import DataMaps, ItemNames, LocationNames
from .locations import location_table, red_rings_table, level_clear_table
from .items import item_table, wisp_unlocks_table, emeralds_table


SCDS_RED_RINGS = 0x119BB4
SCDS_SCORES = 0x119BC0
SCDS_AREA_ID = 0x1207C4
SCDS_LEVEL_ID = 0x1207C8
SCDS_LEVEL_RED_RINGS = 0x1208D7
SCDS_ACTIVE_WISPS = 0x120900

SCDS_COUNTER_POINTER = 0x163D6C
SCDS_SONIC_POINTER = 0x19B19C

SCDS_RAM_START = 0x02000000

class SonicColoursDSClient(BizHawkClient):
    game = "Sonic Colours (DS)"
    system = "NDS"
    patch_suffix = ".apscds"

    local_checked_locations: Set[int]
    local_active_wisps: int
    local_red_rings = 0
    last_level: int
    num_items_received: int

    def initialize_client(self) -> None:
        self.local_checked_locations = set()
        self.last_level = -1
        self.local_active_wisps = 0
        self.local_red_rings = 0
        self.num_items_received = 0
        pass

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger

        try:
            # Check ROM name
            rom_name_bytes = ((await bizhawk.read(ctx.bizhawk_ctx, [(0x0, 16, "ROM")]))[0])
            rom_name = bytes([byte for byte in rom_name_bytes if byte != 0]).decode("ascii")
            if not rom_name == "SONICCOLORSBXSP":
                return False
        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False  # Should verify on the next pass

        ctx.game = self.game
        ctx.items_handling = 0b011
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.125

        self.initialize_client()
        return True

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        from CommonClient import logger
        if ctx.server is None or ctx.server.socket.closed or ctx.slot_data is None:
            return
        try:
            guards: Dict[str, Tuple[int, bytes, str]] = {}
            
            read_result = await bizhawk.read(
                ctx.bizhawk_ctx, 
                [
                    (SCDS_SONIC_POINTER, 4, "Main RAM"),
                    (SCDS_COUNTER_POINTER, 4, "Main RAM")
                ])
            
            guards["SONIC"] = (SCDS_SONIC_POINTER, read_result[0], "Main RAM")
            guards["COUNTERS"] = (SCDS_COUNTER_POINTER, read_result[1], "Main RAM")

            sonic = int.from_bytes(guards["SONIC"][1], "little")
            counters = int.from_bytes(guards["COUNTERS"][1], "little")
            
            read_result = await bizhawk.read(
                ctx.bizhawk_ctx, 
                [
                    (SCDS_AREA_ID, 2, "Main RAM"),
                    (SCDS_LEVEL_ID, 2, "Main RAM")
                ])

            guards["AREA"] = (SCDS_AREA_ID, read_result[0], "Main RAM")
            guards["LEVEL"] = (SCDS_LEVEL_ID, read_result[1], "Main RAM")

            area_id = int.from_bytes(guards["AREA"][1], "little")
            level_id = int.from_bytes(guards["LEVEL"][1], "little")
            location_prefix = DataMaps.level_id_to_location[level_id]

            if ctx.slot_data["redringsanity"] == Toggle.option_true:
                red_ring_storage = 0
                for location in ctx.checked_locations:
                    location_name = ctx.location_names.lookup_in_game(location)
                    if location_name in red_rings_table.keys():
                        red_ring_storage |= 1 << (location_table[location_name] - location_table[LocationNames.tropical_resort_act_1_red_ring_1])
                if red_ring_storage != self.local_red_rings:
                    await bizhawk.guarded_write(
                        ctx.bizhawk_ctx,
                        [
                            (SCDS_RED_RINGS, red_ring_storage.to_bytes(12, "little"), "Main RAM")
                        ], [guards["SONIC"]])
                    self.local_red_rings = red_ring_storage

            await self.handle_received_items(ctx, guards)

            local_checked_locations: set[int] = set()
            if counters > SCDS_RAM_START and ctx.slot_data["redringsanity"] == Toggle.option_true:
                read_result = await bizhawk.guarded_read(
                    ctx.bizhawk_ctx,
                    [
                        (SCDS_LEVEL_RED_RINGS, 5, "Main RAM")
                    ],
                    [guards["SONIC"], guards["LEVEL"]])
                if read_result is not None:
                    for ring in range(len(read_result[0])):
                        if read_result[0][ring] == 1:
                            local_checked_locations.add(location_table[location_prefix + " - Red Star Ring " + str(ring + 1)])
            
            for location in ctx.checked_locations:
                location_name = ctx.location_names.lookup_in_game(location)
                if (location >= location_table[LocationNames.tropical_resort_act_1] 
                        and location <= location_table[LocationNames.asteroid_coaster_mission_3] 
                        and location_name in level_clear_table.keys()):
                    offset = (location_table[location_name] - location_table[LocationNames.tropical_resort_act_1]) * 4
                    read_result = await bizhawk.guarded_read(
                        ctx.bizhawk_ctx,
                        [
                            (SCDS_SCORES + offset, 4, "Main RAM")
                        ],
                        [guards["SONIC"]])
                    if read_result is not None:
                        score = int.from_bytes(read_result[0], "little")
                        if score == 0:
                            score = 1
                            await bizhawk.guarded_write(
                                ctx.bizhawk_ctx,
                                [
                                    (SCDS_SCORES + offset, score.to_bytes(4, "little"), "Main RAM")
                                ], [guards["SONIC"]])
            
            for location in level_clear_table.keys():
                location_code = level_clear_table[location]
                if location_code <= location_table[LocationNames.asteroid_coaster_mission_3]:
                    offset = (location_code - location_table[LocationNames.tropical_resort_act_1]) * 4
                    read_result = await bizhawk.guarded_read(
                        ctx.bizhawk_ctx,
                        [
                            (SCDS_SCORES + offset, 4, "Main RAM")
                        ],
                        [guards["SONIC"]])
                    if read_result is not None:
                        score = int.from_bytes(read_result[0], "little")
                        if score > 0xF: #ignore rank
                            rank = score & 0xF
                            local_checked_locations.add(location_code)



            location_prefix = DataMaps.level_id_to_location[level_id]
            read_result = await bizhawk.guarded_read(
                ctx.bizhawk_ctx,
                [
                    (SCDS_ACTIVE_WISPS, 5, "Main RAM")
                ],
                [guards["SONIC"], guards["LEVEL"]])
            if read_result is not None:
                wisps = int.from_bytes(read_result[0])
                if self.local_active_wisps != wisps:
                    await bizhawk.guarded_write(
                        ctx.bizhawk_ctx,
                        [
                            (SCDS_ACTIVE_WISPS, [self.local_active_wisps], "Main RAM")
                        ], [guards["SONIC"]])
            

            
            # Send locations
            if local_checked_locations != self.local_checked_locations:
                self.local_checked_locations = local_checked_locations

                if local_checked_locations is not None:
                    await ctx.check_locations(local_checked_locations)
            
        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass
        pass

    async def handle_received_items(self, ctx: "BizHawkClientContext", guards: Dict[str, Tuple[int, bytes, str]]) -> None:
        if len(ctx.items_received) > self.num_items_received:
            item = ctx.items_received[self.num_items_received]
            if item.player == ctx.slot:
                item_name = ctx.item_names.lookup_in_game(item.item)
                if item_name in wisp_unlocks_table.keys():
                    self.local_active_wisps |= 1 << (item_table[item_name].code - item_table[ItemNames.white_wisp_unlock].code)

    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: dict) -> None:
        if cmd == "Connected":
            self.initialize_client()