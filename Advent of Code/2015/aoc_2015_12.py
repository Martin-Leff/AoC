import requests
import re
import json

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_12_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

numbers = re.compile(r'-?\d+')
result = list(map(int, numbers.findall(input_text)))
total = sum(result)

print('Part 1 Answer:', total)

# Part 2

input_json = json.loads(input_text)

def expand(val):
    if type(val) == int:
        return val
    if type(val) == list:
        return sum([expand(val) for val in val])
    if type(val) != dict:
        return 0
    if 'red' in val.values():
        return 0
    return expand(list(val.values()))

total = expand(input_json)

print('Part 2 Answer:', total)