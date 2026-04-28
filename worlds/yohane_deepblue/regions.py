import typing

from BaseClasses import CollectionState, Region, Entrance, EntranceType, ItemClassification
from rule_builder.rules import *
from worlds.AutoWorld import World
from Options import Toggle
from .locations import *
from .items import YohaneDeepblueItem
from .data import LocationNames, ItemNames, DataMaps
from .rules import *

def create_regions(world: World, active_locations: dict[str, int]) -> None:
    menu_region = create_region(world, world.origin_region_name, active_locations, menu_region_locations)
    sunken_temple_region = create_region(world, LocationNames.sunken_temple_region, active_locations, sunken_temple_region_locations)
    ruins_region = create_region(world, LocationNames.ruins_region, active_locations, ruins_region_locations)
    ruins_lower_region = create_region(world, LocationNames.ruins_lower_region, active_locations, ruins_lower_region_locations)
    grotto_region = create_region(world, LocationNames.grotto_region, active_locations, grotto_region_locations)
    coral_hill_region = create_region(world, LocationNames.coral_hill_region, active_locations, coral_hill_region_locations)
    sea_of_trees_left_region = create_region(world, LocationNames.sea_of_trees_left_region, active_locations, sea_of_trees_left_region_locations)
    sea_of_trees_region = create_region(world, LocationNames.sea_of_trees_region, active_locations, sea_of_trees_region_locations)
    crystalline_grotto_left_region = create_region(world, LocationNames.crystalline_grotto_left_region, active_locations, crystalline_grotto_left_region_locations)
    crystalline_grotto_main_region = create_region(world, LocationNames.crystalline_grotto_main_region, active_locations, crystalline_grotto_main_region_locations)
    crystalline_grotto_boss_region = create_region(world, LocationNames.crystalline_grotto_boss_region, active_locations, crystalline_grotto_boss_region_locations)
    sunken_volcano_left_region = create_region(world, LocationNames.sunken_volcano_left_region, active_locations, sunken_volcano_left_region_locations)
    sunken_volcano_main_region = create_region(world, LocationNames.sunken_volcano_main_region, active_locations, sunken_volcano_main_region_locations)
    sunken_volcano_boss_region = create_region(world, LocationNames.sunken_volcano_boss_region, active_locations, sunken_volcano_boss_region_locations)
    shipwreck_left_region = create_region(world, LocationNames.shipwreck_left_region, active_locations, shipwreck_left_region_locations)
    shipwreck_center_region = create_region(world, LocationNames.shipwreck_center_region, active_locations, shipwreck_center_region_locations)
    shipwreck_boss_region = create_region(world, LocationNames.shipwreck_boss_region, active_locations, shipwreck_boss_region_locations)
    infernal_altar_region = create_region(world, LocationNames.infernal_altar_region, active_locations, infernal_altar_region_locations)
    aqours_memoria_region = create_region(world, LocationNames.aqours_memoria_region, active_locations, aqours_memoria_region_locations)

    if world.options.progressive_character_unlocks == Toggle.option_true:
        for item in DataMaps.character_item_to_progressive_map.keys():
            progressive = DataMaps.character_item_to_progressive_map[item]
            menu_region.add_event(item, item, Has(progressive[0], progressive[1]), YohaneDeepblueLocation, YohaneDeepblueItem, False)

    world.multiworld.regions += [
        menu_region,
        sunken_temple_region,
        ruins_region,
        ruins_lower_region,
        grotto_region,
        coral_hill_region,
        sea_of_trees_left_region,
        sea_of_trees_region,
        crystalline_grotto_left_region,
        crystalline_grotto_main_region,
        crystalline_grotto_boss_region,
        sunken_volcano_left_region,
        sunken_volcano_main_region,
        sunken_volcano_boss_region,
        shipwreck_left_region,
        shipwreck_center_region,
        shipwreck_boss_region,
        infernal_altar_region,
        aqours_memoria_region,
    ]

def connect_regions(world: World) -> None:
    connect(world, world.origin_region_name, LocationNames.sunken_temple_region, None)
    connect(world, LocationNames.grotto_region, LocationNames.ruins_region, None)
    connect(world, LocationNames.sunken_temple_region, LocationNames.grotto_region, 
            Filtered(chika_block_rule, options=chika_blocks_filter, filtered_resolution=True))
    connect(world, LocationNames.grotto_region, LocationNames.coral_hill_region, gloves_rule & (soarshoes_rule | you_rule | dia_rule))
    connect(world, LocationNames.grotto_region, LocationNames.shipwreck_left_region, sea_charm_rule & (kanan_rule | riko_rule))
    connect(world, LocationNames.shipwreck_left_region, LocationNames.shipwreck_center_region, gloves_rule | soarshoes_rule | chika_rule)
    connect(world, LocationNames.shipwreck_center_region, LocationNames.shipwreck_boss_region, gloves_rule)
    connect(world, LocationNames.coral_hill_region, LocationNames.shipwreck_boss_region, kanan_rule | (upgraded_mari_rule & soarshoes_rule & gloves_rule), True)
    connect(world, LocationNames.shipwreck_boss_region, LocationNames.sea_of_trees_left_region, CanReachLocation(LocationNames.shipwreck_boss_defeated) & (hanamaru_rule | you_rule))
    connect(world, LocationNames.sea_of_trees_left_region, LocationNames.sea_of_trees_region, riko_rule, True)
    connect(world, LocationNames.sea_of_trees_region, LocationNames.sea_of_trees_left_region, riko_rule | kanan_rule, True)
    connect(world, LocationNames.coral_hill_region, LocationNames.crystalline_grotto_left_region, gloves_rule & ruby_rule)
    connect(world, LocationNames.crystalline_grotto_left_region, LocationNames.crystalline_grotto_main_region, hanamaru_rule | you_rule | upgraded_ruby_rule)
    connect(world, LocationNames.crystalline_grotto_main_region, LocationNames.crystalline_grotto_boss_region, (dia_rule & (kanan_rule & sea_charm_rule)) | upgraded_ruby_rule, True)
    connect(world, LocationNames.crystalline_grotto_boss_region, LocationNames.crystalline_grotto_main_region, None, True)
    connect(world, LocationNames.ruins_region, LocationNames.ruins_lower_region, None, True)
    connect(world, LocationNames.ruins_region, LocationNames.sunken_volcano_left_region, None)
    connect(world, LocationNames.ruins_lower_region, LocationNames.sunken_volcano_main_region, kanan_rule)
    connect(world, LocationNames.sunken_volcano_main_region, LocationNames.sunken_volcano_left_region, None, True)
    connect(world, LocationNames.sunken_volcano_main_region, LocationNames.sunken_volcano_boss_region, you_rule | soarshoes_rule)
    connect(world, LocationNames.sunken_temple_region, LocationNames.infernal_altar_region, boss_token_rule)
    connect(world, LocationNames.infernal_altar_region, LocationNames.aqours_memoria_region, CanReachLocation(LocationNames.infernal_altar_boss_defeated))
    pass

def create_region(world: World, name: str, active_locations: dict[str, int], location_set: set[str]) -> Region:
    region = Region(name, world.player, world.multiworld)
    for location in location_set:
        code = active_locations.get(location, 0)
        if location in active_locations.keys():
            region.locations.append(YohaneDeepblueLocation(world.player, location, code, region))
    return region

def connect(world: World, source: str, destination: str, rule: typing.Optional[Rule | typing.Callable[[CollectionState],bool]], one_way: bool = False) -> None:
    source_region = world.multiworld.get_region(source, world.player)
    dest_region = world.multiworld.get_region(destination, world.player)

    entrance_name = source
    randomization_type = EntranceType.ONE_WAY
    if one_way:
        entrance_name += " -> "
    else:
        randomization_type = EntranceType.TWO_WAY
        entrance_name += " <-> "
    entrance_name += destination 
    entrance = Entrance(world.player, entrance_name, source_region, randomization_type=randomization_type)

    if rule is not None:
        world.set_rule(entrance, rule)
    
    source_region.exits.append(entrance)
    entrance.connect(dest_region)