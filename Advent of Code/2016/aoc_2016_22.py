import requests
from itertools import combinations
import re
import os

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_22_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

size_dict = {}
used_dict = {}
avail_dict = {}
coord_list = []

for line in input_text:
    if line.startswith('/dev'):
        x = int(line.split(' ')[0].split('-')[1].strip('x'))
        y = int(line.split(' ')[0].split('-')[2].strip('y'))
        coord_list.append((x, y))

        line_split = line.split('   ')
        if len(line_split) == 5:
            size = int(line.split('   ')[1].strip(' ').strip('T'))
            used = int(line.split('   ')[2].strip(' ').strip('T'))
            avail = int(line.split('   ')[3].strip(' ').strip('T'))
        elif len(line_split) == 3:
            size = int(line_split[0].split('  ')[1].strip(' ').strip('T'))
            used = int(line_split[0].split('  ')[2].strip(' ').strip('T'))
            avail = int(line_split[1].strip(' ').strip('T'))
        else:
            size = int(line_split[1].split('  ')[0].strip(' ').strip('T'))
            used = int(line_split[1].split('  ')[1].strip(' ').strip('T'))
            avail = int(line_split[2].strip(' ').strip('T'))

        size_dict.update({(x, y): size})
        used_dict.update({(x, y): used})
        avail_dict.update({(x, y): avail})

viable_list = []

idx = 0
combo_list = combinations(coord_list, 2)
for combo in list(combo_list):
    combo_1 = combo[0]
    combo_2 = combo[1]

    if 0 < used_dict[combo_1] <= avail_dict[combo_2] or 0 < used_dict[combo_2] <= avail_dict[combo_1]:
        viable_list.append(combo)

viable_count = len(viable_list)

print('Part 1 Answer:', viable_count)

# Part 2

x_max = 0
y_max = 0

for line in input_text:
    if line.startswith('/dev'):
        x = int(line.split(' ')[0].split('-')[1].strip('x'))
        if x > x_max:
            x_max = x
        y = int(line.split(' ')[0].split('-')[2].strip('y'))
        if y > y_max:
            y_max = x

start = (0, 0)
goal = (x_max - 1, 0)

def print_map(y_max, x_max, goal, start, used_dict):
    for y in range(y_max):
        for x in range(x_max):
            if (x, y) == goal:
                c = '{'
            elif (x, y) == start:
                c = '['
            elif used_dict[(x, y)] == 0:
                c = '_'
            else:
                c = '.' if used_dict[(x, y)] < 100 else '#'
            if x == x_max - 1:
                print(c, '\n', end='')
            else:
                print(c, end='')

# print_map(y_max, x_max, goal, start, used_dict)
# Counting steps provides a step count of 230

print('Part 2 Answer:', 230)
