import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_8_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

reg_dict = {}

for line in input_text:

    split_line = line.split(' ')

    reg = split_line[0]
    op = split_line[1]
    amount = int(split_line[2])
    cond_reg = split_line[4]
    cond_op = split_line[5]
    cond_amount = int(split_line[6])
    reg_val = 0
    cond_val = 0

    if reg not in reg_dict:
        reg_dict.update({reg: reg_val})
    else:
        reg_val = reg_dict[reg]

    if cond_reg not in reg_dict:
        reg_dict.update({cond_reg: cond_val})
    else:
        cond_val = reg_dict[cond_reg]

    if cond_op == '<' and cond_val < cond_amount:
        valid = True

    elif cond_op == '>' and cond_val > cond_amount:
        valid = True

    elif cond_op == '<=' and cond_val <= cond_amount:
        valid = True

    elif cond_op == '>=' and cond_val >= cond_amount:
        valid = True

    elif cond_op == '==' and cond_val == cond_amount:
        valid = True

    elif cond_op == '!=' and cond_val != cond_amount:
        valid = True

    else:
        valid = False

    if valid:
        if op == 'inc':
            new_val = reg_val + amount
        else:
            new_val = reg_val - amount

        reg_dict.update({reg: new_val})

max_val = reg_dict[max(reg_dict, key=reg_dict.get)]

print('Part 1 Answer:', max_val)

# Part 2

reg_dict = {}

max_ever = 0

for line in input_text:

    split_line = line.split(' ')

    reg = split_line[0]
    op = split_line[1]
    amount = int(split_line[2])
    cond_reg = split_line[4]
    cond_op = split_line[5]
    cond_amount = int(split_line[6])
    reg_val = 0
    cond_val = 0

    if reg not in reg_dict:
        reg_dict.update({reg: reg_val})
    else:
        reg_val = reg_dict[reg]

    if cond_reg not in reg_dict:
        reg_dict.update({cond_reg: cond_val})
    else:
        cond_val = reg_dict[cond_reg]

    if cond_op == '<' and cond_val < cond_amount:
        valid = True

    elif cond_op == '>' and cond_val > cond_amount:
        valid = True

    elif cond_op == '<=' and cond_val <= cond_amount:
        valid = True

    elif cond_op == '>=' and cond_val >= cond_amount:
        valid = True

    elif cond_op == '==' and cond_val == cond_amount:
        valid = True

    elif cond_op == '!=' and cond_val != cond_amount:
        valid = True

    else:
        valid = False

    if valid:
        if op == 'inc':
            new_val = reg_val + amount
        else:
            new_val = reg_val - amount

        reg_dict.update({reg: new_val})

        if new_val > max_ever:
            max_ever = new_val

print('Part 2 Answer:', max_ever)

