import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_12_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text.splitlines()

# Part 1

print('Part 2 Answer:', input_text)
