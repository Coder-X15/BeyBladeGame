import os
import shelve
from globals import profiles_path

BEYBLADES = {"phantom_orion": {"hp": 90,  "atk": 20, "def": 10, "spd": 80},
             "samurai_ifrit": {"hp": 100, "atk": 15, "def": 15, "spd": 70},
             "big_bang_pegasus":     {"hp": 100, "atk": 20, "def": 10, "spd": 70},
             "gladiator_bahamut":       {"hp": 110, "atk": 30, "def": 30, "spd": 60},
             "pirate_orochi":      {"hp": 100, "atk": 30, "def": 30, "spd": 65},
             "xeno_xcalibur":    {"hp": 95,  "atk": 35, "def": 35, "spd": 55},
             "arc_bahamut":      {"hp": 110, "atk": 30, "def": 50, "spd": 50},
             "hades_kerbecs":      {"hp": 110, "atk": 20, "def": 60, "spd": 60},
             "pirate_kraken":      {"hp": 100, "atk": 60, "def": 30, "spd": 50},
             "blitz_striker":     {"hp": 90,  "atk": 55, "def": 20, "spd": 55}}


def delete_profiles():
    for f in os.listdir(profiles_path):
        filename = os.path.join(profiles_path, f)
        try:
            if os.path.isfile(filename):
                os.unlink(filename)
        except Exception as e:
            print(e)


def create_profiles():
    delete_profiles()
    for beyblade, profile in BEYBLADES.items():
        # path = os.path.join(os.getcwd(), profiles_path)
        # filename = os.path.join(path, beyblade)
        filename = os.path.join(profiles_path, beyblade)
        print(filename)
        shelf_file = shelve.open(filename)
        for key, val in profile.items():
            shelf_file[key] = val
        shelf_file.close()
    return


if __name__ == "__main__":
    create_profiles()

