import requests
import re
from itertools import permutations
import math

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_9_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

distance_dict = dict()
city_list = []

for string in input_text:
    o, d, distance = re.split('to | =', string)
    o = o.strip(' ')
    d = d.strip(' ')
    distance = int(distance.strip(' '))
    distance_dict[(o, d)] = distance
    distance_dict[(d, o)] = distance
    if o not in city_list:
        city_list.append(o)
    if d not in city_list:
        city_list.append(d)

city_perm_list = list(permutations(city_list))

min_distance = math.inf

for perm in city_perm_list:
    perm_list = list(perm)
    perm_distance = 0
    for i in range(len(perm_list) - 1):
        start = perm_list[i]
        end = perm_list[i + 1]
        current_dist = distance_dict[(start, end)]
        perm_distance += current_dist

    if perm_distance < min_distance:
        min_distance = perm_distance

print('Part 1 Answer:', min_distance)

# Part 2

max_distance = 0

for perm in city_perm_list:
    perm_list = list(perm)
    perm_distance = 0
    for i in range(len(perm_list) - 1):
        start = perm_list[i]
        end = perm_list[i + 1]
        current_dist = distance_dict[(start, end)]
        perm_distance += current_dist

    if perm_distance > max_distance:
        max_distance = perm_distance

print('Part 2 Answer:', max_distance)