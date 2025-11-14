import requests
from functools import reduce

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_20_input.txt'

resp = requests.get(url)
input_text = resp.text
# input_text = input_text.splitlines()

# Part 1

min_val = int(input_text)

# max_houses = 10000000
# house_total_max = 0
#
# for i in range(700000, max_houses):
#     house_num = i + 1
#     house_total = 0
#     for j in range(house_num):
#         elf_num = j + 1
#         if house_num % elf_num == 0:
#             house_total += elf_num * 10
#
#     if (house_total > house_total_max) or (house_total > 25000000):
#         print(house_num, house_total)
#         house_total_max = house_total
#
#     if house_total > min_val:
#         print(house_num, house_total)
#         break

def calc_presents(house_num):
    f = set(reduce(list.__add__, ([i, house_num // i] for i in range(1, int(house_num ** 0.5) + 1) if house_num % i == 0)))
    house_total = 0
    for x in f:
        house_total += 10 * x
    return house_total

i = 1
while True:
    house_total = calc_presents(i)
    if house_total > min_val:
        break
    i += 1

print('Part 1 Answer:', i)

# Part 2

def calc_presents_2(house_num):
    f = set(reduce(list.__add__, ([i, house_num // i] for i in range(1, int(house_num ** 0.5) + 1) if house_num % i == 0)))
    house_total = 0
    for x in f:
        if (house_num / x) > 50:
            pass
        else:
            house_total += 11 * x
    return house_total

i = 1
while True:
    house_total = calc_presents_2(i)
    if house_total > min_val:
        break
    i += 1

print('Part 2 Answer:', i)