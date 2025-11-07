import requests
import re
import itertools

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_13_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

guest_list = []
guest_dict = {}

for row in input_text:
    items = row.split(' ')
    first = items[0]
    next_to = items[10].strip('.')
    pos_neg = items[2]

    if pos_neg == 'gain':
        val = int(items[3])
    else:
        val = -1 * int(items[3])

    if first not in guest_list:
        guest_list.append(first)

    guest_dict.update({(first, next_to): val})

max_val = 0

perm_list = itertools.permutations(guest_list)
for perm in perm_list:
    perm = list(perm)
    i = 0
    perm_val = 0

    for i in range(len(perm)):
        guest_1 = perm[i]
        if i == len(perm) - 1:
            guest_2 = perm[0]
        else:
            guest_2 = perm[i + 1]
        next_to_val = guest_dict[(guest_1, guest_2)] + guest_dict[(guest_2, guest_1)]
        perm_val += next_to_val
        i += 1

    if perm_val > max_val:
        max_val = perm_val

print('Part 1 Answer:', max_val)

# Part 2

me = 'Me'
guest_list_2 = guest_list
guest_list_2.append(me)

for guest in guest_list:
    guest_dict.update({(guest, me): 0})
    guest_dict.update({(me, guest): 0})

max_val = 0

perm_list = itertools.permutations(guest_list_2)
for perm in perm_list:
    perm = list(perm)
    i = 0
    perm_val = 0

    for i in range(len(perm)):
        guest_1 = perm[i]
        if i == len(perm) - 1:
            guest_2 = perm[0]
        else:
            guest_2 = perm[i + 1]
        next_to_val = guest_dict[(guest_1, guest_2)] + guest_dict[(guest_2, guest_1)]
        perm_val += next_to_val
        i += 1

    if perm_val > max_val:
        max_val = perm_val

print('Part 2 Answer:', max_val)
