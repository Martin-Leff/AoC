import requests
import regex as re
import collections

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_11_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

print('Part 1 Answer:', input_text)

floor_list = []

for line in input_text:
    f = []
    print(line)
    if 'thulium generator' in line:
        f.append(-1)
    if 'thulium-compatible microchip' in line:
        f.append(1)
    if 'plutonium generator' in line:
        f.append(-2)
    if 'plutonium-compatible microchip' in line:
        f.append(2)
    if 'strontium generator' in line:
        f.append(-3)
    if 'strontium-compatible microchip' in line:
        f.append(3)
    if 'promethium generator' in line:
        f.append(-4)
    if 'promethium-compatible microchip' in line:
        f.append(4)
    if 'ruthenium generator' in line:
        f.append(-5)
    if 'ruthenium-compatible microchip' in line:
        f.append(5)

    floor_list.append(f)

print(floor_list)
print(sum(floor_list, []))