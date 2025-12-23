import requests
import hashlib
import math

from fontTools.misc.cython import returns

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_18_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

def is_trap(l, m, r, trap, safe):
    if ((l == trap and m == trap and r != trap)
            or (l != trap and m == trap and r == trap)
            or (l == trap and m != trap and r != trap)
            or (l != trap and m != trap and r == trap)):
        return trap
    else:
        return safe

trap = '^'
safe = '.'
max_rows = 40
cur_line = input_text
line_list = [cur_line]

for _ in range(max_rows - 1):
    next_line = ''
    for i in range(len(cur_line)):
        if i == 0:
            l_char = safe
            m_char = cur_line[i]
            r_char = cur_line[i + 1]
        elif i == len(cur_line) - 1:
            l_char = cur_line[i - 1]
            m_char = cur_line[i]
            r_char = safe
        else:
            l_char = cur_line[i - 1]
            m_char = cur_line[i]
            r_char = cur_line[i + 1]
        next_line += is_trap(l_char, m_char, r_char, trap, safe)
    line_list.append(next_line)
    cur_line = next_line

safe_count = 0

for line in line_list:
    safe_count += line.count(safe)

print('Part 1 Answer:', safe_count)

# Part 2

trap = '^'
safe = '.'
max_rows = 400000
cur_line = input_text
line_list = [cur_line]

for _ in range(max_rows - 1):
    next_line = ''
    for i in range(len(cur_line)):
        if i == 0:
            l_char = safe
            m_char = cur_line[i]
            r_char = cur_line[i + 1]
        elif i == len(cur_line) - 1:
            l_char = cur_line[i - 1]
            m_char = cur_line[i]
            r_char = safe
        else:
            l_char = cur_line[i - 1]
            m_char = cur_line[i]
            r_char = cur_line[i + 1]
        next_line += is_trap(l_char, m_char, r_char, trap, safe)
    line_list.append(next_line)
    cur_line = next_line

safe_count = 0

for line in line_list:
    safe_count += line.count(safe)

print('Part 2 Answer:', safe_count)