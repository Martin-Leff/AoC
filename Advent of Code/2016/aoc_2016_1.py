import requests
from matplotlib import pyplot as plt

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_1_input.txt'

resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def turn_calc(dir, distance, x, y):
    if dir == 'N':
        y += distance
    elif dir == 'E':
        x += distance
    elif dir == 'S':
        y -= distance
    else:
        x -= distance
    return x, y

def direction_change(cur_dir, turn):
    if cur_dir == 'N' and turn == 'L':
        return 'W'
    elif cur_dir == 'N' and turn == 'R':
        return 'E'
    elif cur_dir == 'E' and turn == 'L':
        return 'N'
    elif cur_dir == 'E' and turn == 'R':
        return 'S'
    elif cur_dir == 'S' and turn == 'L':
        return 'E'
    elif cur_dir == 'S' and turn == 'R':
        return 'W'
    elif cur_dir == 'W' and turn == 'L':
        return 'S'
    else:
        return 'N'

input_text = input_text[0].split(', ')

x = 0
y = 0
direction = 'N'

for step in input_text:
    turn_dir = step[0]
    distance = int(step[1:])
    direction = direction_change(direction, turn_dir)
    x, y = turn_calc(direction, distance, x, y)

total = abs(x) + abs(y)

print('Part 1 Answer:', total)

# Part 2

def turn_calc2(dir, x, y):
    if dir == 'N':
        y += 1
    elif dir == 'E':
        x += 1
    elif dir == 'S':
        y -= 1
    else:
        x -= 1
    return x, y

x = 0
y = 0
direction = 'N'
visited_list = [[x, y]]
min_found = False
vis_x = [x]
vis_y = [y]

for step in input_text:
    turn_dir = step[0]
    distance = int(step[1:])
    direction = direction_change(direction, turn_dir)
    for _ in range(distance):
        x, y = turn_calc2(direction, x, y)
        if [x, y] not in visited_list:
            visited_list.append([x, y])
            vis_x.append(x)
            vis_y.append(y)
        else:
            min_found = True
            break
    if min_found:
        break

total = abs(x) + abs(y)

print('Part 2 Answer:', total)
