from . import ItemNames, LocationNames

chest_location_map = { # locations marked with ! are guesses and need to be confirmed
    LocationNames.cast_tutorial_left_chest: (0x5129F, 0x20),
    LocationNames.case_tutorial_right_chest: (0x5129F, 0x40),
    LocationNames.fishy_archery_chest: (0x512EC, 0x02),
    LocationNames.pathway_to_infernal_altar_chest: (0x512EC, 0x04),
    LocationNames.katys_mask_room_chest: (0x5129F, 0x80),
    LocationNames.chika_testing_grounds_chest: (0x512EC, 0x01),

    LocationNames.grotto_next_to_first_save_room_chest: (0x512F4, 0x80),
    LocationNames.first_waterfall_room_chest: (0x512F4, 0x02), #!
    LocationNames.first_lake_room_chest: (0x512F4, 0x40), #!
    LocationNames.second_lake_room_chest: (0x512F5, 0x01), #!
    LocationNames.spellbook_room_chest: (0x512F4, 0x01),
    LocationNames.long_waterfall_room_chest: (0x512A7, 0x20), #!
    LocationNames.isolated_climb_room_chest: (0x512A7, 0x40), #!
    LocationNames.small_cave_climb_room_chest: (0x512A7, 0x80), #!

    LocationNames.sandy_trap_room_chest: (0x512A3, 0x80),
    LocationNames.vertical_poison_room_chest: (0x512F0, 0x01), #!
    LocationNames.rolling_rocks_room_chest: (0x512F0, 0x02), #!
    LocationNames.laptop_room_chest: (0x512A3, 0x20),
    LocationNames.hall_of_shame_chest: (0x512A3, 0x40),

    LocationNames.sunken_volcano_next_to_first_save_room_chest: (0x51305, 0x10), #!
    LocationNames.hotspring_room_chest: (0x51305, 0x40), #!
    LocationNames.soarshoes_room_chest: (0x51305, 0x04),
    LocationNames.soarshoes_obligatory_issue_room_chest: (0x51305, 0x20),
    LocationNames.tonosamas_parts_room_chest: (0x51305, 0x08), #!

    LocationNames.really_sealed_off_chest_room_chest: (0x51308, 0x01), #!
    LocationNames.spikey_ball_fish_room_chest: (0x51308, 0x08), #!
    LocationNames.final_guard_room_chest: (0x51308, 0x10), #!
    LocationNames.gloves_of_might_room_chest: (0x512BB, 0x80),
    LocationNames.postal_guild_bag_room: (0x512BB, 0x40),

    LocationNames.soarshoesnt_chest_room_chest: (0x512F8, 0x01), #!
    LocationNames.wallcrab_chest_room_chest: (0x512F8, 0x08), #!
    LocationNames.annoying_teleporting_fish_room_chest: (0x512F8, 0x10), #!
    LocationNames.dumb_block_room_chest: (0x512AB, 0x80), #!
    LocationNames.lost_monstie_room_chest: (0x512AB, 0x20),

    LocationNames.one_way_slide_room_chest: (0x512B3, 0x20), #!
    LocationNames.giant_sliding_crystals_room_chest: (0x512B3, 0x40), #!
    LocationNames.isolated_chest_room_chest: (0x51300, 0x02), #!
    LocationNames.looong_slide_room_chest: (0x51300, 0x01),
    LocationNames.mari_issue_room_chest: (0x512B3, 0x80),

    LocationNames.giant_poison_enemy_crab_room_chest: (0x512AF, 0x40), #!
    LocationNames.scarlet_delta_suit_room_chest: (0x512AF, 0x80),
    LocationNames.golden_snail_room_chest: (0x512FC, 0x01), #!
    LocationNames.slope_room_chest: (0x512FC, 0x04), #!
    LocationNames.you_testing_grounds_chest: (0x512FC, 0x08),

    LocationNames.purple_goo_room_chest: (0x512BF, 0x40),
    LocationNames.dark_room_chest: (0x512BF, 0x20),
}

character_rescue_flag_map = {
    LocationNames.chika_rescue: 0x80,
    LocationNames.kanan_rescue: 0x0100,
    LocationNames.dia_rescue: 0x0200,
    LocationNames.ruby_rescue: 0x0400,
    LocationNames.you_rescue: 0x0800,
    LocationNames.mari_rescue: 0x1000,
    LocationNames.riko_rescue: 0x2000,
    LocationNames.hanamaru_rescue: 0x4000,
}

character_quest_flag_map = {
    LocationNames.katys_mask_room_chest: 0x80,
    LocationNames.spellbook_room_chest: 0x0400,
    LocationNames.tonosamas_parts_room_chest: 0x2000,
    LocationNames.laptop_room_chest: 0x010000,
    LocationNames.isolated_chest_room_chest: 0x080000,
    LocationNames.postal_guild_bag_room: 0x400000,
    LocationNames.scarlet_delta_suit_room_chest: 0x02000000,
    LocationNames.lost_monstie_room_chest: 0x10000000,
}

boss_defeated_flag_map = {
    LocationNames.sunken_temple_boss_defeated: 0x20,
    LocationNames.ruins_boss_defeated_1: 0x40,
    LocationNames.ruins_boss_defeated_2: 0x80,
    LocationNames.ruins_boss_defeated_3: 0x0100,
    LocationNames.grotto_boss_defeated: 0x0200,
    LocationNames.coral_hill_boss_defeated: 0x0400,
    LocationNames.sea_of_trees_boss_defeated: 0x0800,
    LocationNames.crystalline_grotto_boss_defeated: 0x1000,
    LocationNames.sunken_volcano_boss_defeated: 0x2000,
    LocationNames.shipwreck_boss_defeated: 0x4000,
    LocationNames.infernal_altar_boss_defeated: 0x8000,

    LocationNames.sunken_temple_boss_refight: 0x010000,
    LocationNames.ruins_boss_refight: 0x020000,
    LocationNames.grotto_boss_refight: 0x040000,
    LocationNames.coral_hill_boss_refight: 0x080000,
    LocationNames.sea_of_trees_boss_refight: 0x100000,
    LocationNames.crystalline_grotto_boss_refight: 0x200000,
    LocationNames.sunken_volcano_boss_refight: 0x400000,
    LocationNames.shipwreck_boss_refight: 0x800000,
    LocationNames.infernal_altar_boss_refight: 0x01000000,
}

character_item_flags_map = {
    ItemNames.lailaps_unlock: 0x20,
    #ItemNames.lailaps_upgrade: 0x40,
    ItemNames.chika_unlock: 0x80,
    #ItemNames.chika_upgrade: 0x0100,
    ItemNames.riko_unlock: 0x0200,
    #ItemNames.riko_upgrade: 0x0400,
    ItemNames.kanan_unlock: 0x0800,
    #ItemNames.kanan_upgrade: 0x1000,
    ItemNames.dia_unlock: 0x2000,
    #ItemNames.dia_upgrade: 0x4000,
    ItemNames.you_unlock: 0x8000,
    #ItemNames.you_upgrade: 0x010000,
    ItemNames.mari_unlock: 0x020000,
    #ItemNames.mari_upgrade: 0x040000,
    ItemNames.hanamaru_unlock: 0x080000,
    #ItemNames.hanamaru_upgrade: 0x100000,
    ItemNames.ruby_unlock: 0x200000,
    #ItemNames.ruby_upgrade: 0x400000,
}

character_item_to_quest_map = {
    ItemNames.chika_unlock: 0x80,
    ItemNames.riko_unlock: 0x0400,
    ItemNames.kanan_unlock: 0x2000,
    ItemNames.hanamaru_unlock: 0x010000,
    ItemNames.ruby_unlock: 0x080000,
    ItemNames.you_unlock: 0x400000,
    ItemNames.dia_unlock: 0x02000000,
    ItemNames.mari_unlock: 0x10000000,
}

character_upgrade_to_area_room = {
    #ItemNames.lailaps_upgrade: (0, [], ""),
    ItemNames.chika_upgrade: (1, [12, 11], LocationNames.katys_mask_room_chest),
    ItemNames.riko_upgrade: (3, [28, 25, 27], LocationNames.spellbook_room_chest),
    ItemNames.kanan_upgrade: (7, [55, 54, 56], LocationNames.tonosamas_parts_room_chest),
    ItemNames.dia_upgrade: (5, [23, 22], LocationNames.scarlet_delta_suit_room_chest),
    ItemNames.you_upgrade: (8, [17, 16, 18], LocationNames.postal_guild_bag_room),
    ItemNames.mari_upgrade: (4, [9, 8, 10], LocationNames.lost_monstie_room_chest),
    ItemNames.hanamaru_upgrade: (2, [19, 24], LocationNames.laptop_room_chest),
    ItemNames.ruby_upgrade: (6, [41, 40, 42], LocationNames.isolated_chest_room_chest),
}