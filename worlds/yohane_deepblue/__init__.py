"""
Archipelago World definition for YOHANE THE PARHELION -BLAZE in the DEEPBLUE-
"""
import typing

from BaseClasses import Item, ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .items import YohaneDeepblueItem, item_groups, item_table, junk_table, event_table
from .locations import YohaneDeepblueLocation, location_groups, location_table, setup_locations
from .regions import create_regions, connect_regions
from .rules import set_rules
from .options import YohaneDeepblueOptions, yohane_deepblue_option_groups
from .data import ItemNames, LocationNames

class YohaneDeepblueWebWorld(WebWorld):
    """
    Webhost info for YOHANE THE PARHELION -BLAZE in the DEEPBLUE-
    """
    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing YOHANE THE PARHELION -BLAZE in the DEEPBLUE- with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["SilicDev"]
    )

    tutorials = [setup_en]

    option_groups = yohane_deepblue_option_groups

class YohaneDeepblueWorld(World):
    game = "YOHANE THE PARHELION -BLAZE in the DEEPBLUE-"
    web = YohaneDeepblueWebWorld()
    topology_present = True

    options_dataclass = YohaneDeepblueOptions
    options: YohaneDeepblueOptions

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table
    item_name_groups = item_groups
    location_name_groups = location_groups

    required_client_version = (0, 6, 6)


    def create_regions(self):
        active_locations = setup_locations(self, self.player)
        create_regions(self, active_locations)
        connect_regions(self)
        pass

    def create_items(self):
        num_locations_to_fill = len(self.multiworld.get_unfilled_locations(self.player))
        itempool: list[YohaneDeepblueItem] = []
        surplus_checks = num_locations_to_fill - len(itempool) - 1
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
        item = YohaneDeepblueItem(name, classification, data.code, self.player)
        return item

    def set_rules(self):
        set_rules(self)
        self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemNames.victory)
    
    def get_filler_item_name(self) -> str:
        junk_keys = list(junk_table.keys())
        return self.multiworld.random.choice(junk_keys)
    
    # No options yet
    #def fill_slot_data(self) -> typing.Dict[str, typing.Any]:
        #slot_data = self.options.as_dict(
        #)
        #return slot_data