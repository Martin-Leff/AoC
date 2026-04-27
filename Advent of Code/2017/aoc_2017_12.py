import requests
import collections

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_12_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

zero_group = [0]
change_flag = True

while change_flag:
    change_flag = False
    for line in input_text:
        start = int(line.split('<->')[0].strip(' '))
        start_list = [start]
        end_group = line.split('<->')[1].split(',')
        end_ints = []
        for end in end_group:
            end_int = int(end.strip(' '))
            end_ints.append(end_int)

        for num in start_list and end_ints:
            if num in zero_group:
                if start not in zero_group:
                    zero_group.append(start)
                    change_flag = True
                for end_int in end_ints:
                    if end_int not in zero_group:
                        zero_group.append(end_int)
                        change_flag = True
    zero_group = list(set(zero_group))

zero_group = list(set(zero_group))
zero_group_len = len(zero_group)

print('Part 1 Answer:', zero_group_len)

# Part 2

number_list = []

for line in input_text:
    start = int(line.split('<->')[0].strip(' '))
    number_list.append(start)

group_count = 0

while number_list:
    start_group = [number_list[0]]

    change_flag = True

    while change_flag:
        change_flag = False
        for line in input_text:
            start = int(line.split('<->')[0].strip(' '))
            start_list = [start]
            end_group = line.split('<->')[1].split(',')
            end_ints = []
            for end in end_group:
                end_int = int(end.strip(' '))
                end_ints.append(end_int)

            for num in start_list and end_ints:
                if num in start_group:
                    if start not in start_group:
                        start_group.append(start)
                        change_flag = True
                    for end_int in end_ints:
                        if end_int not in start_group:
                            start_group.append(end_int)
                            change_flag = True
        start_group = list(set(start_group))

    group_count += 1
    start_group = list(set(start_group))

    number_list = [x for x in number_list if x not in start_group]

print('Part 2 Answer:', group_count)
