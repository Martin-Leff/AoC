import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_18_input.txt'

resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def check_neighbors(grid, x, y, on_val, off_val):
    count = 0
    current = grid[x, y]

    key_list = [
        (x - 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
    ]

    for key in key_list:
        if key in grid.keys():
            val = grid[key]
            if val == on_val:
                count += 1

    if (current == on_val) and (2 <= count <= 3):
        new_val = on_val
    elif (current == on_val) and not (2 <= count <= 3):
        new_val = off_val
    elif (current == off_val) and count == 3:
        new_val = on_val
    else:
        new_val = off_val

    return new_val

def grid_iteration(old_grid, on_val, off_val):
    new_grid = {}
    for key in old_grid:
        new_grid.update({key: check_neighbors(grid, key[0], key[1], on_val, off_val)})
    return new_grid

steps = 100
on_val = '#'
off_val = '.'

i = 1
grid = {}

for line in input_text:
    j = 1
    for char in line:
        grid.update({(i, j): char})
        j += 1
    i += 1

for step in range(steps):
    grid = grid_iteration(grid, on_val, off_val)

count = 0

for key in grid.keys():
    if grid[key] == on_val:
        count += 1

print('Part 1 Answer:', count)

# Part 2

width = 100
length = 100
i = 1
grid = {}

for line in input_text:
    j = 1
    for char in line:
        if (i == width and j == length) or (i == 1 and j == length) or (i == 1 and j == 1) or (i == width and j == 1):
            char = '#'
        grid.update({(i, j): char})
        j += 1
    i += 1

def grid_iteration_2(old_grid, on_val, off_val, width, length):
    new_grid = {}
    for key in old_grid:
        if (key == (width, length)) or (key == (1, length)) or (key == (width, 1)) or (key == (1, 1)):
            new_grid.update({key: on_val})
        else:
            new_grid.update({key: check_neighbors(grid, key[0], key[1], on_val, off_val)})
    return new_grid

for step in range(steps):
    grid = grid_iteration_2(grid, on_val, off_val, width, length)

count = 0

for key in grid.keys():
    if grid[key] == on_val:
        count += 1

print('Part 2 Answer:', count)