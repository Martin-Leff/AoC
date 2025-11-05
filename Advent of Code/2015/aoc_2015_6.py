import requests
import re

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_6_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def toggle_func(coordx1, coordy1, coordx2, coordy2):
    for x in range(coordx1, coordx2):
        for y in range(coordy1, coordy2):
            if d[(x, y)] == 0:
                d.update({(x, y): 1})
            else:
                d.update({(x, y): 0})

def turn_on(coordx1, coordy1, coordx2, coordy2):
    for x in range(coordx1, coordx2):
        for y in range(coordy1, coordy2):
            d.update({(x, y): 1})


def turn_off(coordx1, coordy1, coordx2, coordy2):
    for x in range(coordx1, coordx2):
        for y in range(coordy1, coordy2):
            d.update({(x, y): 0})

def sort(string):
    toggle = 'toggle'
    on = 'turn on'
    off = 'turn off'

    nums = re.findall(r'\d+\.?\d*', string)
    x1, y1, x2, y2 = int(nums[0]), int(nums[1]), int(nums[2]) + 1, int(nums[3]) + 1

    if string.startswith(toggle):
        toggle_func(x1, y1, x2, y2)
    elif string.startswith(on):
        turn_on(x1, y1, x2, y2)
    elif string.startswith(off):
        turn_off(x1, y1, x2, y2)
    else:
        print(string)
        print('Error: Check String')

d = dict()

for x in range(1000):
    for y in range(1000):
        d.update({(x, y): 0})

for string in input_text:
    sort(string)

total = 0

for key in d:
    if d[key] == 1:
        total += 1

print('Part 1 Answer:', total)

# Part 2

def toggle_func_2(coordx1, coordy1, coordx2, coordy2):
    for x in range(coordx1, coordx2):
        for y in range(coordy1, coordy2):
            value = d[(x, y)]
            d.update({(x, y): value + 2})


def turn_on_2(coordx1, coordy1, coordx2, coordy2):
    for x in range(coordx1, coordx2):
        for y in range(coordy1, coordy2):
            value = d[(x, y)]
            d.update({(x, y): value + 1})


def turn_off_2(coordx1, coordy1, coordx2, coordy2):
    for x in range(coordx1, coordx2):
        for y in range(coordy1, coordy2):
            value = d[(x, y)]
            if value == 0:
                continue
            else:
                d.update({(x, y): value - 1})

def sort_2(string):
    toggle = 'toggle'
    on = 'turn on'
    off = 'turn off'

    nums = re.findall(r'\d+\.?\d*', string)
    x1, y1, x2, y2 = int(nums[0]), int(nums[1]), int(nums[2]) + 1, int(nums[3]) + 1

    if string.startswith(toggle):
        toggle_func_2(x1, y1, x2, y2)
    elif string.startswith(on):
        turn_on_2(x1, y1, x2, y2)
    elif string.startswith(off):
        turn_off_2(x1, y1, x2, y2)
    else:
        print(string)
        print('Error: Check String')

d = dict()

for x in range(1000):
    for y in range(1000):
        d.update({(x, y): 0})

for string in input_text:
    sort_2(string)

total = 0

for key in d:
    val = d[key]
    total += val

print('Part 2 Answer:', total)