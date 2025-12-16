import numpy as np
import requests
import regex as re

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_8_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

width = 50
height = 6

screen = np.zeros(shape=(height, width))

for line in input_text:
    if line.startswith('rect'):
        x, y = line.split()[1].split('x')
        y, x = int(x), int(y)
        screen[:x, :y] = 1
    elif line.startswith('rotate row'):
        row = int(line.split()[2].split('=')[1])
        offset = int(line.split()[4])
        screen[row] = np.roll(screen[row], offset)
    else:
        column = int(line.split()[2].split('=')[1])
        offset = int(line.split()[4])
        screen[:, column] = np.roll(screen[:, column], offset)

total_count = sum(sum(screen))

print('Part 1 Answer:', total_count)

# Part 2

# line_end = True

print_quest = False

if print_quest:
    for row in screen:
        for char in row:
            if char:
                print('#', end='')
            else:
                print(' ', end='')
        print('\n')

password = 'upojflbcez'

print('Part 2 Answer:', password)