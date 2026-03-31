"""
Archipelago World definition for Sonic Colours (DS)
"""
import typing

from BaseClasses import Item, ItemClassification, Region, Tutorial
import settings
from worlds.AutoWorld import WebWorld, World

from .client import SonicColoursDSClient
from .items import SonicColoursDSItem, item_groups, planet_access_table, wisp_unlocks_table, emeralds_table, item_table, event_table, junk_table
from .locations import SonicColoursDSLocation, location_groups, location_table, setup_locations
from .options import SonicColoursDSOptions, Goal
from .data import ItemNames, LocationNames

class SonicColoursDSWebWorld(WebWorld):
    """
    Webhost info for Sonic Colours
    """
    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Sonic Colours (DS) with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["SilicDev"]
    )

    tutorials = [setup_en]


class SonicColoursDSSettings(settings.Group):
    class SonicColoursDSRomFile(settings.UserFilePath):
        """File name of your European Sonic Colours (DS) ROM"""
        description = "Sonic Colours (DS) ROM File"
        copy_to = "Sonic Colours (Europe) (En,Ja,Fr,De,Es,It).nds"
        md5s = ["d098c9ea8192ebb4ea63a6bd2d2b4670"]

    rom_file: SonicColoursDSRomFile = SonicColoursDSRomFile(SonicColoursDSRomFile.copy_to)

class SonicColorsDSWorld(World):
    game = "Sonic Colours (DS)"
    web = SonicColoursDSWebWorld()
    topology_present = True

    settings_key = "sonic_colours_ds_settings"
    settings: typing.ClassVar[SonicColoursDSSettings]

    options_dataclass = SonicColoursDSOptions
    options: SonicColoursDSOptions

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table
    item_name_groups = item_groups
    location_name_groups = location_groups

    required_client_version = (0, 6, 6)

    def create_regions(self):
        active_locations = setup_locations(self, self.player)
        menu_region = Region("Menu", self.player, self.multiworld)
        menu_region.add_locations(active_locations, SonicColoursDSLocation)
        # todo: add other regions
        self.multiworld.regions.append(menu_region)
        pass

    def create_items(self):
        itempool: list[SonicColoursDSItem] = []
        for item in wisp_unlocks_table.keys():
            itempool.append(self.create_item(item))
        for item in planet_access_table.keys():
            itempool.append(self.create_item(item))
        if self.options.goal.value == Goal.option_wisp_armor:
            self.multiworld.get_location(LocationNames.nega_wisp_armor, self.player).place_locked_item(self.create_item(ItemNames.park_keys))
        elif self.options.goal.value == Goal.option_mother_wisp:
            for item in emeralds_table.keys():
                itempool.append(self.create_item(item))
            self.multiworld.get_location(LocationNames.nega_mother_wisp, self.player).place_locked_item(self.create_item(ItemNames.mother_wisp))
        surplus_checks = len(self.get_locations()) - len(itempool) - 1
        itempool += [self.create_filler() for _ in range(surplus_checks)]
        self.multiworld.itempool += itempool
        

    def create_item(self, name: str) -> Item:
        data = None
        if name in event_table:
            data = event_table[name]
        else:
            data = item_table[name]
        classification = ItemClassification.filler
        if data.progression:
            classification = ItemClassification.progression
        item = SonicColoursDSItem(name, classification, data.code, self.player)
        return item

    def set_rules(self):
        self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemNames.park_keys if self.options.goal.value == Goal.option_wisp_armor else ItemNames.mother_wisp, self.player)  

    def get_filler_item_name(self) -> str:
        junk_keys = list(junk_table.keys())
        return self.multiworld.random.choice(junk_keys)
