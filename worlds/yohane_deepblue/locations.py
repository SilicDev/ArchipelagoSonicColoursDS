import typing

from Options import Toggle
from BaseClasses import Location
from worlds.AutoWorld import World

from .data import LocationNames

class YohaneDeepblueLocation(Location):
    game: str = "YOHANE THE PARHELION -BLAZE in the DEEPBLUE-"

character_rescue_locations = {
    LocationNames.chika_rescue: 1,
    LocationNames.kanan_rescue: 2,
    LocationNames.dia_rescue: 3,
    LocationNames.ruby_rescue: 4,
    LocationNames.you_rescue: 5,
    LocationNames.mari_rescue: 6,
    LocationNames.riko_rescue: 7,
    LocationNames.hanamaru_rescue: 8,
}

character_upgrade_locations = {
    LocationNames.chika_upgrade_quest: 20,
    LocationNames.riko_upgrade_quest: 21,
    LocationNames.kanan_upgrade_quest: 22,
    LocationNames.hanamaru_upgrade_quest: 23,
    LocationNames.ruby_upgrade_quest: 24,
    LocationNames.you_upgrade_quest: 25,
    LocationNames.dia_upgrade_quest: 26,
    LocationNames.mari_upgrade_quest: 27,
}

boss_fight_locations = {
    LocationNames.sunken_temple_boss_defeated: 40,
    LocationNames.ruins_boss_defeated_1: 41,
    LocationNames.ruins_boss_defeated_2: 42,
    LocationNames.ruins_boss_defeated_3: 43,
    LocationNames.grotto_boss_defeated: 44,
    LocationNames.coral_hill_boss_defeated: 45,
    LocationNames.sea_of_trees_boss_defeated: 46,
    LocationNames.crystalline_grotto_boss_defeated: 47,
    LocationNames.sunken_volcano_boss_defeated: 48,
    LocationNames.shipwreck_boss_defeated: 49,
    LocationNames.infernal_altar_boss_defeated: 50,

    LocationNames.aquors_memoria_boss_defeated: None
}

boss_refight_locations = {
    LocationNames.sunken_temple_boss_refight: 60,
    LocationNames.ruins_boss_refight: 61,
    LocationNames.grotto_boss_refight: 62,
    LocationNames.coral_hill_boss_refight: 63,
    LocationNames.sea_of_trees_boss_refight: 64,
    LocationNames.crystalline_grotto_boss_refight: 65,
    LocationNames.sunken_volcano_boss_refight: 66,
    LocationNames.shipwreck_boss_refight: 67,
    LocationNames.infernal_altar_boss_refight: 68,
}

chest_locations = {
    LocationNames.cast_tutorial_left_chest: 80,
    LocationNames.case_tutorial_right_chest: 81,
    LocationNames.fishy_archery_chest: 82,
    LocationNames.pathway_to_infernal_altar_chest: 83,
    LocationNames.katys_mask_room_chest: 84,
    LocationNames.chika_testing_grounds_chest: 85,

    LocationNames.grotto_next_to_first_save_room_chest: 86,
    LocationNames.first_waterfall_room_chest: 87,
    LocationNames.first_lake_room_chest: 88,
    LocationNames.second_lake_room_chest: 89,
    LocationNames.spellbook_room_chest: 90,
    LocationNames.long_waterfall_room_chest: 91,
    LocationNames.isolated_climb_room_chest: 92,
    LocationNames.small_cave_climb_room_chest: 93,

    LocationNames.sandy_trap_room_chest: 94,
    LocationNames.vertical_poison_room_chest: 95,
    LocationNames.rolling_rocks_room_chest: 96,
    LocationNames.laptop_room_chest: 97,
    LocationNames.hall_of_shame_chest: 98,

    LocationNames.sunken_volcano_next_to_first_save_room_chest: 99,
    LocationNames.hotspring_room_chest: 100,
    LocationNames.soarshoes_room_chest: 101,
    LocationNames.soarshoes_obligatory_issue_room_chest: 102,
    LocationNames.tonosamas_parts_room_chest: 103,

    LocationNames.really_sealed_off_chest_room_chest: 104,
    LocationNames.spikey_ball_fish_room_chest: 105,
    LocationNames.final_guard_room_chest: 106,
    LocationNames.gloves_of_might_room_chest: 107,
    LocationNames.postal_guild_bag_room: 108,

    LocationNames.soarshoesnt_chest_room_chest: 109,
    LocationNames.annoying_teleporting_fish_room_chest: 110,
    LocationNames.wallcrab_chest_room_chest: 111,
    LocationNames.dumb_block_room_chest: 112,
    LocationNames.lost_monstie_room_chest: 113,

    LocationNames.one_way_slide_room_chest: 114,
    LocationNames.giant_sliding_crystals_room_chest: 115,
    LocationNames.isolated_chest_room_chest: 116,
    LocationNames.looong_slide_room_chest: 117,
    LocationNames.mari_issue_room_chest: 118,

    LocationNames.giant_poison_enemy_crab_room_chest: 119,
    LocationNames.scarlet_delta_suit_room_chest: 120,
    LocationNames.golden_snail_room_chest: 121,
    LocationNames.slope_room_chest: 122,
    LocationNames.you_testing_grounds_chest: 123,

    LocationNames.purple_goo_room_chest: 124,
    LocationNames.dark_room_chest: 125,
}

menu_region_locations = {
    LocationNames.chika_rescue,
    LocationNames.kanan_rescue,
    LocationNames.dia_rescue,
    LocationNames.ruby_rescue,
    LocationNames.you_rescue,
    LocationNames.mari_rescue,
    LocationNames.riko_rescue,
    LocationNames.hanamaru_rescue,
    LocationNames.chika_upgrade_quest,
    LocationNames.riko_upgrade_quest,
    LocationNames.kanan_upgrade_quest,
    LocationNames.hanamaru_upgrade_quest,
    LocationNames.ruby_upgrade_quest,
    LocationNames.you_upgrade_quest,
    LocationNames.dia_upgrade_quest,
    LocationNames.mari_upgrade_quest,
}

sunken_temple_region_locations = {
    LocationNames.sunken_temple_boss_defeated,

    LocationNames.cast_tutorial_left_chest,
    LocationNames.case_tutorial_right_chest,
    LocationNames.fishy_archery_chest,
    LocationNames.pathway_to_infernal_altar_chest,
    LocationNames.katys_mask_room_chest,
    LocationNames.chika_testing_grounds_chest,
}

ruins_region_locations = {
    LocationNames.ruins_boss_defeated_1,
    LocationNames.ruins_boss_defeated_2,
    LocationNames.ruins_boss_defeated_3,

    LocationNames.sandy_trap_room_chest,
    LocationNames.vertical_poison_room_chest,
    LocationNames.rolling_rocks_room_chest,
    LocationNames.laptop_room_chest,
    LocationNames.hall_of_shame_chest,
}

grotto_region_locations = {
    LocationNames.grotto_boss_defeated,

    LocationNames.grotto_next_to_first_save_room_chest,
    LocationNames.first_waterfall_room_chest,
    LocationNames.first_lake_room_chest,
    LocationNames.second_lake_room_chest,
    LocationNames.spellbook_room_chest,
    LocationNames.long_waterfall_room_chest,
    LocationNames.isolated_climb_room_chest,
    LocationNames.small_cave_climb_room_chest,
}

coral_hill_region_locations = {
    LocationNames.coral_hill_boss_defeated,

    LocationNames.soarshoesnt_chest_room_chest,
    LocationNames.annoying_teleporting_fish_room_chest,
    LocationNames.wallcrab_chest_room_chest,
    LocationNames.dumb_block_room_chest,
    LocationNames.lost_monstie_room_chest,
}

sea_of_trees_region_locations = {
    LocationNames.sea_of_trees_boss_defeated,

    LocationNames.giant_poison_enemy_crab_room_chest,
    LocationNames.scarlet_delta_suit_room_chest,
    LocationNames.golden_snail_room_chest,
    LocationNames.slope_room_chest,
    LocationNames.you_testing_grounds_chest,
}

crystalline_grotto_region_locations = {
    LocationNames.crystalline_grotto_boss_defeated,

    LocationNames.one_way_slide_room_chest,
    LocationNames.giant_sliding_crystals_room_chest,
    LocationNames.isolated_chest_room_chest,
    LocationNames.looong_slide_room_chest,
    LocationNames.mari_issue_room_chest,
}

sunken_volcano_left_region_locations = set() # Left empty for now

sunken_volcano_right_region_locations = {
    LocationNames.sunken_volcano_boss_defeated,

    LocationNames.sunken_volcano_next_to_first_save_room_chest,
    LocationNames.hotspring_room_chest,
    LocationNames.soarshoes_room_chest,
    LocationNames.soarshoes_obligatory_issue_room_chest,
    LocationNames.tonosamas_parts_room_chest,
}

shipwreck_region_locations = {
    LocationNames.shipwreck_boss_defeated,

    LocationNames.really_sealed_off_chest_room_chest,
    LocationNames.spikey_ball_fish_room_chest,
    LocationNames.final_guard_room_chest,
    LocationNames.gloves_of_might_room_chest,
    LocationNames.postal_guild_bag_room,
}

infernal_altar_region_locations = {
    LocationNames.infernal_altar_boss_defeated,

    LocationNames.purple_goo_room_chest,
    LocationNames.dark_room_chest,
}

aqours_memoria_region_locations = {
    LocationNames.aquors_memoria_boss_defeated,

    LocationNames.sunken_temple_boss_refight,
    LocationNames.ruins_boss_refight,
    LocationNames.grotto_boss_refight,
    LocationNames.coral_hill_boss_refight,
    LocationNames.sea_of_trees_boss_refight,
    LocationNames.crystalline_grotto_boss_refight,
    LocationNames.sunken_volcano_boss_refight,
    LocationNames.shipwreck_boss_refight,
    LocationNames.infernal_altar_boss_refight,
}

location_table: dict[str, int] = {
    **character_rescue_locations,
    #**character_upgrade_locations,
    **boss_fight_locations,
    **boss_refight_locations,
    **chest_locations,
}

def setup_locations(world: World, player: int):
    locations = {}
    locations = location_table
    return locations

lookup_id_to_name: dict[int, str] = {idx: name for name, idx in location_table.items()}

location_groups: dict[str, set[str]] = {
}