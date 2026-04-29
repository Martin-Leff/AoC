import requests
from functools import reduce
from operator import xor

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_15_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

gen_dict = {}

for row in input_text:
    gen = row.split(' ')[1]
    gen_number = row.split(' ')[4]
    gen_dict.update({gen: gen_number})

gen_a_start = int(gen_dict['A'])

gen_b_start = int(gen_dict['B'])
gen_a_factor = 16807
gen_b_factor = 48271
divider = 2147483647
max_count = 40000000
comp_length = 16
count = 0

for _ in range(max_count):
    gen_a_new = (gen_a_start * gen_a_factor) % divider
    gen_b_new = (gen_b_start * gen_b_factor) % divider
    gen_a_start = gen_a_new
    gen_b_start = gen_b_new

    a_bin = '{:032b}'.format(gen_a_start)
    b_bin = '{:032b}'.format(gen_b_start)

    a_string = a_bin[-comp_length:]
    b_string = b_bin[-comp_length:]

    if a_string == b_string:
        count += 1

print('Part 1 Answer:', count)

# Part 2

gen_a_start = int(gen_dict['A'])
gen_b_start = int(gen_dict['B'])
gen_a_factor = 16807
gen_b_factor = 48271
gen_a_mult = 4
gen_b_mult = 8
divider = 2147483647
max_count = 5000000
comp_length = 16
count = 0

for _ in range(max_count):
    gen_a_new = (gen_a_start * gen_a_factor) % divider

    while gen_a_new % gen_a_mult != 0:
        gen_a_start = gen_a_new
        gen_a_new = (gen_a_start * gen_a_factor) % divider

    gen_b_new = (gen_b_start * gen_b_factor) % divider

    while gen_b_new % gen_b_mult != 0:
        gen_b_start = gen_b_new
        gen_b_new = (gen_b_start * gen_b_factor) % divider

    gen_a_start = gen_a_new
    gen_b_start = gen_b_new

    a_bin = '{:032b}'.format(gen_a_start)
    b_bin = '{:032b}'.format(gen_b_start)

    a_string = a_bin[-comp_length:]
    b_string = b_bin[-comp_length:]

    if a_string == b_string:
        count += 1

print('Part 2 Answer:', count)