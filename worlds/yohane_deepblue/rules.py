from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from worlds.AutoWorld import World
from rule_builder.rules import *
from .options import EnableYouSkips, EarlyChikaBlockMoved

from .data import LocationNames, ItemNames


you_enabled_filter = [OptionFilter(EnableYouSkips, EnableYouSkips.option_true)]
chika_blocks_filter = [OptionFilter(EarlyChikaBlockMoved, EarlyChikaBlockMoved.option_true)]

soarshoes_rule = Has(ItemNames.fallen_angels_soarshoes)
gloves_rule = Has(ItemNames.gloves_of_might)
sea_charm_rule = Has(ItemNames.sea_deitys_charm)

lailaps_rule = Has(ItemNames.lailaps_unlock)
chika_rule = Has(ItemNames.chika_unlock)
riko_rule = Has(ItemNames.riko_unlock)
kanan_rule = Has(ItemNames.kanan_unlock)
dia_rule = Has(ItemNames.dia_unlock)
you_rule = Has(ItemNames.you_unlock)
mari_rule = Has(ItemNames.mari_unlock)
hanamaru_rule = Has(ItemNames.hanamaru_unlock)
ruby_rule = Has(ItemNames.ruby_unlock)

upgraded_chika_rule = Has(ItemNames.chika_upgrade) & chika_rule
upgraded_riko_rule = Has(ItemNames.riko_upgrade) & riko_rule
upgraded_kanan_rule = Has(ItemNames.kanan_upgrade) & kanan_rule
upgraded_dia_rule = Has(ItemNames.dia_upgrade) & dia_rule
upgraded_you_rule = Has(ItemNames.you_upgrade) & you_rule
upgraded_mari_rule = Has(ItemNames.mari_upgrade) & mari_rule
upgraded_hanamaru_rule = Has(ItemNames.hanamaru_upgrade) & hanamaru_rule
upgraded_ruby_rule = Has(ItemNames.ruby_upgrade) & ruby_rule

big_weapon_rule = HasAny(ItemNames.threaded_blade, ItemNames.shamrock, ItemNames.demon_slayer, ItemNames.claiomh_solais)

def set_rules(world: World) -> None:
    set_chest_rules(world)
    pass

def set_chest_rules(world: World) -> None:
    # Sunken Temple
    world.set_rule(world.get_location(LocationNames.fishy_archery_chest), gloves_rule | soarshoes_rule)
    world.set_rule(world.get_location(LocationNames.katys_mask_room_chest), you_rule | (soarshoes_rule & (chika_rule | upgraded_ruby_rule)))
    world.set_rule(world.get_location(LocationNames.chika_testing_grounds_chest), you_rule)

    # Grotto
    #world.set_rule(world.get_location(LocationNames.first_waterfall_room_chest), )
    #world.set_rule(world.get_location(LocationNames.first_lake_room_chest), )
    #world.set_rule(world.get_location(LocationNames.second_lake_room_chest), )
    world.set_rule(world.get_location(LocationNames.spellbook_room_chest), riko_rule)
    #world.set_rule(world.get_location(LocationNames.long_waterfall_room_chest), )
    #world.set_rule(world.get_location(LocationNames.isolated_climb_room_chest), )
    #world.set_rule(world.get_location(LocationNames.small_cave_climb_room_chest), )

    # Ruins
    world.set_rule(world.get_location(LocationNames.sandy_trap_room_chest), soarshoes_rule | kanan_rule | you_rule)
    #world.set_rule(world.get_location(LocationNames.vertical_poison_room_chest), )
    #world.set_rule(world.get_location(LocationNames.rolling_rocks_room_chest), )
    world.set_rule(world.get_location(LocationNames.laptop_room_chest), you_rule | hanamaru_rule)
    world.set_rule(world.get_location(LocationNames.hall_of_shame_chest), soarshoes_rule | (gloves_rule & you_rule))

    # Sunken Volcano
    #world.set_rule(world.get_location(LocationNames.sunken_volcano_next_to_first_save_room_chest), )
    #world.set_rule(world.get_location(LocationNames.hotspring_room_chest), )
    world.set_rule(world.get_location(LocationNames.soarshoes_room_chest), kanan_rule | (soarshoes_rule & gloves_rule) | you_rule)
    #world.set_rule(world.get_location(LocationNames.soarshoes_obligatory_issue_room_chest), )
    world.set_rule(world.get_location(LocationNames.tonosamas_parts_room_chest), riko_rule & (big_weapon_rule | dia_rule | upgraded_hanamaru_rule | upgraded_mari_rule))

    # Shipwreck
    #world.set_rule(world.get_location(LocationNames.really_sealed_off_chest_room_chest), )
    #world.set_rule(world.get_location(LocationNames.spikey_ball_fish_room_chest), )
    #world.set_rule(world.get_location(LocationNames.final_guard_room_chest), )
    world.set_rule(
        world.get_location(LocationNames.gloves_of_might_room_chest), 
        (CanReachRegion(LocationNames.coral_hill_region) | (kanan_rule | (you_rule & riko_rule))) & (chika_rule | you_rule)
    )
    world.set_rule(
        world.get_location(LocationNames.postal_guild_bag_room),
        (CanReachRegion(LocationNames.coral_hill_region) | (kanan_rule | (you_rule & riko_rule))) & ((chika_rule & upgraded_mari_rule) | (kanan_rule & you_rule & gloves_rule))
    )

    # Coral Hill
    world.set_rule(world.get_location(LocationNames.soarshoesnt_chest_room_chest), gloves_rule)
    world.set_rule(world.get_location(LocationNames.annoying_teleporting_fish_room_chest), gloves_rule)
    world.set_rule(world.get_location(LocationNames.wallcrab_chest_room_chest), gloves_rule)
    world.set_rule(world.get_location(LocationNames.dumb_block_room_chest), gloves_rule)
    world.set_rule(world.get_location(LocationNames.lost_monstie_room_chest), upgraded_ruby_rule & gloves_rule)

    # Crystalline Grotto
    #world.set_rule(world.get_location(LocationNames.one_way_slide_room_chest), )
    #world.set_rule(world.get_location(LocationNames.giant_sliding_crystals_room_chest), )
    #world.set_rule(world.get_location(LocationNames.isolated_chest_room_chest), )
    world.set_rule(world.get_location(LocationNames.looong_slide_room_chest), gloves_rule) # you_rule | soarshoes_rule for easier access
    world.set_rule(world.get_location(LocationNames.mari_issue_room_chest), gloves_rule & you_rule)

    # Sea of Trees
    #world.set_rule(world.get_location(LocationNames.giant_poison_enemy_crab_room_chest), )
    world.set_rule(world.get_location(LocationNames.scarlet_delta_suit_room_chest), gloves_rule & riko_rule)
    #world.set_rule(world.get_location(LocationNames.golden_snail_room_chest), )
    #world.set_rule(world.get_location(LocationNames.slope_room_chest), )
    world.set_rule(world.get_location(LocationNames.you_testing_grounds_chest), gloves_rule & riko_rule & you_rule & (chika_rule | kanan_rule))

    # Infernal Altar
    world.set_rule(world.get_location(LocationNames.purple_goo_room_chest), you_rule & (soarshoes_rule | gloves_rule))
    world.set_rule(world.get_location(LocationNames.dark_room_chest), you_rule & (soarshoes_rule | gloves_rule))



