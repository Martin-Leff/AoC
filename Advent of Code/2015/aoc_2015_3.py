import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_3_input.txt'
resp = requests.get(url)
input_text = resp.text

print(input_text)