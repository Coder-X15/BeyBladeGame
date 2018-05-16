"""
Save Load Module
Created by: Roy Mainer, May 2018

Savegame Dictionary Fields:
"player_beyblade"   : name of the player's BB
"opp_beyblade" : name of the opponent's BB

"Profile Dictionary Fields":
"hp"    : BB hit points
"atk"   : BB atk value, how much damage the BB causes other BBs when it hits them
"def"   : BB def value, dmg reduced when BB is hit
"spd"   : BB spd value, movement speed, max radius from the arena center
"""


import os
import shelve
from globals import profiles_path


def save(filename="savegame", save_dict=None):
    if save_dict is None:
        save_dict = {}
    if not any(save_dict):
        print("ERROR: got empty save_dict")
        return False
    save_game_shelf_file = shelve.open(filename)
    for key, val in save_dict.items():
        save_game_shelf_file[key] = val
    save_game_shelf_file.close()
    return


def load(filename="savegame", key=None):
    if key is None:
        print("ERROR: Key is None!")
        return None
    save_game_shelf_file = shelve.open(filename)
    if key not in save_game_shelf_file:
        return None
    val = save_game_shelf_file[key]
    save_game_shelf_file.close()
    return val


def load_profile(beyblade):
    filename = os.path.join(profiles_path, beyblade)
    sf = shelve.open(filename)
    bb_dict = {"hp": None, "atk": None, "def": None, "spd": None}
    for key in bb_dict.keys():
        bb_dict[key] = sf[key]
    sf.close()
    return bb_dict
