"""
Option definitions for Sonic Colours (DS)
"""
from dataclasses import dataclass

from Options import (Choice, DeathLink, DefaultOnToggle, OptionSet, NamedRange, Range, Toggle, FreeText,
                     PerGameCommonOptions, OptionGroup, StartInventory, OptionList)

class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten.

    - Nega-Wisp Armor: Beat Eggman at the end of Terminal Velocity (requires all Wisps)
    - Nega-Mother Wisp: Beat the Nega-Mother Wisp after collecting all seven Chaos Emeralds
    """
    display_name = "Goal"
    default = 0
    option_wisp_armor = 0
    option_mother_wisp = 1

class RankRequirement(Choice):
    """
    The rank required to consider a level beaten.
    """
    display_name = "Rank Requirement"
    default = 0
    option_rank_d = 0
    option_rank_c = 1
    option_rank_b = 2
    option_rank_a = 3
    option_rank_s = 4

class RedRingSanity(Toggle):
    """
    Collecting a Red Star Ring gives you an item.
    """
    display_name = "Red Ring Sanity"

scds_option_groups = [
    OptionGroup("Goal Options", [
        Goal,
        RankRequirement
    ]),
    OptionGroup("Sanity Options", [
        RedRingSanity
    ])
]

@dataclass
class SonicColoursDSOptions(PerGameCommonOptions):
    goal: Goal
    rankrequirement: RankRequirement

    redringsanity: RedRingSanity