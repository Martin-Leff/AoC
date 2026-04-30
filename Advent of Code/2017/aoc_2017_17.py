from collections import deque
import requests
from functools import reduce
from operator import xor

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_17_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

buffer = [0]
last_val = 2017
step_count = int(input_text)
start_point = 0

for i in range(last_val):
    i = i + 1
    buffer_length = len(buffer)
    offset = (step_count + start_point) % buffer_length
    start_point = offset + 1
    buffer.insert(start_point, i)

last_index = buffer.index(last_val)

next_index = last_index + 1
next_val = buffer[next_index]

print('Part 1 Answer:', next_val)

# Part 2

last_val = 50000000
buffer = deque([0])
step_count = int(input_text)
start_point = 0

for i in range(last_val):
    i = i + 1
    buffer.rotate(-step_count)
    buffer.append(i)

zero_index = buffer.index(0)

next_index = zero_index + 1
next_val = buffer[next_index]

print('Part 2 Answer:', next_val)