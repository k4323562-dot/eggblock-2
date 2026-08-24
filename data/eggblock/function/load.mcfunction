scoreboard objectives add eggblock_lay dummy

execute unless data storage eggblock:settings hatch_chance run data merge storage eggblock:settings {hatch_chance:0.5}