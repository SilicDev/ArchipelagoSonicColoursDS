import typing

from BaseClasses import CollectionState, Region, Entrance, EntranceType, ItemClassification
from rule_builder.rules import *
from worlds.AutoWorld import World
from Options import Toggle
from .locations import *
from .data import LocationNames, ItemNames

def create_regions(world: World, active_locations: dict[str, int]) -> None:
    menu_region = create_region(world, "Menu", active_locations, menu_region_locations)
    sunken_temple_region = create_region(world, LocationNames.sunken_temple_region, active_locations, sunken_temple_region_locations)
    ruins_region = create_region(world, LocationNames.ruins_region, active_locations, ruins_region_locations)
    grotto_region = create_region(world, LocationNames.grotto_region, active_locations, grotto_region_locations)
    coral_hill_region = create_region(world, LocationNames.coral_hill_region, active_locations, coral_hill_region_locations)
    sea_of_trees_region = create_region(world, LocationNames.sea_of_trees_region, active_locations, sea_of_trees_region_locations)
    crystalline_grotto_region = create_region(world, LocationNames.crystalline_grotto_region, active_locations, crystalline_grotto_region_locations)
    sunken_volcano_left_region = create_region(world, LocationNames.sunken_volcano_left_region, active_locations, sunken_volcano_left_region_locations)
    sunken_volcano_right_region = create_region(world, LocationNames.sunken_volcano_right_region, active_locations, sunken_volcano_right_region_locations)
    shipwreck_region = create_region(world, LocationNames.shipwreck_region, active_locations, shipwreck_region_locations)
    infernal_altar_region = create_region(world, LocationNames.infernal_altar_region, active_locations, infernal_altar_region_locations)
    aqours_memoria_region = create_region(world, LocationNames.aqours_memoria_region, active_locations, aqours_memoria_region_locations)

    world.multiworld.regions += [
        menu_region,
        sunken_temple_region,
        ruins_region,
        grotto_region,
        coral_hill_region,
        sea_of_trees_region,
        crystalline_grotto_region,
        sunken_volcano_left_region,
        sunken_volcano_right_region,
        shipwreck_region,
        infernal_altar_region,
        aqours_memoria_region,
    ]

def connect_regions(world: World) -> None:
    connect(world, "Menu", LocationNames.sunken_temple_region, None)
    connect(world, LocationNames.grotto_region, LocationNames.ruins_region, None)
    if world.options.earlychikablocksmoved == Toggle.option_true:
        connect(world, LocationNames.sunken_temple_region, LocationNames.grotto_region, None)
    else:
        connect(world, LocationNames.sunken_temple_region, LocationNames.grotto_region, 
                lambda state: state.has(ItemNames.chika_unlock, world.player) or 
                    state.has_all([
                        ItemNames.ruby_unlock,
                        ItemNames.ruby_upgrade
                    ], world.player))
    connect(world, LocationNames.grotto_region, LocationNames.coral_hill_region, 
            lambda state: _coral_hill_access_rule(world, state))
    connect(world, LocationNames.shipwreck_region, LocationNames.coral_hill_region,  
            lambda state: _coral_hill_access_rule(world, state))
    connect(world, LocationNames.shipwreck_region, LocationNames.sea_of_trees_region, 
            lambda state: state.has(ItemNames.kanan_unlock, world.player) or 
                state.has_all([
                    ItemNames.mari_unlock,
                    ItemNames.mari_upgrade,
                    ItemNames.fallen_angels_soarshoes,
                    ItemNames.gloves_of_might
                ], world.player))
    connect(world, LocationNames.coral_hill_region, LocationNames.crystalline_grotto_region, 
            lambda state: state.has(ItemNames.gloves_of_might, world.player))
    connect(world, LocationNames.ruins_region, LocationNames.sunken_volcano_left_region, None)
    connect(world, LocationNames.sunken_volcano_left_region, LocationNames.sunken_volcano_right_region, 
            lambda state: state.has(ItemNames.kanan_unlock, world.player))
    connect(world, LocationNames.grotto_region, LocationNames.shipwreck_region, 
            lambda state: state.has(ItemNames.sea_deitys_charm, world.player))
    connect(world, LocationNames.coral_hill_region, LocationNames.shipwreck_region, 
            lambda state: state.has(ItemNames.sea_deitys_charm, world.player))
    connect(world, LocationNames.sea_of_trees_region, LocationNames.shipwreck_region, None)
    connect(world, LocationNames.sunken_temple_region, LocationNames.infernal_altar_region, 
            lambda state: state.has(ItemNames.boss_token, world.player, 8) and state.has_all([
                    ItemNames.riko_unlock,
                    ItemNames.kanan_unlock,
                    ItemNames.gloves_of_might
                ], world.player))
    connect(world, LocationNames.infernal_altar_region, LocationNames.aqours_memoria_region, None)
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

def _coral_hill_access_rule(world: World, state: CollectionState) -> bool:
    return (state.has(ItemNames.gloves_of_might, world.player) and state.has_any([
        ItemNames.you_unlock,
        ItemNames.dia_unlock,
        ItemNames.fallen_angels_soarshoes
    ], world.player)) or (state.has(ItemNames.you_unlock, world.player) and state.has_any([
        ItemNames.gloves_of_might,
        ItemNames.dia_unlock,
        ItemNames.fallen_angels_soarshoes
    ], world.player))