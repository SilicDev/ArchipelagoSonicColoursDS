"""
Classes and functions related to creating a ROM patch
"""

from settings import get_settings
from worlds.Files import APProcedurePatch


EU_HASH = "406514E483EE092A89F4298F59FD53A9"

class SonicColoursDSPatch(APProcedurePatch):
    game = "Sonic Colours (DS)"
    hash = EU_HASH
    patch_file_ending = ".apscds"
    result_file_ending = ".nds"
    
    @classmethod
    def get_source_data(cls) -> bytes:
        with open(get_settings().sonic_colours_ds_settings.rom_file, "rb") as infile:
            base_rom_bytes = bytes(infile.read())

        return base_rom_bytes
    pass