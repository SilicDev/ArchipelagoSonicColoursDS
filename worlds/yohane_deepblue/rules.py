from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from worlds.AutoWorld import World

from .data import LocationNames, ItemNames

def set_rules(world: World) -> None:
    set_chest_rules(world)
    pass

def set_chest_rules(world: World) -> None:
    # Sunken Temple
    set_rule(world.get_location(LocationNames.fishy_archery_chest), 
             lambda state: state.has_any([
                 ItemNames.fallen_angels_soarshoes,
                 ItemNames.gloves_of_might
             ], world.player))
    set_rule(world.get_location(LocationNames.katys_mask_room_chest), 
            lambda state: state.has(ItemNames.you_unlock, world.player) or (
                    state.has(ItemNames.fallen_angels_soarshoes, world.player) and (
                        state.has(ItemNames.chika_unlock, world.player) or 
                        state.has_all([
                            ItemNames.ruby_unlock,
                            ItemNames.ruby_upgrade
                        ], world.player)
                    )
                ))
    set_rule(world.get_location(LocationNames.chika_testing_grounds_chest), 
             lambda state: state.has(ItemNames.you_unlock, world.player))