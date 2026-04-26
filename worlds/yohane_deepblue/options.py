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

class ProgressiveCharacterUnlocks(Toggle):
    """
    If `true` places progressive unlocks for characters and upgrades instead of individual ones.
    
    Example: Two items "Progressive Chika" instead of "Chika" and "Katy's Mask"
    """
    display_name = "Progressive Character Unlocks"

class UpgradeHints(OptionSet):
    """
    The type of hints to create when obtaining a character.

    - Vanilla: Hints what item is at the normal upgrade chest
    - AP: Hints where the upgrade item is located.
    """
    display_name = "Upgrade Hints"
    valid_keys = frozenset({"Vanilla", "AP"})
    default = frozenset({"Vanilla"})
    
    _option_vanilla = "Vanilla"
    _option_ap = "AP"

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

    progressive_character_unlocks: ProgressiveCharacterUnlocks
    upgrade_hints: UpgradeHints

    earlychikablocksmoved: EarlyChikaBlockMoved
    enableyouskips: EnableYouSkips

