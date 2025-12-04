import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_2_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

x = 1
y = 1
code = ''

for line in input_text:
    for char in line:
        if char == 'U':
            y += 1
            if y > 2:
                y = 2
        elif char == 'D':
            y -= 1
            if y < 0:
                y = 0
        elif char == 'R':
            x += 1
            if x > 2:
                x = 2
        elif char == 'L':
            x -= 1
            if x < 0:
                x = 0

    if x == 0 and y == 2:
        code = code + '1'
    elif x == 1 and y == 2:
        code = code + '2'
    elif x == 2 and y == 2:
        code = code + '3'
    elif x == 0 and y == 1:
        code = code + '4'
    elif x == 1 and y == 1:
        code = code + '5'
    elif x == 2 and y == 1:
        code = code + '6'
    elif x == 0 and y == 0:
        code = code + '7'
    elif x == 1 and y == 0:
        code = code + '8'
    elif x == 2 and y == 0:
        code = code + '9'

print('Part 1 Answer:', code)

# Part 2

x = 0
y = 2
code = ''
naughty_list = [(2, -1), (1, 0), (0, 1), (-1, 2), (0, 3), (1, 4), (2, 5), (3, 4), (4, 3), (5, 2), (4, 1), (3, 0)]

for line in input_text:
    for char in line:
        if (char == 'U') and ((x, y + 1) not in naughty_list):
            y += 1
        elif (char == 'D') and ((x, y - 1) not in naughty_list):
            y -= 1
        elif (char == 'R') and ((x + 1, y) not in naughty_list):
            x += 1
        elif (char == 'L') and ((x - 1, y) not in naughty_list):
            x -= 1

    if x == 2 and y == 4:
        code = code + '1'
    elif x == 1 and y == 3:
        code = code + '2'
    elif x == 2 and y == 3:
        code = code + '3'
    elif x == 3 and y == 3:
        code = code + '4'
    elif x == 0 and y == 2:
        code = code + '5'
    elif x == 1 and y == 2:
        code = code + '6'
    elif x == 2 and y == 2:
        code = code + '7'
    elif x == 3 and y == 2:
        code = code + '8'
    elif x == 4 and y == 2:
        code = code + '9'
    elif x == 1 and y == 1:
        code = code + 'A'
    elif x == 2 and y == 1:
        code = code + 'B'
    elif x == 3 and y == 1:
        code = code + 'C'
    elif x == 2 and y == 0:
        code = code + 'D'

print('Part 2 Answer:', code)