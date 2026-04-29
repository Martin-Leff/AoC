import requests
from functools import reduce
from operator import xor

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_16_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

def spin(string, position):
    string_len = len(string)
    end_pos = string_len - position
    new_string = string[end_pos:] + string[:end_pos]
    return new_string

def exchange(string, position_1, position_2):
    first = min(position_1, position_2)
    second = max(position_1, position_2)
    if first == second:
        return string
    new_string = string[:first] + string[second] + string[first + 1:second] + string[first] + string[second + 1:]
    return new_string

def partner(string, character_1, character_2):
    position_1 = string.find(character_1)
    position_2 = string.find(character_2)
    return exchange(string, position_1, position_2)

moves = input_text.split(',')

long_string = 'abcdefghijklmnop'

for move in moves:
    if move[0] == 's':
        position = int(move.strip('s'))
        long_string = spin(long_string, position)
    elif move[0] == 'x':
        pos_1 = int(move.strip('x').split('/')[0])
        pos_2 = int(move.strip('x').split('/')[1])
        long_string = exchange(long_string, pos_1, pos_2)
    else:
        char_1 = move[1]
        char_2 = move[3]
        long_string = partner(long_string, char_1, char_2)

print('Part 1 Answer:', long_string)

# Part 2

long_string = 'abcdefghijklmnop'

dance_count = 1000000000
cycle_count = 0

for _ in range(dance_count):
    if long_string == 'abcdefghijklmnop' and _ > 0:
        cycle_count = _
        break
    for move in moves:
        if move[0] == 's':
            position = int(move.strip('s'))
            long_string = spin(long_string, position)
        elif move[0] == 'x':
            pos_1 = int(move.strip('x').split('/')[0])
            pos_2 = int(move.strip('x').split('/')[1])
            long_string = exchange(long_string, pos_1, pos_2)
        else:
            char_1 = move[1]
            char_2 = move[3]
            long_string = partner(long_string, char_1, char_2)

extra_cycles = dance_count % cycle_count

long_string = 'abcdefghijklmnop'

for _ in range(extra_cycles):
    for move in moves:
        if move[0] == 's':
            position = int(move.strip('s'))
            long_string = spin(long_string, position)
        elif move[0] == 'x':
            pos_1 = int(move.strip('x').split('/')[0])
            pos_2 = int(move.strip('x').split('/')[1])
            long_string = exchange(long_string, pos_1, pos_2)
        else:
            char_1 = move[1]
            char_2 = move[3]
            long_string = partner(long_string, char_1, char_2)

print('Part 2 Answer:', long_string)