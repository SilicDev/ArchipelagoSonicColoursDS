
from typing import TYPE_CHECKING

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext


class SonicColoursDSClient(BizHawkClient):
    game = "Sonic Colours (DS)"
    system = "NDS"
    patch_suffix = ".apscds"

    def initialize_client(self) -> None:
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
        if ctx.server is None or ctx.server.socket.closed or ctx.slot_data is None:
            return
        pass