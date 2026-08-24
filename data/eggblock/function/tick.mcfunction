execute as @e[type=chicken,nbt=!{Age:0}] run data modify entity @s Age set value 0

execute as @e[type=chicken,predicate=eggblock:no_type] run loot replace entity @s armor.body loot eggblock:chicken_type

execute as @e[type=chicken] store result score @s eggblock_lay run data get entity @s EggLayTime
execute as @e[type=chicken,scores={eggblock_lay=1800..}] store result entity @s EggLayTime int 1 run random value 600..1800

execute as @e[type=egg] at @s run function eggblock:custom_egg with entity @s
execute as @e[type=marker,tag=eggblock_custom_egg,predicate=eggblock:no_vehicle] at @s run function eggblock:summon_random_chicken