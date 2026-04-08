import typing

from BaseClasses import CollectionState, Region, Entrance, ItemClassification
from worlds.AutoWorld import World
from .locations import *
from .data import LocationNames, ItemNames

def create_regions(world: World, active_locations: dict[str, int]) -> None:
    menu_region = create_region(world, "Menu", active_locations, location_table.keys())
    
    world.multiworld.regions += [
        menu_region,
    ]

def connect_regions(world: World) -> None:
    pass

def create_region(world: World, name: str, active_locations: dict[str, int], location_set: set[str]) -> Region:
    region = Region(name, world.player, world.multiworld)
    for location in location_set:
        code = active_locations.get(location, 0)
        if location in active_locations.keys():
            region.locations.append(YohaneDeepblueLocation(world.player, location, code, region))
    return region

def connect(world: World, source: str, destination: str, rule: typing.Optional[typing.Callable[[CollectionState],bool]]) -> None:
    source_region = world.multiworld.get_region(source, world.player)
    dest_region = world.multiworld.get_region(destination, world.player)

    entrance = Entrance(world.player, destination, source_region)

    if rule:
        entrance.access_rule = rule
    
    source_region.exits.append(entrance)
    entrance.connect(dest_region)