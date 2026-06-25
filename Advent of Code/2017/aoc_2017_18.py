import requests
from collections import deque

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_18_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

freq_name = ''
freq_list = {}
sound = ''
i = 0
program_length = len(input_text)

while i in range(program_length):
    command = input_text[i]
    instruct = command.split(' ')[0]

    if instruct == 'snd':
        freq_name = command.split(' ')[1]
        freq = freq_list[freq_name]
        if freq_name in freq_list:
            sound = freq

    elif instruct == 'set':
        reg_name = command.split(' ')[1]
        set_to_name = command.split(' ')[2]

        try:
            set_to_name = int(set_to_name)
            freq = set_to_name
        except ValueError:
            freq = freq_list[set_to_name]

        freq_list.update({reg_name: freq})

    elif instruct == 'add':
        reg_name = command.split(' ')[1]
        set_to_name = command.split(' ')[2]

        try:
            set_to_name = int(set_to_name)
            freq = set_to_name
        except ValueError:
            freq = freq_list[set_to_name]

        if reg_name in freq_list:
            cur_freq = freq_list[reg_name]
        else:
            cur_freq = 0

        freq_list.update({reg_name: cur_freq + freq})

    elif instruct == 'mul':
        reg_name = command.split(' ')[1]
        set_to_name = command.split(' ')[2]

        try:
            set_to_name = int(set_to_name)
            freq = set_to_name
        except ValueError:
            freq = freq_list[set_to_name]

        if reg_name in freq_list:
            cur_freq = freq_list[reg_name]
        else:
            cur_freq = 0

        freq_list.update({reg_name: cur_freq * freq})

    elif instruct == 'mod':
        reg_name = command.split(' ')[1]
        set_to_name = command.split(' ')[2]

        try:
            set_to_name = int(set_to_name)
            freq = set_to_name
        except ValueError:
            freq = freq_list[set_to_name]

        if reg_name in freq_list:
            cur_freq = freq_list[reg_name]
        else:
            cur_freq = 0

        freq_list.update({reg_name: cur_freq % freq})

    elif instruct == 'rcv':
        reg_name = command.split(' ')[1]

        if reg_name in freq_list:
            cur_freq = freq_list[reg_name]
        else:
            cur_freq = 0

        if cur_freq:
            break

    elif instruct == 'jgz':
        reg_name = command.split(' ')[1]
        offset_name = command.split(' ')[2]

        try:
            offset_name = int(offset_name)
            offset = offset_name
        except ValueError:
            offset = freq_list[offset_name]

        if reg_name in freq_list:
            cur_freq = freq_list[reg_name]
        else:
            cur_freq = 0

        if cur_freq > 0:
            i += offset
            i -= 1

    i += 1

print('Part 1 Answer:', sound)


# Part 2

def value(r, regs):
    if r.isalpha():
        return regs.get(r, 0)
    else:
        return int(r)

def program(regs, q_in, q_out):
    while (regs['counter'] >= 0 and regs['counter'] < len(commands)):
        parsed = commands[regs['counter']].strip().split(' ')
        command = parsed[0]
        val = parsed[1]

        if command == 'rcv':
            if len(q_in) == 0:
                return True
            regs[val] = q_in.popleft()
        if command == 'jgz':
            if value(val, regs) > 0:
                regs['counter'] += value(parsed[2], regs)
                continue
        if command == 'snd':
            q_out.append(value(val, regs))
            regs['sent'] = value('sent', regs) + 1
        if command == 'set':
            regs[val] = value(parsed[2], regs)
        if command == 'add':
            regs[val] = value(val, regs) + value(parsed[2], regs)
        if command == 'mul':
            regs[val] = value(val, regs) * value(parsed[2], regs)
        if command == 'mod':
            regs[val] = value(val, regs) % value(parsed[2], regs)

        regs['counter'] += 1
    return

# input_text = ['snd 1', 'snd 2', 'snd p', 'rcv a', 'rcv b', 'rcv c', 'rcv d']

program_length = len(input_text)

reg_0 = {'p': 0, 'counter': 0}
reg_1 = {'p': 1, 'counter': 0}

q_for_0 = deque()
q_for_1 = deque()

commands = input_text

program(reg_0, q_for_0, q_for_1)

while True:
    if not program(reg_0, q_for_0, q_for_1): break
    if not program(reg_1, q_for_1, q_for_0): break
    if len(q_for_0) == 0 and len(q_for_1) == 0: break

count = reg_1['sent']

print('Part 2 Answer:', count)
