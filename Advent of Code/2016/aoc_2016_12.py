import requests
import regex as re
import collections
from collections import deque, Counter
from itertools import chain, combinations

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_12_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

i = 0
a = 0
b = 0
c = 0
d = 0

while True:
    command = input_text[i].split(' ')
    instruct = command[0]

    if instruct == 'cpy':
        if command[1] == 'a':
            val = a
        elif command[1] == 'b':
            val = b
        elif command[1] == 'c':
            val = c
        elif command[1] == 'd':
            val = d
        else:
            val = int(command[1])

        reg = command[2]

        if reg == 'a':
            a = val
        elif reg == 'b':
            b = val
        elif reg == 'c':
            c = val
        else:
            d = val

    elif instruct == 'inc':
        reg = command[1]
        if reg == 'a':
            a += 1
        elif reg == 'b':
            b += 1
        elif reg == 'c':
            c += 1
        else:
            d += 1

    elif instruct == 'dec':
        reg = command[1]
        if reg == 'a':
            a -= 1
        elif reg == 'b':
            b -= 1
        elif reg == 'c':
            c -= 1
        else:
            d -= 1

    elif instruct == 'jnz':
        reg = command[1]
        if reg == 'a':
            register = a
        elif reg == 'b':
            register = b
        elif reg == 'c':
            register = c
        elif reg == 'd':
            register = d
        else:
            register = int(reg)
        val = int(command[2])
        if register != 0:
            i += val - 1

    i += 1
    if i >= len(input_text):
        break

print('Part 1 Answer:', a)

# Part 2

i = 0
a = 0
b = 0
c = 1
d = 0

while True:
    command = input_text[i].split(' ')
    instruct = command[0]

    if instruct == 'cpy':
        if command[1] == 'a':
            val = a
        elif command[1] == 'b':
            val = b
        elif command[1] == 'c':
            val = c
        elif command[1] == 'd':
            val = d
        else:
            val = int(command[1])

        reg = command[2]

        if reg == 'a':
            a = val
        elif reg == 'b':
            b = val
        elif reg == 'c':
            c = val
        else:
            d = val

    elif instruct == 'inc':
        reg = command[1]
        if reg == 'a':
            a += 1
        elif reg == 'b':
            b += 1
        elif reg == 'c':
            c += 1
        else:
            d += 1

    elif instruct == 'dec':
        reg = command[1]
        if reg == 'a':
            a -= 1
        elif reg == 'b':
            b -= 1
        elif reg == 'c':
            c -= 1
        else:
            d -= 1

    elif instruct == 'jnz':
        reg = command[1]
        if reg == 'a':
            register = a
        elif reg == 'b':
            register = b
        elif reg == 'c':
            register = c
        elif reg == 'd':
            register = d
        else:
            register = int(reg)
        val = int(command[2])
        if register != 0:
            i += val - 1

    i += 1
    if i >= len(input_text):
        break

print('Part 2 Answer:', a)