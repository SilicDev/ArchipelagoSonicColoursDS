"""
Option definitions for YOHANE THE PARHELION -BLAZE in the DEEPBLUE-
"""
from dataclasses import dataclass

from Options import (Choice, DeathLink, DefaultOnToggle, OptionSet, NamedRange, Range, Toggle, FreeText,
                     PerGameCommonOptions, OptionGroup, StartInventory, OptionList)

yohane_deepblue_option_groups = [
    
]

@dataclass
class YohaneDeepblueOptions(PerGameCommonOptions):
    pass