execute as @e[type=chicken] run function eggblock:tick/chicken

execute as @e[type=egg] at @s run function eggblock:tick/egg

execute as @e[type=marker,tag=eggblock_custom_egg,predicate=eggblock:no_vehicle] at @s run function eggblock:hatch_chicken with entity @s data