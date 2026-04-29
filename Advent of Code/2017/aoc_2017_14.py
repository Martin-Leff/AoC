import requests
from functools import reduce
from operator import xor

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_14_input.txt'
resp = requests.get(url)
input_text = resp.text


# Part 1

def knot_hash_calc(string):
    round_count = 64
    extra = [17, 31, 73, 47, 23]

    segments = []

    for character in string:
        ascii_char = ord(character)
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

    knot_hash_string = ''

    for number in dense_hash:
        hex_num = hex(number).split('x')[1]
        while len(hex_num) < 2:
            hex_num = '0' + hex_num
        knot_hash_string += hex_num

    return knot_hash_string

max_rows = 127

disk = []

for i in range(max_rows + 1):
    row_string = input_text + '-' + str(i)
    row_knot_hash = knot_hash_calc(row_string)
    row_binary = ''
    for char in row_knot_hash:
        bin_padded = f"{int(char, 16):04b}"
        row_binary = row_binary + bin_padded
    disk.append(row_binary)

used_count = 0

for row in disk:
    for char in row:
        if char == '1':
            used_count += 1

print('Part 1 Answer:', used_count)


# Part 2

def search_algo(x, y, max_dimension):
    if (x, y) in seen:
        return
    seen.add((x, y))
    if disk_dict[(x, y)] == '0':
        return
    if x > 0:
        search_algo(x - 1, y, max_dimension)
    if y > 0:
        search_algo(x, y - 1, max_dimension)
    if x < max_dimension:
        search_algo(x + 1, y, max_dimension)
    if y < max_dimension:
        search_algo(x, y + 1, max_dimension)

disk_dict = {}

for i in range(len(disk)):
    row = disk[i]
    for j in range(len(row)):
        char = row[j]
        disk_dict.update({(i, j): char})

zone_count = 0
seen = set()
max_dim = 127

for i in range(max_dim + 1):
    for j in range(max_dim + 1):
        if (i, j) in seen:
            continue
        if disk_dict[(i, j)] == '0':
            continue
        zone_count += 1
        search_algo(i, j, max_dim)

print('Part 2 Answer:', zone_count)

