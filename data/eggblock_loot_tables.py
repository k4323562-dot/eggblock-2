import os, sys, urllib.request
from pathlib import Path


if len(sys.argv) > 1:
    MCVERSION = sys.argv[1]
else:
#### SET MINECRAFT VERSION MANUALLY HERE ####
    MCVERSION = "26.3-snapshot-9"


os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not Path.cwd().name == "data":
    print("Working directory not named 'data'! bldp generation scripts must be stored within the 'data' folder of your pack to generate correctly!")
    input("Press Enter to exit program...")
    sys.exit()

if not Path("bldp.py").is_file():
    with open("bldp.py", "w", encoding="utf-8") as bldp_main:
        bldp_main.write(urllib.request.urlopen("https://raw.githubusercontent.com/blockerlocker/bldp/main/data/bldp.py").read().decode('utf-8'))

import bldp

bldp.remove_path("minecraft/loot_table/gameplay/chicken_lay.json")
bldp.remove_path("eggblock/loot_table/chicken_type.json")

item_list = bldp.get_registry_data(MCVERSION,"item")

egg_loot_table = {
    "type": "minecraft:gift",
    "pools": [
        {
            "entries": [
                {
                    "type": "minecraft:alternatives",
                    "children": []
                }
            ],
            "rolls": 1
        }
    ],
    "random_sequence": "minecraft:gameplay/chicken_lay"
}

chicken_type_loot_table = {
    "pools": [
        {
            "entries": [],
            "rolls": 1,
            "modifier": {
                "type": "minecraft:set_components",
                "components": {
                    "minecraft:equippable": {
                        "slot": "body"
                    }
                }
            }
        }
    ]
}

for item in item_list:
    if item != "air":
        egg_entry = {
            "type": "minecraft:item",
            "condition": {
                "type": "minecraft:entity_properties",
                "entity": "this",
                "predicate": {
                    "minecraft:equipment": {
                        "body": {
                            "items": item
                        }
                    }
                }
            },
            "name": item
        }

        egg_loot_table["pools"][0]["entries"][0]["children"].append(egg_entry)
        chicken_type_loot_table["pools"][0]["entries"].append({"type":"item","name":item})

bldp.json_to_file(egg_loot_table,"minecraft/loot_table/gameplay","chicken_lay")
bldp.json_to_file(chicken_type_loot_table,"eggblock/loot_table","chicken_type")