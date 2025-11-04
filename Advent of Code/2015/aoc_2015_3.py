import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_3_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

def next_house(char):
    if char == '^':
        y_next = 1
        x_next = 0
    elif char == '>':
        y_next = 0
        x_next = 1
    elif char == 'v':
        y_next = -1
        x_next = 0
    else:
        y_next = 0
        x_next = -1
    return x_next, y_next

coord_list = []
x = 0
y = 0
coord_list.append((x, y))

for char in input_text:
    x_next, y_next = next_house(char)
    x += x_next
    y += y_next
    coord_list.append((x, y))

total = len(set(coord_list))
print('Part 1 Answer:', total)

# Part 2:

i = 0
santa_list = []
r_santa_list = []

coord_list = []
x = 0
y = 0
coord_list.append((x, y))

for char in input_text:
    i += 1
    if i % 2:
        santa_list.append(char)
    else:
        r_santa_list.append(char)

for char in santa_list:
    x_next, y_next = next_house(char)
    x += x_next
    y += y_next
    coord_list.append((x, y))

x = 0
y = 0

for char in r_santa_list:
    x_next, y_next = next_house(char)
    x += x_next
    y += y_next
    coord_list.append((x, y))

total = len(set(coord_list))
print('Part 2 Answer:', total)