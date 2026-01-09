import requests
import operator

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_7_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

def get_max(block_list):
    max_index, max_value = max(enumerate(block_list), key=operator.itemgetter(1))
    return max_index, max_value

def distribute_block(dis_index, dis_val, block_list):
    next_index = dis_index + 1
    if next_index < len(block_list):
        start_block = block_list[:dis_index] + [0] + block_list[next_index:]
    else:
        start_block = block_list[:dis_index] + [0]
        next_index = 0

    while dis_val:
        dis_val -= 1
        next_block = start_block[:next_index] + [start_block[next_index] + 1] + start_block[next_index + 1:]
        start_block = next_block
        next_index += 1
        if next_index >= len(start_block):
            next_index -= len(start_block)

    return start_block


input_list = input_text.split('\t')

block_list = []

for input in input_list:
    element = int(input)
    block_list.append(element)

dup_found = False
iteration_list = [block_list]
count = 0

while not dup_found:
    count += 1
    max_index, max_value = get_max(block_list)
    new_block_list = distribute_block(max_index, max_value, block_list)
    if new_block_list not in iteration_list:
        iteration_list.append(new_block_list)
    else:
        dup_found = True
    block_list = new_block_list

print('Part 1 Answer:', count)

# Part 2

block_list = []

for input in input_list:
    element = int(input)
    block_list.append(element)

dup_found = False
iteration_list = [block_list]
count = 0
return_block = []

end_count = 0
start_count = 0

while not dup_found:
    count += 1
    max_index, max_value = get_max(block_list)
    new_block_list = distribute_block(max_index, max_value, block_list)
    if new_block_list not in iteration_list:
        iteration_list.append(new_block_list)
    elif new_block_list == return_block:
        end_count = count
        dup_found = True
    elif not return_block:
        return_block = new_block_list
        start_count = count
    block_list = new_block_list

loop_count = end_count - start_count

print('Part 2 Answer:', loop_count)