execute if predicate eggblock:no_type run function eggblock:init_chicken

execute store result score @s eggblock_lay run data get entity @s EggLayTime
execute if score @s eggblock_lay matches 1800.. store result entity @s EggLayTime int 1 run random value 600..1800

execute unless data entity @s {InLove:0} run data merge entity @s {InLove:0,EggLayTime:0}