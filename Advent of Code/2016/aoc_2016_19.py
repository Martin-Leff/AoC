import requests
import hashlib
import math
import collections

from fontTools.misc.cython import returns

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_19_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

elf_list = list(range(1, int(input_text) + 1))

while len(elf_list) > 1:
    if len(elf_list) % 2 != 0:
        new_elf_list = elf_list[::2]
        new_elf_list.pop(0)
    else:
        new_elf_list = elf_list[::2]
    elf_list = new_elf_list

final_elf = elf_list[0]

print('Part 1 Answer:', final_elf)

# Part 2

queue_1 = collections.deque()
queue_2 = collections.deque()

elf_total = int(input_text)

for i in range(elf_total):
    queue_1.append(i + 1)

len_q1 = len(queue_1)
len_q2 = len(queue_2)

l = elf_total

while len_q1 > len_q2:
    queue_2.append(queue_1.pop())
    len_q1 -= 1
    len_q2 += 1


while l > 2:
    queue_2.pop()
    queue_2.appendleft(queue_1.popleft())
    len_q1 -= 1
    if (len_q2 - len_q1) > 1:
        queue_1.append(queue_2.pop())
        len_q1 += 1
        len_q2 -= 1
    l -= 1

final_elf = queue_1[0]

print('Part 2 Answer:', final_elf)

