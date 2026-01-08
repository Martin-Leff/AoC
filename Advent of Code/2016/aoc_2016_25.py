import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_25_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def output_check(output):
    match = True
    initial = 0
    char_check = initial
    for i in range(len(output)):
        if output[i] != char_check:
            match = False
            break
        if char_check == 1:
            char_check = 0
        else:
            char_check = 1

    return match


command_list = input_text

output_found = False

a_init = -1

while not output_found:
    i = 0
    a_init += 1
    a = a_init
    b = 0
    c = 0
    d = 0
    j = 0
    active = True
    out_list = []

    while active:
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

        elif instruct == 'out':
            reg = command[1]

            if reg == 'a':
                val = a
            elif reg == 'b':
                val = b
            elif reg == 'c':
                val = c
            elif reg == 'd':
                val = d
            else:
                val = int(reg)

            out_list.append(val)

        i += 1

        if i == len(command_list) - 1:
            j += 1
            if j > 0:
                active = False

        if i >= len(command_list):
            active = False

    output_found = output_check(out_list)

print('Part 1 Answer:', a_init)