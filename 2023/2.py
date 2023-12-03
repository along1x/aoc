import os
from operator import mul
from functools import reduce

# bag = {
#     'red': 12,
#     "green": 13,
#     "blue": 14,
# }

total = 0
with open('2023/inputs/2.txt', 'r') as fin:
    line = fin.readline()
    while line: 
        game_num, games = line.split(':')
        game_num = int(game_num[5:])

        cubes = {
            'red': 0, "green": 0, "blue": 0,
        }

        # possible = True
        for game in games.strip().split(";"):
            for pull in game.strip().split(","):
                num, color = pull.strip().split(" ")
                num = int(num.strip())

                cubes[color] = max(cubes[color], num)

                # if num > bag[color.strip()]:
                #     possible = False
                #     break

        #     if not possible:
        #         break

        # if possible:
        #     total += game_num

        power = reduce(mul, cubes.values(), 1)
        print(line, "-", power)
        total += power
            
        line = fin.readline()

print(total)