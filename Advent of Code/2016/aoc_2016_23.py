import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_23_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def toggle(command_list, i, n):
    target_index = i + n
    old_command = ''
    if 0 <= target_index < len(command_list):
        old_command = command_list[target_index]
    if old_command:
        command = old_command.split(' ')
        instruct = command[0]
        new_command = ''
        if instruct == 'inc':
            new_command = old_command.replace('inc', 'dec')
        elif instruct == 'tgl':
            new_command = old_command.replace('tgl', 'inc')
        elif instruct == 'dec':
            new_command = old_command.replace('dec', 'inc')
        elif instruct == 'jnz':
            new_command = old_command.replace('jnz', 'cpy')
        elif instruct == 'cpy':
            new_command = old_command.replace('cpy', 'jnz')
        else:
            print('ERROR ERROR')
        new_command_list = command_list[:target_index] + [new_command] + command_list[(target_index + 1):]

    else:
        new_command_list = command_list

    return new_command_list


command_list = input_text

i = 0
a = 7
b = 0
c = 0
d = 0

while True:
    command = command_list[i].split(' ')
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
        if command[2] == 'a':
            val = a
        elif command[2] == 'b':
            val = b
        elif command[2] == 'c':
            val = c
        elif command[2] == 'd':
            val = d
        else:
            val = int(command[2])
        if register != 0:
            i += val - 1

    elif instruct == 'tgl':
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
        command_list = toggle(command_list, i, val)

    i += 1
    if i >= len(command_list):
        break

print('Part 1 Answer:', a)

# Part 2

command_list = input_text

i = 0
a = 12
b = 0
c = 0
d = 0

while True:
    command = command_list[i].split(' ')
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
        if command[2] == 'a':
            val = a
        elif command[2] == 'b':
            val = b
        elif command[2] == 'c':
            val = c
        elif command[2] == 'd':
            val = d
        else:
            val = int(command[2])
        if register != 0:
            i += val - 1

    elif instruct == 'tgl':
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
        command_list = toggle(command_list, i, val)

    i += 1
    if i >= len(command_list):
        break

print('Part 2 Answer:', a)
