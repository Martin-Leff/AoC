import requests
import itertools
import math

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_17_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

containers = list(map(int, input_text))
total_sum = 0

for length in range(len(containers)):
    for comb in itertools.combinations(containers, length + 1):
        if sum(comb) == 150:
            total_sum += 1

print('Part 1 Answer:', total_sum)

# Part 2

inf = math.inf
min_length = inf
total_sum = 0

for length in range(len(containers)):

    for comb in itertools.combinations(containers, length + 1):
        if (sum(comb) == 150) and (length <= min_length):
            min_length = length
            total_sum += 1

print('Part 2 Answer:', total_sum)
