import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_23_input.txt'

resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

i = 0
a = 0
b = 0

while True:
    command = input_text[i].split(' ')
    instruct = command[0]

    if instruct == 'tpl':
        reg = command[1]
        if reg == 'a':
            a = a * 3
        else:
            b = b * 3

    elif instruct == 'hlf':
        reg = command[1]
        if reg == 'a':
            a = a / 2
        else:
            b = b / 2

    elif instruct == 'jmp':
        inc = int(command[1]) -1
        i += inc

    elif instruct == 'jie':
        reg = command[1].strip(',')
        inc = int(command[2]) - 1
        if (reg == 'a') and (a % 2 == 0):
            i += inc
        elif (reg == 'b') and (b % 2 == 0):
            i += inc

    elif instruct == 'jio':
        reg = command[1].strip(',')
        inc = int(command[2]) - 1
        if (reg == 'a') and (a == 1):
            i += inc
        elif (reg == 'b') and (b == 1):
            i += inc

    elif instruct == 'inc':
        reg = command[1]
        if reg == 'a':
            a += 1
        else:
            b += 1

    i += 1
    if i >= len(input_text):
        break

print('Part 1 Answer:', b)

# Part 2

i = 0
a = 1
b = 0

while True:
    command = input_text[i].split(' ')
    instruct = command[0]

    if instruct == 'tpl':
        reg = command[1]
        if reg == 'a':
            a = a * 3
        else:
            b = b * 3

    elif instruct == 'hlf':
        reg = command[1]
        if reg == 'a':
            a = a / 2
        else:
            b = b / 2

    elif instruct == 'jmp':
        inc = int(command[1]) -1
        i += inc

    elif instruct == 'jie':
        reg = command[1].strip(',')
        inc = int(command[2]) - 1
        if (reg == 'a') and (a % 2 == 0):
            i += inc
        elif (reg == 'b') and (b % 2 == 0):
            i += inc

    elif instruct == 'jio':
        reg = command[1].strip(',')
        inc = int(command[2]) - 1
        if (reg == 'a') and (a == 1):
            i += inc
        elif (reg == 'b') and (b == 1):
            i += inc

    elif instruct == 'inc':
        reg = command[1]
        if reg == 'a':
            a += 1
        else:
            b += 1

    i += 1
    if i >= len(input_text):
        break

print('Part 2 Answer:', b)