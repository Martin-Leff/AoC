import requests
import re

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_12_input.txt'
resp = requests.get(url)
input_text = resp.text

print(input_text)

numbers = re.compile(r'-?\d+')
result = list(map(int, numbers.findall(input_text)))
print(result)
total = sum(result)

print(total)
