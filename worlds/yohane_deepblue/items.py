import typing

from BaseClasses import Item

from .data import ItemNames

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool
    quantity: int = 1

class YohaneDeepblueItem(Item):
    game: str = "YOHANE THE PARHELION -BLAZE in the DEEPBLUE-"

junk_table: typing.Dict[str, ItemData] = {

}

event_table: typing.Dict[str, ItemData] = {
    
}

item_table: typing.Dict[str, ItemData] = {

    **junk_table,
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}

item_groups: typing.Dict[str, str] = {
}