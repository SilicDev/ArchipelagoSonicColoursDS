import typing

from BaseClasses import Item

from .data import ItemNames

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool
    quantity: int = 1

class YohaneDeepblueItem(Item):
    game: str = "YOHANE THE PARHELION -BLAZE in the DEEPBLUE-"


character_upgrade_table = {
    #ItemNames.lailaps_upgrade: ItemData(0, True), # Unused
    ItemNames.chika_upgrade: ItemData(1, True),
    ItemNames.riko_upgrade: ItemData(2, True),
    ItemNames.kanan_upgrade: ItemData(3, True),
    ItemNames.hanamaru_upgrade: ItemData(4, True),
    ItemNames.ruby_upgrade: ItemData(5, True),
    ItemNames.you_upgrade: ItemData(6, True),
    ItemNames.dia_upgrade: ItemData(7, True),
    ItemNames.mari_upgrade: ItemData(8, True),
}

unique_accessories_table = {
    ItemNames.extra_accessory_slot: ItemData(9, True, 2), # also 10
    ItemNames.fallen_angels_soarshoes: ItemData(11, True),
    ItemNames.gloves_of_might: ItemData(12, True),
    ItemNames.sea_deitys_charm: ItemData(13, True),
}

breakable_material_table = {
    ItemNames.deepsea_cotton: ItemData(201, False),
}

enemy_material_table = {
    ItemNames.freaky_tentacle: ItemData(232, False),
}

rare_material_table = {
    ItemNames.whale_harp: ItemData(226, False, 2),
    ItemNames.shark_rip: ItemData(270, False),
    ItemNames.ichimonji_scabbard: ItemData(284, False),
    ItemNames.ripple_shell: ItemData(311, False),
    ItemNames.world_pinetree_lumber: ItemData(320, False),
    ItemNames.phantom_jewel: ItemData(321, False),
    ItemNames.lunar_grindstone: ItemData(323, False),
    ItemNames.twinkling_stardust: ItemData(324, False, 2),
    ItemNames.lucent_matter: ItemData(325, False, 2),
    ItemNames.princesss_diary: ItemData(326, False),
    ItemNames.numazu_star: ItemData(327, False, 3),
    ItemNames.torn_collar: ItemData(328, False),
    ItemNames.enchanted_optical_lens: ItemData(329, False),
    ItemNames.lady_of_the_lakes_fin: ItemData(330, False),
    ItemNames.lady_of_the_lakes_bromide: ItemData(331, False),
    ItemNames.bright_red_cloth: ItemData(332, False),
    ItemNames.hole_filled_cube: ItemData(333, False),
    ItemNames.canola_bouquet: ItemData(334, False),
    ItemNames.miniature_train: ItemData(335, False),
    ItemNames.huge_conch: ItemData(336, False),
}

consumables_table = {
    ItemNames.health_potion: ItemData(401, False),
    ItemNames.musical_score: ItemData(419, False),
}

weapons_table = {
    ItemNames.crossbow: ItemData(601, False),
    ItemNames.burstbow: ItemData(602, False),
    ItemNames.mistilteinn: ItemData(603, False),
    ItemNames.tribow: ItemData(604, False),
    ItemNames.tres_perfora: ItemData(605, False),
    ItemNames.autobow: ItemData(606, False),
    ItemNames.ballista: ItemData(607, False),
    ItemNames.dagger: ItemData(608, False),
    ItemNames.stilletto: ItemData(609, False),
    ItemNames.carnwennan: ItemData(610, False),
    ItemNames.tri_knife: ItemData(611, False),
    ItemNames.spread_toss: ItemData(612, False),
    ItemNames.battle_axe: ItemData(613, False),
    ItemNames.great_axe: ItemData(614, False),
    ItemNames.buster_sword: ItemData(615, False),
    ItemNames.the_iron_bludgeoner: ItemData(616, False),
    ItemNames.akatsuki_no_tachi: ItemData(617, False),
    ItemNames.katar: ItemData(618, False),
    ItemNames.broadsword: ItemData(619, False),
    ItemNames.the_slicer: ItemData(620, False),
    ItemNames.balmung: ItemData(621, False),
    ItemNames.katana: ItemData(622, False),
    ItemNames.gekisei: ItemData(623, False),
    ItemNames.threded_blade: ItemData(624, False),
    ItemNames.shamrock: ItemData(625, False),
    ItemNames.demon_slayer: ItemData(626, False),
    ItemNames.claiomh_solais: ItemData(627, False),
}

accessories_table = {
    ItemNames.fortune_tellers_veil: ItemData(801, False),
    ItemNames.cotton_cape: ItemData(802, False),
    ItemNames.diving_suit: ItemData(803, False),
    ItemNames.crimson_cape: ItemData(804, False),
    ItemNames.chainmail_cape: ItemData(805, False),
    ItemNames.chemical_cape: ItemData(806, False),
    ItemNames.chainlink_cloak: ItemData(807, False),
    ItemNames.warriors_cloak: ItemData(808, False),
    ItemNames.silk_cape: ItemData(809, False),
    ItemNames.magical_cape: ItemData(810, False),
    ItemNames.fluffy_coat: ItemData(811, False),
    ItemNames.fireproof_cloak: ItemData(812, False),
    ItemNames.gold_threaded_cape: ItemData(813, False),
    ItemNames.platinum_cloak: ItemData(814, False),
    ItemNames.seaborne_cape: ItemData(815, False),
    ItemNames.bolteaters_garment: ItemData(816, False),
    ItemNames.solar_cloak: ItemData(817, False),
    ItemNames.luminous_cape: ItemData(818, False),
    ItemNames.princesss_cape: ItemData(819, False),
    ItemNames.dusk_garment: ItemData(820, False),
    ItemNames.fallen_angels_cloak_bad: ItemData(821, False),
    ItemNames.fallen_angels_cloak: ItemData(822, False),
    ItemNames.ring: ItemData(823, False),
    ItemNames.bronze_ring: ItemData(824, False),
    ItemNames.silver_ring: ItemData(825, False),
    ItemNames.gold_ring: ItemData(826, False),
    ItemNames.platinum_ring: ItemData(827, False),
    ItemNames.orichalcum_ring: ItemData(828, False),
    ItemNames.cystal_ring: ItemData(829, False),
    ItemNames.ruby_ring: ItemData(830, False),
    ItemNames.diamond_ring: ItemData(831, False),
    ItemNames.alexanderite_ring: ItemData(832, False),
    ItemNames.karkinos_pincer: ItemData(833, False),
    ItemNames.lovecadite: ItemData(834, False),
    ItemNames.medallion_of_numazu: ItemData(835, False),
    ItemNames.lady_of_the_lakes_charm: ItemData(836, False),
    ItemNames.lailaps_collar: ItemData(837, False),
    ItemNames.memorial_locket: ItemData(838, False),
    ItemNames.earring: ItemData(839, False),
    ItemNames.bunny_earring: ItemData(840, False),
    ItemNames.clover_earring: ItemData(841, False),
    ItemNames.beckoning_cat_earring: ItemData(842, False),
    ItemNames.holly_earring: ItemData(843, False),
    ItemNames.bell_earring: ItemData(844, False),
    ItemNames.tattered_cloth: ItemData(845, False),
    ItemNames.crabmet: ItemData(846, False),
    ItemNames.serpent_bracelet: ItemData(847, False),
    ItemNames.holy_circlet: ItemData(848, False),
    ItemNames.static_necklace: ItemData(849, False),
    ItemNames.warlords_bandage: ItemData(850, False),
    ItemNames.phantom_robe: ItemData(851, False),
    ItemNames.magic_mirror_pendant: ItemData(852, False),
    ItemNames.aegis_earring: ItemData(853, False),
    ItemNames.tranquil_foliate: ItemData(854, False),
    ItemNames.hot_blooded_bell: ItemData(855, False),
    ItemNames.motivational_headband: ItemData(856, False),
    ItemNames.analytics_spectacles: ItemData(857, False),
    ItemNames.shades_gauntlet: ItemData(858, False),
    ItemNames.victory_medal: ItemData(859, False),
    ItemNames.lady_of_the_lakes_locket: ItemData(860, False),
    ItemNames.kinek_cube: ItemData(861, False),
    ItemNames.canola_wreath: ItemData(862, False),
    ItemNames.locomotive_pendant: ItemData(863, False),
    ItemNames.fabled_conch: ItemData(864, False),
    ItemNames.goddesss_bracelet: ItemData(865, False),
    ItemNames.sphene_earring: ItemData(866, False),
}

character_unlock_table = { # No actual items exist for these
    ItemNames.lailaps_unlock: ItemData(1000, True),
    ItemNames.chika_unlock: ItemData(1001, True),
    ItemNames.riko_unlock: ItemData(1002, True),
    ItemNames.kanan_unlock: ItemData(1003, True),
    ItemNames.dia_unlock: ItemData(1004, True),
    ItemNames.you_unlock: ItemData(1005, True),
    ItemNames.mari_unlock: ItemData(1006, True),
    ItemNames.hanamaru_unlock: ItemData(1007, True),
    ItemNames.ruby_unlock: ItemData(1008, True),
}

junk_table: typing.Dict[str, ItemData] = {

}

event_table: typing.Dict[str, ItemData] = {
    ItemNames.victory: ItemData(None, True),
}

item_table: typing.Dict[str, ItemData] = {
    **unique_accessories_table,
    **character_unlock_table,
    **character_upgrade_table,
    **breakable_material_table,
    **enemy_material_table,
    **rare_material_table,
    **weapons_table,
    **accessories_table,
    **junk_table,
    "Nothing": ItemData(-1, False),
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}

item_groups: typing.Dict[str, str] = {
    "Accessories": list(unique_accessories_table.keys()),
    "Characters": list(character_unlock_table.keys()),
    "Upgrades": list(character_upgrade_table.keys()),
    "Rare Materials": list(rare_material_table.keys()),
}