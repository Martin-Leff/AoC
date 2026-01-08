import requests
from itertools import combinations

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_3_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

def next_coord(coord, direction):
    if direction == 'R':
        new_coord = (coord[0] + 1, coord[1])
    elif direction == 'U':
        new_coord = (coord[0], coord[1] + 1)
    elif direction == 'L':
        new_coord = (coord[0] - 1, coord[1])
    else:
        new_coord = (coord[0], coord[1] - 1)

    return new_coord

def direction_switch(direction):
    if direction == 'R':
        direction = 'U'
    elif direction == 'U':
        direction = 'L'
    elif direction == 'L':
        direction = 'D'
    else:
        direction = 'R'
    return direction

end = int(input_text)

i = 1
x = 0
y = 0
coord = (x, y)
coord_dict = {coord: i}
direction = 'R'

while i < end:
    i += 1
    new_coord = next_coord(coord, direction)
    coord_dict.update({new_coord: i})
    coord = new_coord
    x = coord[0]
    y = coord[1]

    if ((direction == 'R' and (x, y + 1) not in coord_dict) or
            (direction == 'U' and (x - 1, y) not in coord_dict) or
            (direction == 'L' and (x, y - 1) not in coord_dict) or
            (direction == 'D' and (x + 1, y) not in coord_dict)):
        direction = direction_switch(direction)

end_coords = [key for key, val in coord_dict.items() if val == end][0]

steps = abs(end_coords[0]) + abs(end_coords[1])

print('Part 1 Answer:', steps)

# Part 2

def total_neighbors(x, y, coord_dict):
    up = (x, y + 1)
    up_right = (x + 1, y + 1)
    right = (x + 1, y)
    down_right = (x + 1, y - 1)
    down = (x, y - 1)
    down_left = (x - 1, y - 1)
    left = (x - 1, y)
    up_left = (x - 1, y + 1)
    directions = [up, up_right, right, down_right, down, down_left, left, up_left]

    total = 0
    for direction in directions:
        if direction in coord_dict:
            total += coord_dict[direction]

    return total

i = 1
x = 0
y = 0
coord = (x, y)
coord_dict = {coord: i}
direction = 'R'

while i < end:
    new_coord = next_coord(coord, direction)
    coord = new_coord
    x = coord[0]
    y = coord[1]
    i = total_neighbors(x, y, coord_dict)
    coord_dict.update({new_coord: i})

    if ((direction == 'R' and (x, y + 1) not in coord_dict) or
            (direction == 'U' and (x - 1, y) not in coord_dict) or
            (direction == 'L' and (x, y - 1) not in coord_dict) or
            (direction == 'D' and (x + 1, y) not in coord_dict)):
        direction = direction_switch(direction)

print('Part 2 Answer:', i)