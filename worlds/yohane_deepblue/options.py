"""
Option definitions for YOHANE THE PARHELION -BLAZE in the DEEPBLUE-
"""
from dataclasses import dataclass

from Options import (Choice, DeathLink, DefaultOnToggle, OptionSet, NamedRange, Range, Toggle, FreeText,
                     PerGameCommonOptions, OptionGroup, StartInventory, StartInventoryPool, OptionList)

class EarlyChikaBlockMoved(DefaultOnToggle):
    """
    Moves some early Chika blocks to open up the randomizer.
    """
    display_name = "Move Early Chika Blocks"

class EnableYouSkips(DefaultOnToggle):
    """
    If `true` considers using You to fit through 1 tile gaps while in the air in-logic
    """
    display_name = "Enable You Skips"

yohane_deepblue_option_groups = [
    OptionGroup("Logic Customization", [
        EarlyChikaBlockMoved,
        EnableYouSkips
    ])
]

@dataclass
class YohaneDeepblueOptions(PerGameCommonOptions):
    deathlink: DeathLink
    start_inventory_from_pool: StartInventoryPool

    earlychikablocksmoved: EarlyChikaBlockMoved
    enableyouskips: EnableYouSkips