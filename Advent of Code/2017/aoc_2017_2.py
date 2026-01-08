import requests
from itertools import combinations

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_2_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

total = 0
spreadsheet = []

for line in input_text:
    line = line.split('\t')
    new_line = []
    for char in line:
        number = int(char)
        new_line.append(number)
    spreadsheet.append(new_line)

for row in spreadsheet:
    max_num = max(row)
    min_num = min(row)
    diff = max_num - min_num
    total += diff

print('Part 1 Answer:', total)

total = 0

for row in spreadsheet:
    unfound = True
    combos = combinations(row, 2)

    while unfound:
        for combo in combos:
            modulo_1 = combo[0] % combo[1]
            modulo_2 = combo[1] % combo[0]
            if modulo_1 == 0:
                total += combo[0] / combo[1]
                unfound = False
            if modulo_2 == 0:
                total += combo[1] / combo[0]
                unfound = False

print('Part 2 Answer:', total)