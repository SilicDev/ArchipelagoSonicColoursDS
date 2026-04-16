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
    LocationNames.annoying_teleporting_fish_room_chest: (0x512F8, 0x08), #!
    LocationNames.wallcrab_chest_room_chest: (0x512F8, 0x10), #!
    LocationNames.dumb_block_room_chest: (0x512AB, 0x80), #!
    LocationNames.lost_monstie_room_chest: (0x512AB, 0x20),

    LocationNames.one_way_slide_room_chest: (0x512B3, 0x10), #!
    LocationNames.giant_sliding_crystals_room_chest: (0x512B3, 0x20), #!
    LocationNames.isolated_chest_room_chest: (0x512B3, 0x40), #!
    LocationNames.looong_slide_room_chest: (0x51300, 0x01),
    LocationNames.mari_issue_room_chest: (0x51300, 0x02),

    LocationNames.giant_poison_enemy_crab_room_chest: (0x512AF, 0x40), #!
    LocationNames.scarlet_delta_suit_room_chest: (0x512AF, 0x80),
    LocationNames.golden_snail_room_chest: (0x512FC, 0x01), #!
    LocationNames.slope_room_chest: (0x512FC, 0x04), #!
    LocationNames.you_testing_grounds_chest: (0x512FC, 0x08),

    LocationNames.purple_goo_room_chest: (0x512BF, 0x40),
    LocationNames.dark_room_chest: (0x512BF, 0x20),
}