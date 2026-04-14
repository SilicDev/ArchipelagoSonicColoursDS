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

if TYPE_CHECKING:
    import kvui

FLAGS_STRUCT_BASE_OFFSET = 0x0115B498
MAIN_BASE_OFFSET = 0x0166B418

PTR_FLAGS_STRUCT = [0x28, 0x8, 0x8]
OFFSET_IS_DEAD = 0x360
OFFSET_AREA_RELOAD = 0xCD
OFFSET_IN_CREDITS = 0xCE

class ConnectionStatus(enum.IntEnum):
    NOT_CONNECTED = 1
    CONNECTED = 2

class YohaneDeepblueCommandProcessor(ClientCommandProcessor):
    ctx: "YohaneDeepblueContext"

    def _cmd_kaboom(self) -> None:
        """Trigger a death.
        """
        self.ctx.on_deathlink({
            "time": time.time(),
            "source": self.ctx.player_names[self.ctx.slot],
            "cause": ""
        })

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

    deathlink_enabled = False
    can_send_deathlink = False

    command_processor = YohaneDeepblueCommandProcessor

    def __init__(self, server_address: str | None = None, password: str | None = None) -> None:
        super().__init__(server_address, password)

        self.queued_locations = []
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
                        # receive item

                    for new_remotely_cleared_location in self.checked_locations - self.locations_checked:
                        # other game collected item, clear location
                        pass

                    in_credits = self.game_process.read_uchar(flags_struct + OFFSET_IN_CREDITS)
                    if in_credits != 0 and not self.finished_game:
                        await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                        self.finished_game = True
                except Exception as e:
                    logger.exception(e)
                pass # game specific logic
            elif not self.game_connected:
                # connect game
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
            self.deathlink_enabled = self.slot_data.get("death_link", False)

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
