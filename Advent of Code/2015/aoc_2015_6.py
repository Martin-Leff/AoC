import requests
import re

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_6_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

print(input_text)

# Part 1

def toggle_func(coordx1, coordy1, coordx2, coordy2):
    return

def turn_on(coordx1, coordy1, coordx2, coordy2):
    return

def turn_off(coordx1, coordy1, coordx2, coordy2):
    return

def sort(string):
    toggle = 'toggle'
    on = 'turn on'
    off = 'turn off'

    nums = re.findall(r'\d+\.?\d*', string)
    x1, y1, x2, y2 = int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])

    if string.startswith(toggle):
        toggle_func(x1, y1, x2, y2)

d = dict()

for x in range(1000):
    for y in range(1000):
        d.update({(x, y): 0})

print(d)

for string in input_text:
    sort(string)