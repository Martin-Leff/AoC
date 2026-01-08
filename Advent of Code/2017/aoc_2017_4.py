import requests
from itertools import combinations

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_4_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

print('Part 1 Answer:', input_text)