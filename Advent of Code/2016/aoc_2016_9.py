import requests
import regex as re

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_9_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

def decompose_string(string):
    i = 0
    total = 0
    while i < len(string):
        if string[i] == '(':
            i += 1
            sub_string = ''
            while string[i] != ')':
                sub_string += string[i]
                i += 1
            length = int(sub_string.split('x')[0])
            repeat = int(sub_string.split('x')[1])
            length_add = length * repeat
            total += length_add
            i += length
        else:
            total += 1
        i += 1
    return total


total_total = decompose_string(input_text)

print('Part 1 Answer:', total_total)

# Part 2

def decompose_string2(string):
    i = 0
    total = 0
    while i < len(string):
        if string[i] == '(':
            i += 1
            sub_string = ''
            while string[i] != ')':
                sub_string += string[i]
                i += 1
            length = int(sub_string.split('x')[0])
            repeat = int(sub_string.split('x')[1])
            total += repeat * decompose_string2(string[i + 1:i + length + 1])
            i += length
        else:
            total += 1
        i += 1
    return total

total_total = decompose_string2(input_text)

print('Part 2 Answer:', total_total)
