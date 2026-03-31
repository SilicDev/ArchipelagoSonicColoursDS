"""
Option definitions for Sonic Colours (DS)
"""
from dataclasses import dataclass

from Options import (Choice, DeathLink, DefaultOnToggle, OptionSet, NamedRange, Range, Toggle, FreeText,
                     PerGameCommonOptions, OptionGroup, StartInventory, OptionList)

class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten.

    - Nega Wisp Armor: Beat Eggman at the end of Terminal Velocity (requires all Wisps)
    - Nega Mother Wisp: Beat the Nega Mother Wisp after collecting all seven chaos emeralds
    """
    display_name = "Goal"
    default = 0
    option_wisp_armor = 0
    option_mother_wisp = 1

class RedRingSanity(Toggle):
    """
    Collecting a ring gives you an item.
    """
    display_name = "RedRingSanity"

@dataclass
class SonicColoursDSOptions(PerGameCommonOptions):
    goal: Goal

    redringsanity: RedRingSanity