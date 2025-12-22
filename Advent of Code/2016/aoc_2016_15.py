import requests
import hashlib
from sys import setrecursionlimit
setrecursionlimit(10000)

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_15_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

key_dict = {}
att_dict = {}

for line in input_text:
    number = int(line.split(' ')[1].strip('#'))
    total_pos = int(line.split(' ')[3])
    start_pos = int(line.split(' ')[11].strip('.'))
    att_dict.update({number:{'total': total_pos, 'start': start_pos}})
    inline_pos = total_pos - number
    while inline_pos < 0:
        inline_pos += total_pos
    key_dict.update({number: inline_pos})

t = 0
answer_dict = {}

while answer_dict != key_dict:
    t += 1
    for disc in att_dict:
        total_pos = att_dict[disc]['total']
        cur_pos = (att_dict[disc]['start'] + t) % total_pos
        answer_dict.update({disc: cur_pos})

print('Part 1 Answer:', t)

# Part 2

part_2 = 'Disc #7 has 11 positions; at time=0, it is at position 0.'

part_2_input_text = input_text.append(part_2)


key_dict = {}
att_dict = {}

for line in input_text:
    number = int(line.split(' ')[1].strip('#'))
    total_pos = int(line.split(' ')[3])
    start_pos = int(line.split(' ')[11].strip('.'))
    att_dict.update({number:{'total': total_pos, 'start': start_pos}})
    inline_pos = total_pos - number
    while inline_pos < 0:
        inline_pos += total_pos

    key_dict.update({number: inline_pos})

t = 0
answer_dict = {}

while answer_dict != key_dict:
    t += 1
    for disc in att_dict:
        total_pos = att_dict[disc]['total']
        cur_pos = (att_dict[disc]['start'] + t) % total_pos
        answer_dict.update({disc: cur_pos})

print('Part 2 Answer:', t)