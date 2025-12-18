import requests
import regex as re
import collections
from collections import deque, Counter
from itertools import chain, combinations

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_13_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

def is_valid(x, y, offset):
    valid = False
    val = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + offset
    bin_val = format(val, 'b')
    even_odd = bin_val.count('1')
    if even_odd % 2 == 0:
        valid = True
    return valid

offset = int(input_text)
end_coord = (31, 39)

seen = {(1, 1)}
steps = 0
new = seen
keep_looking = True

while keep_looking == True:
    check_here = new.copy()
    new = set()
    for old_x, old_y in check_here:
        for new_x, new_y in [(old_x, old_y + 1), (old_x, old_y - 1), (old_x + 1, old_y), (old_x - 1, old_y)]:
            if (new_x, new_y) in seen or not is_valid(new_x, new_y, offset) or new_x < 0 or new_y < 0:
                continue
            seen.add((new_x, new_y))
            new.add((new_x, new_y))
    steps += 1

    if end_coord in seen:
        keep_looking = False

print('Part 1 Answer:', steps)

# Part 2

seen = {(1, 1)}
steps = 0
new = seen
keep_looking = True

while keep_looking == True:
    check_here = new.copy()
    new = set()
    for old_x, old_y in check_here:
        for new_x, new_y in [(old_x, old_y + 1), (old_x, old_y - 1), (old_x + 1, old_y), (old_x - 1, old_y)]:
            if (new_x, new_y) in seen or not is_valid(new_x, new_y, offset) or new_x < 0 or new_y < 0:
                continue
            seen.add((new_x, new_y))
            new.add((new_x, new_y))
    steps += 1

    if steps == 50:
        keep_looking = False

locations = len(seen)

print('Part 2 Answer:', locations)