
from typing import TYPE_CHECKING, Dict, Set, Tuple

from Options import Toggle
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

from .data import DataMaps
from .locations import location_table


SCDS_AREA_ID = 0x1207C4
SCDS_LEVEL_ID = 0x1207C8
SCDS_LEVEL_RED_RINGS = 0x1208D7
SCDS_SONIC_POINTER = 0x19B19C

class SonicColoursDSClient(BizHawkClient):
    game = "Sonic Colours (DS)"
    system = "NDS"
    patch_suffix = ".apscds"

    local_checked_locations: Set[int]
    last_level: int

    def initialize_client(self) -> None:
        self.local_checked_locations = set()
        self.last_level = -1
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
        ctx.items_handling = 0b001
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
                    (SCDS_SONIC_POINTER, 4, "Main RAM")
                ])
            
            guards["SONIC"] = (SCDS_SONIC_POINTER, read_result[0], "Main RAM")

            sonic = int.from_bytes(guards["SONIC"][1], "little")
            
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

            local_checked_locations: set[int] = set()
            if ctx.slot_data["redringsanity"] == Toggle.option_true:
                location_prefix = DataMaps.level_id_to_location[level_id]
                read_result = await bizhawk.guarded_read(
                    ctx.bizhawk_ctx, 
                    [
                        (SCDS_LEVEL_RED_RINGS, 5, "Main RAM")
                    ],
                    [guards["SONIC"], guards["LEVEL"]])
                if read_result is not None:
                    for ring in range(len(read_result[0])):
                        if read_result[0][ring] == 1:
                            local_checked_locations.add(location_table[location_prefix + " - Red Ring " + str(ring + 1)])
            # Send locations
            if local_checked_locations != self.local_checked_locations:
                self.local_checked_locations = local_checked_locations

                if local_checked_locations is not None:
                    await ctx.check_locations(local_checked_locations)
            
        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass
        pass