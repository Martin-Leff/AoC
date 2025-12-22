import requests
import hashlib
from sys import setrecursionlimit
setrecursionlimit(10000)

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_15_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1


print('Part 2 Answer:', input_text)
