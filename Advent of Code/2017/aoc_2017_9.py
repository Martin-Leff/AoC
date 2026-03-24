import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_9_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

total_score = 0
cur_depth = 0
in_garbage = False
skip_char = False

for char in input_text:
    if not in_garbage:
        if char == '{':
            cur_depth += 1
        if char == '}':
            total_score += cur_depth
            cur_depth -= 1
        elif char == '<':
            in_garbage = True
    else:
        if skip_char:
            skip_char = False
        elif char == '!':
            skip_char = True
        elif char == '>':
            in_garbage = False

print('Part 1 Answer:', total_score)

# Part 2

garbage_score = 0
cur_depth = 0
in_garbage = False
skip_char = False

for char in input_text:
    if not in_garbage:
        if char == '{':
            cur_depth += 1
        if char == '}':
            cur_depth -= 1
        elif char == '<':
            in_garbage = True
    else:
        if skip_char:
            skip_char = False
        elif char == '!':
            skip_char = True
        elif char == '>':
            in_garbage = False
        else:
            garbage_score += 1

print('Part 2 Answer:', garbage_score)