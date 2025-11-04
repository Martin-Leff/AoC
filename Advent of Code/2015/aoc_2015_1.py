import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_1_input.txt'
resp = requests.get(url)
input_text = resp.text


# Part 1
f = 0

for char in input_text:
    if char == '(':
        f += 1
    else:
        f -= 1

print('Part 1 Answer:', f)

# Part 2
f = 0
i = 0

for char in input_text:
    if char == '(':
        f += 1
    else:
        f -= 1
    i += 1
    if f < 0:
        break

print('Part 2 Answer:', i)
