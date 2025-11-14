import requests
import re

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_19_input.txt'

resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

molecule = input_text[-1]

input_text.remove(input_text[-1])
input_text.remove(input_text[-1])

tuple_list = []
start_list = []

for line in input_text:
    items = line.split(' ')
    start_el = items[0]
    if start_el not in start_list:
        start_list.append(start_el)
    end_el = items[2]
    tuple_list.append((start_el, end_el))

new_mol_list = []

for starter in start_list:
    combo_list = [element for element in tuple_list if element[0] == starter]
    for combo in combo_list:
        end_el = combo[1]
        matches = re.finditer(starter, molecule)
        for match in matches:
            new_molecule = molecule[:match.start()] + end_el + molecule[match.end():]
            if new_molecule not in new_mol_list:
                new_mol_list.append(new_molecule)

print('Part 1 Answer:', len(new_mol_list))

# Part 2

tuple_list = []
start_list = []
end_list = []

combo_dict = {}

for line in input_text:
    items = line.split(' ')
    start_el = items[0]
    if start_el not in start_list:
        start_list.append(start_el)
    end_el = items[2]
    if end_el not in end_list:
        end_list.append(end_el)
    combo_dict.update({end_el: start_el})

new_molecule = molecule

count = 0

while new_molecule != 'e':
    for compound in end_list:
        matches = re.finditer(compound, new_molecule)
        for match in matches:
            start_el = combo_dict[compound]
            match_start = match.start()
            match_end = match.end()
            new_molecule = new_molecule[:match_start] + start_el + new_molecule[match_end:]
            count += 1
            break

print('Part 2 Answer:', count)
