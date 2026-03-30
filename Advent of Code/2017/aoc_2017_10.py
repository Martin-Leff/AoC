import requests
from functools import reduce
from operator import xor

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_10_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

cur_pos = 0
num_list = list(range(0,256))
list_len = len(num_list)
splits = input_text.split(',')
skip = 0

for split in splits:
    segment = int(split)
    num_list = num_list[cur_pos:] + num_list[:cur_pos]
    rev_section = num_list[0:segment][::-1]
    num_list = rev_section + num_list[segment::]
    num_list = num_list[list_len - cur_pos:] + num_list[:list_len - cur_pos]
    cur_pos = (segment + skip + cur_pos) % list_len
    skip += 1

product = num_list[0] * num_list[1]

print('Part 1 Answer:', product)

# Part 2

round_count = 64
extra = [17, 31, 73, 47, 23]

segments = []

for char in input_text:
    ascii_char = ord(char)
    segments.append(ascii_char)

segments = segments + extra

cur_pos = 0
num_list = list(range(0,256))
list_len = len(num_list)
skip = 0
bit_length = 16
number_of_bits = list_len / bit_length

while round_count > 0:
    for segment in segments:
        num_list = num_list[cur_pos:] + num_list[:cur_pos]
        rev_section = num_list[0:segment][::-1]
        num_list = rev_section + num_list[segment::]
        num_list = num_list[list_len - cur_pos:] + num_list[:list_len - cur_pos]
        cur_pos = (segment + skip + cur_pos) % list_len
        skip += 1
    round_count -= 1

bit_count = 0

dense_hash = []

while bit_count < number_of_bits:
    bit_slice = num_list[bit_length * bit_count:bit_length * (bit_count + 1)]
    res = reduce(xor, bit_slice)
    dense_hash.append(res)
    bit_count += 1

knot_hash = ''

for number in dense_hash:
    hex_num = hex(number).split('x')[1]
    while len(hex_num) < 2:
        hex_num = '0' + hex_num
    knot_hash += hex_num

print('Part 2 Answer:', knot_hash)