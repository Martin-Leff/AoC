import requests
from itertools import combinations

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_5_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

i = 0

maze_dict = {}

for element in input_text:
    element = int(element)
    maze_dict.update({i: element})
    i += 1

start = 0
current = start

escaped = False
steps = 0

while not escaped:
    jump = maze_dict[current]
    maze_dict.update({current: jump + 1})
    current = current + jump
    steps += 1
    if current not in maze_dict:
        escaped = True

print('Part 1 Answer:', steps)

# Part 2

i = 0

maze_dict = {}

for element in input_text:
    element = int(element)
    maze_dict.update({i: element})
    i += 1

start = 0
current = start

escaped = False
steps = 0

while not escaped:
    jump = maze_dict[current]
    if jump >= 3:
        maze_dict.update({current: jump - 1})
    else:
        maze_dict.update({current: jump + 1})
    current = current + jump
    steps += 1
    if current not in maze_dict:
        escaped = True

print('Part 2 Answer:', steps)