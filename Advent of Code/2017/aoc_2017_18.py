import collections
import requests
from functools import reduce
from operator import xor
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

# def program(pid, rcv_queue, snd_queue, j):
#     r = collections.defaultdict(int)
#     r['p'] = pid
#
#     value = lambda v: r[v] if v.isalpha() else int(v)
#
#     i = 0
#
#     while i in range(program_length):
#         command = input_text[i]
#         instruct = command.split(' ')[0]
#
#         if instruct == 'snd':
#             freq_name = command.split(' ')[1]
#             snd_queue.append(value(freq_name))
#             yield 'send'
#
#         elif instruct == 'set':
#             reg_name = command.split(' ')[1]
#             set_to_name = value(command.split(' ')[2])
#
#             r[reg_name] = set_to_name
#
#         elif instruct == 'add':
#             reg_name = command.split(' ')[1]
#             set_to_name = value(command.split(' ')[2])
#
#             r[reg_name] += set_to_name
#
#         elif instruct == 'mul':
#             reg_name = command.split(' ')[1]
#             set_to_name = value(command.split(' ')[2])
#
#             r[reg_name] *= set_to_name
#
#         elif instruct == 'mod':
#             reg_name = command.split(' ')[1]
#             set_to_name = value(command.split(' ')[2])
#
#             r[reg_name] %= set_to_name
#
#         elif instruct == 'rcv':
#             while not rcv_queue:
#                 yield 'wait'
#             else:
#                 reg_name = command.split(' ')[1]
#                 r[reg_name] = rcv_queue.popleft()
#                 yield 'recvd'
#
#         elif instruct == 'jgz':
#             reg_name = command.split(' ')[1]
#             offset = value(command.split(' ')[2])
#
#             if r[reg_name] > 0:
#                 i += offset
#                 i -= 1
#         i += 1
#         j += 1
#
#         print(j)
#
#         if j == 1375:
#             print('i:',i)

# input_text = ['snd 1', 'snd 2', 'snd p', 'rcv a', 'rcv b', 'rcv c', 'rcv d']
#
# program_length = len(input_text)
#
# q1 = collections.deque()
#
# j = 0
#
# for signal in program(0, q1, q1, j):
#     if signal == 'recvd': break
#
# q0, q1 = collections.deque(), collections.deque()
#
# prog_0, prog_1 = program(0, q1, q0, j), program(1, q0, q1, j)
#
# i, count = 0, 0
# while True:
#     a, b = next(prog_1), next(prog_0)
#     count += a == 'send'
#     if {a, b} == {'wait'}:
#         break
#
# print('Part 2 Answer:', count)
#
# # test
#
# def program1(pid, inqueue, outqueue):
#     r = collections.defaultdict(int)
#     r['p'] = pid
#     val = lambda v: r[v] if v.isalpha() else int(v)
#
#     i = 0
#     while 0 <= i < len(input_text):
#         f, X, Y, *_ = (input_text[i] + " ?").split()
#         if f == 'set':      r[X] = val(Y)
#         elif f == 'add':    r[X] += val(Y)
#         elif f == 'mul':    r[X] *= val(Y)
#         elif f == 'mod':    r[X] %= val(Y)
#         elif f == 'jgz' and val(X) > 0:     i += val(Y) - 1
#         elif f == 'snd':
#             outqueue.append(val(X))
#             yield 'send'
#         elif f == 'rcv':
#             while not inqueue:
#                 yield 'wait'
#             else:
#                 r[X] = inqueue.popleft()
#                 yield 'recd'
#         print(i)
#         i += 1
#
# q1 = collections.deque()
# for s in program1(0, q1, q1):
#     if s == 'recd': break
# print(q1[-1])
#
# q0, q1 = collections.deque(), collections.deque()
# P0, P1 = program1(0, q1, q0), program1(1, q0, q1)
# i, count = 0, 0
# while True:
#     a, b = next(P1), next(P0)
#     count += a == 'send'
#     if {a, b} == {'wait'}:
#         break
# print(count)

# TEST

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
