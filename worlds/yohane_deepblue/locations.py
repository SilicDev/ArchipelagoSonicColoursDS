import typing

from Options import Toggle
from BaseClasses import Location
from worlds.AutoWorld import World

from .data import LocationNames

class YohaneDeepblueLocation(Location):
    game: str = "YOHANE THE PARHELION -BLAZE in the DEEPBLUE-"


location_table: typing.Dict[str, int] = {

}

def setup_locations(world: World, player: int):
    locations = {}
    return locations

lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in location_table.items()}

location_groups: typing.Dict[str, str] = {
}