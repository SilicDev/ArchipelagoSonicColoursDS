import typing

from BaseClasses import Item

from .data import ItemNames

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool
    quantity: int = 1

class YohaneDeepblueItem(Item):
    game: str = "YOHANE THE PARHELION -BLAZE in the DEEPBLUE-"

unique_accessories_table = {
    ItemNames.sea_deitys_charm: ItemData(1, True),
    ItemNames.fallen_angels_soarshoes: ItemData(2, True),
    ItemNames.gloves_of_might: ItemData(3, True),
    ItemNames.extra_accessory_slot: ItemData(4, True, 2),
}

character_unlock_table = {
    ItemNames.lailaps_unlock: ItemData(10, True),
    ItemNames.chika_unlock: ItemData(11, True),
    ItemNames.riko_unlock: ItemData(12, True),
    ItemNames.kanan_unlock: ItemData(13, True),
    ItemNames.dia_unlock: ItemData(14, True),
    ItemNames.you_unlock: ItemData(15, True),
    ItemNames.mari_unlock: ItemData(16, True),
    ItemNames.hanamaru_unlock: ItemData(17, True),
    ItemNames.ruby_unlock: ItemData(18, True),
}

character_upgrade_table = {
    #ItemNames.lailaps_upgrade: ItemData(30, True), # Unused
    ItemNames.chika_upgrade: ItemData(31, True),
    ItemNames.riko_upgrade: ItemData(32, True),
    ItemNames.kanan_upgrade: ItemData(33, True),
    ItemNames.dia_upgrade: ItemData(34, True),
    ItemNames.you_upgrade: ItemData(35, True),
    ItemNames.mari_upgrade: ItemData(36, True),
    ItemNames.hanamaru_upgrade: ItemData(37, True),
    ItemNames.ruby_upgrade: ItemData(38, True),
}

rare_material_table = {
    ItemNames.bright_red_cloth: ItemData(50, False),
    ItemNames.canola_bouquet: ItemData(51, False),
    ItemNames.enchanted_optical_lens: ItemData(52, False),
    ItemNames.hole_filled_cube: ItemData(53, False),
    ItemNames.huge_conch: ItemData(54, False),
    ItemNames.ichimonji_scabbard: ItemData(55, False),
    ItemNames.lady_of_the_lakes_bromide: ItemData(56, False),
    ItemNames.lady_of_the_lakes_fin: ItemData(57, False),
    ItemNames.lucent_matter: ItemData(58, False, 2),
    ItemNames.lunar_grindstone: ItemData(59, False),
    ItemNames.miniature_train: ItemData(60, False),
    ItemNames.numazu_star: ItemData(61, False, 3),
    ItemNames.phantom_jewel: ItemData(62, False),
    ItemNames.princesss_diary: ItemData(63, False),
    ItemNames.ripple_spell: ItemData(64, False),
    ItemNames.shark_rip: ItemData(65, False),
    ItemNames.torn_collar: ItemData(66, False),
    ItemNames.twinkling_stardust: ItemData(67, False, 2),
    ItemNames.whale_harp: ItemData(68, False, 2),
    ItemNames.world_pinetree_lumber: ItemData(69, False),
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
    **rare_material_table,
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