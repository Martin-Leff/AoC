import requests
import sys

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_20_input.txt'
resp = requests.get(url)
input_text = resp.text
data = input_text
input_text = input_text.splitlines()

# Part 1

range_list = []

for line in input_text:
    start = int(line.split('-')[0])
    end = int(line.split('-')[1])
    range_list.append((start, end))

min_range = 0
max_range = 0
finished = False

while not finished:
    finished = True
    for ranges in range_list:
        if min_range >= ranges[0] >= max_range:
            min_range = ranges[0]
            max_range = ranges[1]
            finished = False
        if ranges[0] <= max_range < ranges[1]:
            max_range = ranges[1]
            finished = False

min_final = max_range + 1

print('Part 1 Answer:', min_final)

# Part 2

range_starts = []

for line in input_text:
    start = int(line.split('-')[0])
    range_starts.append(start)

max_val = 4294967295

valid = []
min_range = 0
max_range = 0

while max_range < max_val:
    finished = False

    while not finished:
        finished = True
        for ranges in range_list:
            if min_range >= ranges[0] >= max_range:
                min_range = ranges[0]
                max_range = ranges[1]
                finished = False
            if ranges[0] <= max_range < ranges[1]:
                max_range = ranges[1]
                finished = False
        if finished:
            valid_ip = max_range + 1
            if valid_ip < max_val and valid_ip not in range_starts:
                valid.append(valid_ip)
            min_range = valid_ip
            max_range = valid_ip

valid_ip_tot = len(valid)

print('Part 2 Answer:', valid_ip_tot)
