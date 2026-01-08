import requests
import itertools
import math

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_24_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def print_map(coord_dict, input_text):
    for y in range(len(input_text)):
        line = input_text[y]
        for x in range(len(line)):
            print(coord_dict[(x, y)], end='')
        print('')


def check_neighbor(coord, coord_dict_temp, target_found, new_start):
    x = coord[0]
    y = coord[1]
    left = (x - 1, y)
    right = (x + 1, y)
    up = (x, y + 1)
    down = (x, y - 1)
    directions = [left, right, up, down]
    for direction in directions:
        if coord_dict_temp[direction] not in [wall, seen]:
            if coord_dict_temp[direction] != passage:
                target_found = True
                new_start = direction
            else:
                coord_dict_temp.update({direction: seen})

    return coord_dict_temp, target_found, new_start

coord_dict = {}

y = 0

for y in range(len(input_text)):
    line = input_text[y]
    for x in range(len(line)):
        char = input_text[y][x]
        coord_dict.update({(x, y): char})

wall = '#'
passage = '.'
seen = '_'
start = list(coord_dict.keys())[list(coord_dict.values()).index('0')]

coord_dict.update({start: seen})

steps = 0

coord_dict_temp = coord_dict.copy()

while any(char not in [wall, passage, seen] for char in list(coord_dict.values())):
    target_found = False
    new_start = ''

    for coord in coord_dict:
        if coord_dict[coord] == seen:
            coord_dict_temp, target_found, new_start = check_neighbor(coord, coord_dict_temp, target_found, new_start)

    coord_dict = coord_dict_temp.copy()

    if target_found:
        for coord in coord_dict:
            if coord_dict[coord] == seen:
                coord_dict.update({coord: passage})
        coord_dict.update({new_start: seen})

    coord_dict_temp = coord_dict.copy()

    steps += 1

print('Part 1 Answer:', steps)

# Part 2

def check_neighbor_2(coord, end, coord_dict_temp, end_found):
    x = coord[0]
    y = coord[1]
    left = (x - 1, y)
    right = (x + 1, y)
    up = (x, y + 1)
    down = (x, y - 1)
    directions = [left, right, up, down]
    for direction in directions:
        if coord_dict_temp[direction] not in [wall, seen]:
            if coord_dict_temp[direction] == end:
                end_found = True
            else:
                coord_dict_temp.update({direction: seen})

    return end_found, coord_dict_temp

def bfs_search(start_point, end_point, coord_dict, number_dict):
    start_coord = number_dict[start_point]
    coord_dict_temp = coord_dict.copy()
    end_found = False
    distance = -1
    coord_dict_temp.update({start_coord: seen})
    while not end_found:
        for coord in coord_dict:
            if coord_dict[coord] == seen:
                end_found, coord_dict_temp = check_neighbor_2(coord, end_point, coord_dict_temp, end_found)
        distance += 1
        coord_dict = coord_dict_temp.copy()

    return distance

coord_dict_master = {}
number_dict = {}

y = 0

for y in range(len(input_text)):
    line = input_text[y]
    for x in range(len(line)):
        char = input_text[y][x]
        coord_dict_master.update({(x, y): char})
        if char not in [wall, seen, passage]:
            number_dict.update({char: (x, y)})

start = '0'
start_coord = number_dict[start]
end = '0'

number_dict_middle = number_dict.copy()
number_dict_middle.pop(start)

order_list_middle = list(itertools.permutations(number_dict_middle.keys()))

order_list = []

for order in order_list_middle:
    start_tuple = (start,)
    end_tuple = (end,)
    order = start_tuple + order + end_tuple
    # order = start_tuple + order
    order_list.append(order)

number_dict.update({end: number_dict[start]})

combos = itertools.combinations(number_dict.keys(), 2)

coord_dict = coord_dict_master.copy()

distance_dict = {}

for combo in combos:
    start_point = combo[0]
    end_point = combo[1]

    distance = bfs_search(start_point, end_point, coord_dict, number_dict)
    distance_dict.update({(start_point, end_point): distance})
    distance_dict.update({(end_point, start_point): distance})

min_steps = math.inf

for order in order_list:
    path_steps = 0
    for i in range(len(order) - 1):
        start_point = order[i]
        end_point = order[i + 1]

        distance = distance_dict[(start_point, end_point)]

        path_steps += distance

    if path_steps < min_steps:
        min_steps = path_steps

print('Part 2 Answer:', min_steps)
