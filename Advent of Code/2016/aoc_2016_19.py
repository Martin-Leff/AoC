import requests
import hashlib
import math

from fontTools.misc.cython import returns

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_19_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

print('Part 2 Answer:', input_text)