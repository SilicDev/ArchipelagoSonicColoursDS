from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from worlds.AutoWorld import World

from .data import LocationNames, ItemNames

def set_rules(world: World) -> None:
    if world.options.goal.value == 1:
        set_rule(world.get_location(LocationNames.nega_mother_wisp), 
                lambda state: state.has_all([
                    ItemNames.white_emerald,
                    ItemNames.red_emerald,
                    ItemNames.cyan_emerald,
                    ItemNames.purple_emerald,
                    ItemNames.green_emerald,
                    ItemNames.yellow_emerald,
                    ItemNames.blue_emerald,
                ], world.player))
    set_rule(world.get_location(LocationNames.nega_wisp_armor), 
             lambda state: state.has_all([
                ItemNames.red_wisp_unlock,
                ItemNames.orange_wisp_unlock,
                ItemNames.yellow_wisp_unlock,
                ItemNames.cyan_wisp_unlock,
                ItemNames.violet_wisp_unlock
             ], world.player))
    if world.options.redringsanity:
        set_red_ring_rules(world)

def set_red_ring_rules(world: World) -> None:
    pass