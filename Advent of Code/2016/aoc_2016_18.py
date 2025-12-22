import requests
import hashlib
import math

from fontTools.misc.cython import returns

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_18_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

def path_hex(string):
    return hashlib.md5(string.encode()).hexdigest()[:4]

def valid_dir(string, coord, valid_char):
    valid = []
    x = coord[0]
    y = coord[1]
    for i in range(len(string)):
        char = string[i]
        if char in valid_char:
            if y != -1 and i == 0:
                valid.append('U')
            if y != -4 and i == 1:
                valid.append('D')
            if x != 1 and i == 2:
                valid.append('L')
            if x != 4 and i == 3:
                valid.append('R')
    return valid


def current_loc_calc(path, start):
    start_x = start[0]
    start_y = start[1]
    U = path.count('U')
    D = path.count('D')
    L = path.count('L')
    R = path.count('R')

    y_change = U - D
    x_change = R - L

    return (start_x + x_change, start_y + y_change)


valid_char = 'bcdef'
end = (4, -4)
start = (1, -1)
inf = math.inf
shortest = inf
shortest_path = ''
path = ''
queue = [path]

while queue:
    path = queue.pop(0)
    current_loc = current_loc_calc(path, start)
    string = input_text + path
    next_hash = path_hex(string)
    valid_dirs = valid_dir(next_hash, current_loc, valid_char)
    for direction in valid_dirs:
        new_path = path + direction
        next_loc = current_loc_calc(new_path, start)
        if next_loc == end:
            if len(new_path) < shortest:
                shortest = len(new_path)
                shortest_path = new_path
        else:
            queue.append(new_path)

print('Part 1 Answer:', shortest_path)

# Part 2

longest = 0
path = ''
queue = [path]

while queue:
    path = queue.pop(0)
    current_loc = current_loc_calc(path, start)
    string = input_text + path
    next_hash = path_hex(string)
    valid_dirs = valid_dir(next_hash, current_loc, valid_char)
    for direction in valid_dirs:
        new_path = path + direction
        next_loc = current_loc_calc(new_path, start)
        if next_loc == end:
            if len(new_path) > longest:
                longest = len(new_path)
        else:
            queue.append(new_path)

print('Part 2 Answer:', longest)
