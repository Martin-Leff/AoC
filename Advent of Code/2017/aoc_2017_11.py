import requests
import math

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_11_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

moves = input_text.split(',')

x = 0
y = 0
z = 0


for move in moves:
    if move == 'n':
        z -= 1
        y += 1
    elif move == 's':
        z += 1
        y -= 1
    elif move == 'nw':
        x -= 1
        y += 1
    elif move == 'se':
        x += 1
        y -= 1
    elif move == 'ne':
        x += 1
        z -= 1
    else:
        x -= 1
        z += 1

distance = (abs(x) + abs(y) + abs(z)) / 2

print('Part 1 Answer:', distance)

# Part 2

x = 0
y = 0
z = 0

distance_list = []

for move in moves:
    if move == 'n':
        z -= 1
        y += 1
    elif move == 's':
        z += 1
        y -= 1
    elif move == 'nw':
        x -= 1
        y += 1
    elif move == 'se':
        x += 1
        y -= 1
    elif move == 'ne':
        x += 1
        z -= 1
    else:
        x -= 1
        z += 1

    distance = (abs(x) + abs(y) + abs(z)) / 2
    distance_list.append(distance)

max_distance = max(distance_list)

print('Part 2 Answer:', max_distance)
