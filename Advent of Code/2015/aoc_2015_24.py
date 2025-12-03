import requests
from functools import reduce
from itertools import combinations
from operator import mul

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_24_input.txt'

resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def calc(num_of_groups):
    target_weight = sum(input_text) / num_of_groups
    for i in range(len(input_text)):
        quant_en = [reduce(mul, c) for c in combinations(input_text, i) if sum(c) == target_weight]
        if quant_en:
            return min(quant_en)

input_text = [int(s) for s in input_text]

num_of_groups = 3

qe_min = calc(3)

print('Part 1 Answer:', qe_min)

# Part 2

qe_min = calc(4)

print('Part 2 Answer:', qe_min)