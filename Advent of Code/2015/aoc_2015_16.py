import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_16_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

children_key = 3
cats_key = 7
samoyeds_key = 2
pomeranians_key = 3
akitas_key = 0
vizslas_key = 0
goldfish_key = 5
trees_key = 3
cars_key = 2
perfumes_key = 1

key_dict = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

sue_dict = {}

for line in input_text:
    items = line.split(' ')
    number = items[1].strip(':')
    index_1 = items[2].strip(':')
    index_val_1 = int(items[3].strip(','))
    index_2 = items[4].strip(':')
    index_val_2 = int(items[5].strip(','))
    index_3 = items[6].strip(':')
    index_val_3 = int(items[7])
    sue_dict[number] = {index_1: index_val_1, index_2: index_val_2, index_3: index_val_3}

# print(sue_dict)

sue_number = 0
final_sue = 0

for sue in sue_dict:
    this_sue = sue_dict[sue]
    stop = False
    for index in this_sue:
        if this_sue[index] != key_dict[index]:
            stop = True
            pass
    if stop:
        pass
    else:
        final_sue = sue

print('Part 1 Answer:', final_sue)

# Part 2

final_sue = 0

for sue in sue_dict:
    this_sue = sue_dict[sue]
    stop = False
    for index in this_sue:
        if index == 'cats' or index == 'trees':
            if this_sue[index] <= key_dict[index]:
                stop = True
                pass
        elif index == 'pomeranians' or index == 'goldfish':
            if this_sue[index] >= key_dict[index]:
                stop = True
                pass
        elif this_sue[index] != key_dict[index]:
            stop = True
            pass
    if stop:
        pass
    else:
        final_sue = sue

print('Part 2 Answer:', final_sue)