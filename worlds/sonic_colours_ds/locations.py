import typing

from BaseClasses import Location
from worlds.AutoWorld import World

from .data import LocationNames

class SonicColoursDSLocation(Location):
    game: str = "Sonic Colours (DS)"

level_clear_table = {
    LocationNames.movement_tutorial: 0,
    LocationNames.white_wisp_tutorial: 1,
    LocationNames.red_wisp_tutorial: 2,
    LocationNames.orange_wisp_tutorial: 3,
    LocationNames.yellow_wisp_tutorial: 4,
    LocationNames.cyan_wisp_tutorial: 5,
    LocationNames.violet_wisp_tutorial: 6,

    LocationNames.tropical_resort_act_1: 10,
    LocationNames.tropical_resort_act_2: 11,
    LocationNames.tropical_resort_boss: 12,
    LocationNames.tropical_resort_mission_1: 13,
    LocationNames.tropical_resort_mission_2: 14,
    LocationNames.tropical_resort_mission_3: 15,

    LocationNames.sweet_mountain_act_1: 20,
    LocationNames.sweet_mountain_act_2: 21,
    LocationNames.sweet_mountain_boss: 22,
    LocationNames.sweet_mountain_mission_1: 23,
    LocationNames.sweet_mountain_mission_2: 24,
    LocationNames.sweet_mountain_mission_3: 25,

    LocationNames.starlight_carnival_act_1: 30,
    LocationNames.starlight_carnival_act_2: 31,
    LocationNames.starlight_carnival_boss: 32,
    LocationNames.starlight_carnival_mission_1: 33,
    LocationNames.starlight_carnival_mission_2: 34,
    LocationNames.starlight_carnival_mission_3: 35,

    LocationNames.planet_wisp_act_1: 40,
    LocationNames.planet_wisp_act_2: 41,
    LocationNames.planet_wisp_boss: 42,
    LocationNames.planet_wisp_mission_1: 43,
    LocationNames.planet_wisp_mission_2: 44,
    LocationNames.planet_wisp_mission_3: 45,

    LocationNames.aquarium_park_act_1: 50,
    LocationNames.aquarium_park_act_2: 51,
    LocationNames.aquarium_park_boss: 52,
    LocationNames.aquarium_park_mission_1: 53,
    LocationNames.aquarium_park_mission_2: 54,
    LocationNames.aquarium_park_mission_3: 55,

    LocationNames.asteroid_coaster_act_1: 60,
    LocationNames.asteroid_coaster_act_2: 61,
    LocationNames.asteroid_coaster_boss: 62,
    LocationNames.asteroid_coaster_mission_1: 63,
    LocationNames.asteroid_coaster_mission_2: 64,
    LocationNames.asteroid_coaster_mission_3: 65,

    LocationNames.terminal_velocity_chase: 70
}

red_rings_table = {
    LocationNames.tropical_resort_act_1_red_ring_1: 100,
    LocationNames.tropical_resort_act_1_red_ring_2: 101,
    LocationNames.tropical_resort_act_1_red_ring_3: 102,
    LocationNames.tropical_resort_act_1_red_ring_4: 103,
    LocationNames.tropical_resort_act_1_red_ring_5: 104,
    
    LocationNames.tropical_resort_act_2_red_ring_1: 110,
    LocationNames.tropical_resort_act_2_red_ring_2: 111,
    LocationNames.tropical_resort_act_2_red_ring_3: 112,
    LocationNames.tropical_resort_act_2_red_ring_4: 113,
    LocationNames.tropical_resort_act_2_red_ring_5: 114,

    LocationNames.tropical_resort_mission_1_red_ring_1: 120,
    LocationNames.tropical_resort_mission_1_red_ring_2: 121,
    LocationNames.tropical_resort_mission_2_red_ring_1: 123,
    LocationNames.tropical_resort_mission_2_red_ring_2: 124,
    LocationNames.tropical_resort_mission_3_red_ring_1: 126,
    LocationNames.tropical_resort_mission_3_red_ring_2: 127,

    LocationNames.sweet_mountain_act_1_red_ring_1: 130,
    LocationNames.sweet_mountain_act_1_red_ring_2: 131,
    LocationNames.sweet_mountain_act_1_red_ring_3: 132,
    LocationNames.sweet_mountain_act_1_red_ring_4: 133,
    LocationNames.sweet_mountain_act_1_red_ring_5: 134,

    LocationNames.sweet_mountain_act_2_red_ring_1: 140,
    LocationNames.sweet_mountain_act_2_red_ring_2: 141,
    LocationNames.sweet_mountain_act_2_red_ring_3: 142,
    LocationNames.sweet_mountain_act_2_red_ring_4: 143,
    LocationNames.sweet_mountain_act_2_red_ring_5: 144,

    LocationNames.sweet_mountain_mission_1_red_ring_1: 150,
    LocationNames.sweet_mountain_mission_1_red_ring_2: 151,
    LocationNames.sweet_mountain_mission_2_red_ring_1: 153,
    LocationNames.sweet_mountain_mission_2_red_ring_2: 154,
    LocationNames.sweet_mountain_mission_3_red_ring_1: 156,
    LocationNames.sweet_mountain_mission_3_red_ring_2: 157,

    LocationNames.starlight_carnival_act_1_red_ring_1: 160,
    LocationNames.starlight_carnival_act_1_red_ring_2: 161,
    LocationNames.starlight_carnival_act_1_red_ring_3: 162,
    LocationNames.starlight_carnival_act_1_red_ring_4: 163,
    LocationNames.starlight_carnival_act_1_red_ring_5: 164,

    LocationNames.starlight_carnival_act_2_red_ring_1: 170,
    LocationNames.starlight_carnival_act_2_red_ring_2: 171,
    LocationNames.starlight_carnival_act_2_red_ring_3: 172,
    LocationNames.starlight_carnival_act_2_red_ring_4: 173,
    LocationNames.starlight_carnival_act_2_red_ring_5: 174,

    LocationNames.starlight_carnival_mission_1_red_ring_1: 180,
    LocationNames.starlight_carnival_mission_1_red_ring_2: 181,
    LocationNames.starlight_carnival_mission_2_red_ring_1: 183,
    LocationNames.starlight_carnival_mission_2_red_ring_2: 184,
    LocationNames.starlight_carnival_mission_3_red_ring_1: 186,
    LocationNames.starlight_carnival_mission_3_red_ring_2: 187,

    LocationNames.planet_wisp_act_1_red_ring_1: 190,
    LocationNames.planet_wisp_act_1_red_ring_2: 191,
    LocationNames.planet_wisp_act_1_red_ring_3: 192,
    LocationNames.planet_wisp_act_1_red_ring_4: 193,
    LocationNames.planet_wisp_act_1_red_ring_5: 194,

    LocationNames.planet_wisp_act_2_red_ring_1: 200,
    LocationNames.planet_wisp_act_2_red_ring_2: 201,
    LocationNames.planet_wisp_act_2_red_ring_3: 202,
    LocationNames.planet_wisp_act_2_red_ring_4: 203,
    LocationNames.planet_wisp_act_2_red_ring_5: 204,

    LocationNames.planet_wisp_mission_1_red_ring_1: 210,
    LocationNames.planet_wisp_mission_1_red_ring_2: 211,
    LocationNames.planet_wisp_mission_2_red_ring_1: 213,
    LocationNames.planet_wisp_mission_2_red_ring_2: 214,
    LocationNames.planet_wisp_mission_3_red_ring_1: 216,
    LocationNames.planet_wisp_mission_3_red_ring_2: 217,

    LocationNames.aquarium_park_act_1_red_ring_1: 220,
    LocationNames.aquarium_park_act_1_red_ring_2: 221,
    LocationNames.aquarium_park_act_1_red_ring_3: 222,
    LocationNames.aquarium_park_act_1_red_ring_4: 223,
    LocationNames.aquarium_park_act_1_red_ring_5: 224,

    LocationNames.aquarium_park_act_2_red_ring_1: 230,
    LocationNames.aquarium_park_act_2_red_ring_2: 231,
    LocationNames.aquarium_park_act_2_red_ring_3: 232,
    LocationNames.aquarium_park_act_2_red_ring_4: 233,
    LocationNames.aquarium_park_act_2_red_ring_5: 234,

    LocationNames.aquarium_park_mission_1_red_ring_1: 240,
    LocationNames.aquarium_park_mission_1_red_ring_2: 241,
    LocationNames.aquarium_park_mission_2_red_ring_1: 243,
    LocationNames.aquarium_park_mission_2_red_ring_2: 244,
    LocationNames.aquarium_park_mission_3_red_ring_1: 246,
    LocationNames.aquarium_park_mission_3_red_ring_2: 247,

    LocationNames.asteroid_coaster_act_1_red_ring_1: 250,
    LocationNames.asteroid_coaster_act_1_red_ring_2: 251,
    LocationNames.asteroid_coaster_act_1_red_ring_3: 252,
    LocationNames.asteroid_coaster_act_1_red_ring_4: 253,
    LocationNames.asteroid_coaster_act_1_red_ring_5: 254,

    LocationNames.asteroid_coaster_act_2_red_ring_1: 260,
    LocationNames.asteroid_coaster_act_2_red_ring_2: 261,
    LocationNames.asteroid_coaster_act_2_red_ring_3: 262,
    LocationNames.asteroid_coaster_act_2_red_ring_4: 263,
    LocationNames.asteroid_coaster_act_2_red_ring_5: 264,

    LocationNames.asteroid_coaster_mission_1_red_ring_1: 270,
    LocationNames.asteroid_coaster_mission_1_red_ring_2: 271,
    LocationNames.asteroid_coaster_mission_2_red_ring_1: 273,
    LocationNames.asteroid_coaster_mission_2_red_ring_2: 274,
    LocationNames.asteroid_coaster_mission_3_red_ring_1: 276,
    LocationNames.asteroid_coaster_mission_3_red_ring_2: 277,
}

special_stage_table = {
    LocationNames.special_stage_1: 280,
    LocationNames.special_stage_2: 281,
    LocationNames.special_stage_3: 282,
    LocationNames.special_stage_4: 283,
    LocationNames.special_stage_5: 284,
    LocationNames.special_stage_6: 285,
    LocationNames.special_stage_7: 286,
}

location_table = {
    **level_clear_table,
    **red_rings_table,
    **special_stage_table,
}

tropical_resort_region_locations = [
    LocationNames.movement_tutorial,
    LocationNames.white_wisp_tutorial,

    LocationNames.tropical_resort_act_1,
    LocationNames.tropical_resort_act_1_red_ring_1,
    LocationNames.tropical_resort_act_1_red_ring_2,
    LocationNames.tropical_resort_act_1_red_ring_3,
    LocationNames.tropical_resort_act_1_red_ring_4,
    LocationNames.tropical_resort_act_1_red_ring_5,

    LocationNames.tropical_resort_act_2,
    LocationNames.tropical_resort_act_2_red_ring_1,
    LocationNames.tropical_resort_act_2_red_ring_2,
    LocationNames.tropical_resort_act_2_red_ring_3,
    LocationNames.tropical_resort_act_2_red_ring_4,
    LocationNames.tropical_resort_act_2_red_ring_5,

    LocationNames.tropical_resort_mission_1,
    LocationNames.tropical_resort_mission_1_red_ring_1,
    LocationNames.tropical_resort_mission_1_red_ring_2,

    LocationNames.tropical_resort_mission_2,
    LocationNames.tropical_resort_mission_2_red_ring_1,
    LocationNames.tropical_resort_mission_2_red_ring_2,

    LocationNames.tropical_resort_mission_3,
    LocationNames.tropical_resort_mission_3_red_ring_1,
    LocationNames.tropical_resort_mission_3_red_ring_2,

    LocationNames.tropical_resort_boss,
]

sweet_mountain_region_locations = [
    LocationNames.red_wisp_tutorial,

    LocationNames.sweet_mountain_act_1,
    LocationNames.sweet_mountain_act_1_red_ring_1,
    LocationNames.sweet_mountain_act_1_red_ring_2,
    LocationNames.sweet_mountain_act_1_red_ring_3,
    LocationNames.sweet_mountain_act_1_red_ring_4,
    LocationNames.sweet_mountain_act_1_red_ring_5,

    LocationNames.sweet_mountain_act_2,
    LocationNames.sweet_mountain_act_2_red_ring_1,
    LocationNames.sweet_mountain_act_2_red_ring_2,
    LocationNames.sweet_mountain_act_2_red_ring_3,
    LocationNames.sweet_mountain_act_2_red_ring_4,
    LocationNames.sweet_mountain_act_2_red_ring_5,

    LocationNames.sweet_mountain_mission_1,
    LocationNames.sweet_mountain_mission_1_red_ring_1,
    LocationNames.sweet_mountain_mission_1_red_ring_2,

    LocationNames.sweet_mountain_mission_2,
    LocationNames.sweet_mountain_mission_2_red_ring_1,
    LocationNames.sweet_mountain_mission_2_red_ring_2,

    LocationNames.sweet_mountain_mission_3,
    LocationNames.sweet_mountain_mission_3_red_ring_1,
    LocationNames.sweet_mountain_mission_3_red_ring_2,

    LocationNames.sweet_mountain_boss,
]

starlight_carnival_region_locations = [
    LocationNames.orange_wisp_tutorial,

    LocationNames.starlight_carnival_act_1,
    LocationNames.starlight_carnival_act_1_red_ring_1,
    LocationNames.starlight_carnival_act_1_red_ring_2,
    LocationNames.starlight_carnival_act_1_red_ring_3,
    LocationNames.starlight_carnival_act_1_red_ring_4,
    LocationNames.starlight_carnival_act_1_red_ring_5,

    LocationNames.starlight_carnival_act_2,
    LocationNames.starlight_carnival_act_2_red_ring_1,
    LocationNames.starlight_carnival_act_2_red_ring_2,
    LocationNames.starlight_carnival_act_2_red_ring_3,
    LocationNames.starlight_carnival_act_2_red_ring_4,
    LocationNames.starlight_carnival_act_2_red_ring_5,

    LocationNames.starlight_carnival_mission_1,
    LocationNames.starlight_carnival_mission_1_red_ring_1,
    LocationNames.starlight_carnival_mission_1_red_ring_2,

    LocationNames.starlight_carnival_mission_2,
    LocationNames.starlight_carnival_mission_2_red_ring_1,
    LocationNames.starlight_carnival_mission_2_red_ring_2,

    LocationNames.starlight_carnival_mission_3,
    LocationNames.starlight_carnival_mission_3_red_ring_1,
    LocationNames.starlight_carnival_mission_3_red_ring_2,

    LocationNames.starlight_carnival_boss,
]

planet_wisp_region_locations = [
    LocationNames.yellow_wisp_tutorial,

    LocationNames.planet_wisp_act_1,
    LocationNames.planet_wisp_act_1_red_ring_1,
    LocationNames.planet_wisp_act_1_red_ring_2,
    LocationNames.planet_wisp_act_1_red_ring_3,
    LocationNames.planet_wisp_act_1_red_ring_4,
    LocationNames.planet_wisp_act_1_red_ring_5,

    LocationNames.planet_wisp_act_2,
    LocationNames.planet_wisp_act_2_red_ring_1,
    LocationNames.planet_wisp_act_2_red_ring_2,
    LocationNames.planet_wisp_act_2_red_ring_3,
    LocationNames.planet_wisp_act_2_red_ring_4,
    LocationNames.planet_wisp_act_2_red_ring_5,

    LocationNames.planet_wisp_mission_1,
    LocationNames.planet_wisp_mission_1_red_ring_1,
    LocationNames.planet_wisp_mission_1_red_ring_2,

    LocationNames.planet_wisp_mission_2,
    LocationNames.planet_wisp_mission_2_red_ring_1,
    LocationNames.planet_wisp_mission_2_red_ring_2,

    LocationNames.planet_wisp_mission_3,
    LocationNames.planet_wisp_mission_3_red_ring_1,
    LocationNames.planet_wisp_mission_3_red_ring_2,

    LocationNames.planet_wisp_boss,
]

aquarium_park_region_locations = [
    LocationNames.cyan_wisp_tutorial,

    LocationNames.aquarium_park_act_1,
    LocationNames.aquarium_park_act_1_red_ring_1,
    LocationNames.aquarium_park_act_1_red_ring_2,
    LocationNames.aquarium_park_act_1_red_ring_3,
    LocationNames.aquarium_park_act_1_red_ring_4,
    LocationNames.aquarium_park_act_1_red_ring_5,

    LocationNames.aquarium_park_act_2,
    LocationNames.aquarium_park_act_2_red_ring_1,
    LocationNames.aquarium_park_act_2_red_ring_2,
    LocationNames.aquarium_park_act_2_red_ring_3,
    LocationNames.aquarium_park_act_2_red_ring_4,
    LocationNames.aquarium_park_act_2_red_ring_5,

    LocationNames.aquarium_park_mission_1,
    LocationNames.aquarium_park_mission_1_red_ring_1,
    LocationNames.aquarium_park_mission_1_red_ring_2,

    LocationNames.aquarium_park_mission_2,
    LocationNames.aquarium_park_mission_2_red_ring_1,
    LocationNames.aquarium_park_mission_2_red_ring_2,

    LocationNames.aquarium_park_mission_3,
    LocationNames.aquarium_park_mission_3_red_ring_1,
    LocationNames.aquarium_park_mission_3_red_ring_2,

    LocationNames.aquarium_park_boss,
]

asteroid_coaster_region_locations = [
    LocationNames.violet_wisp_tutorial,

    LocationNames.asteroid_coaster_act_1,
    LocationNames.asteroid_coaster_act_1_red_ring_1,
    LocationNames.asteroid_coaster_act_1_red_ring_2,
    LocationNames.asteroid_coaster_act_1_red_ring_3,
    LocationNames.asteroid_coaster_act_1_red_ring_4,
    LocationNames.asteroid_coaster_act_1_red_ring_5,

    LocationNames.asteroid_coaster_act_2,
    LocationNames.asteroid_coaster_act_2_red_ring_1,
    LocationNames.asteroid_coaster_act_2_red_ring_2,
    LocationNames.asteroid_coaster_act_2_red_ring_3,
    LocationNames.asteroid_coaster_act_2_red_ring_4,
    LocationNames.asteroid_coaster_act_2_red_ring_5,

    LocationNames.asteroid_coaster_mission_1,
    LocationNames.asteroid_coaster_mission_1_red_ring_1,
    LocationNames.asteroid_coaster_mission_1_red_ring_2,

    LocationNames.asteroid_coaster_mission_2,
    LocationNames.asteroid_coaster_mission_2_red_ring_1,
    LocationNames.asteroid_coaster_mission_2_red_ring_2,

    LocationNames.asteroid_coaster_mission_3,
    LocationNames.asteroid_coaster_mission_3_red_ring_1,
    LocationNames.asteroid_coaster_mission_3_red_ring_2,

    LocationNames.asteroid_coaster_boss,
]

terminal_velocity_region_locations = [
    LocationNames.terminal_velocity_chase,
    LocationNames.nega_wisp_armor,
]

def setup_locations(world: World, player: int):
    locations = {}

    locations.update({**level_clear_table})
    locations.update({**special_stage_table})

    if world.options.redringsanity:
        locations.update({**red_rings_table})
    if world.options.goal.value == 0:
        locations.update({LocationNames.nega_wisp_armor: None})
    elif world.options.goal.value == 1:
        locations.update({
            LocationNames.nega_wisp_armor: 80,
            LocationNames.nega_mother_wisp: None
        })

    return locations

lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in location_table.items()}

location_groups = {
    "Level Clear": list(level_clear_table.keys()),
    "Red Rings": list(red_rings_table.keys()),
    "Special Stage": list(special_stage_table.keys()),
    "Tutorial": {
        LocationNames.movement_tutorial,
        LocationNames.white_wisp_tutorial,
        LocationNames.red_wisp_tutorial,
        LocationNames.orange_wisp_tutorial,
        LocationNames.yellow_wisp_tutorial,
        LocationNames.cyan_wisp_tutorial,
        LocationNames.violet_wisp_tutorial,
    },
    "Tropical Resort": tropical_resort_region_locations,
    "Sweet Mountain": sweet_mountain_region_locations,
    "Starlight Carnival": starlight_carnival_region_locations,
    "Planet Wisp": planet_wisp_region_locations,
    "Aquarium Park": aquarium_park_region_locations,
    "Asteroid Coaster": asteroid_coaster_region_locations,
    "Terminal Velocity": terminal_velocity_region_locations,
}