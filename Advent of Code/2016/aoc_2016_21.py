import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_21_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def swap_pos(string, pos_1, pos_2):
    min_pos = min(pos_1, pos_2)
    max_pos = max(pos_1, pos_2)
    new_string = string[:min_pos] + string[max_pos] + string[min_pos + 1:max_pos] + string[min_pos] + string[max_pos + 1:]
    return new_string

def swap_letter(string, let_1, let_2):
    let_1_pos = string.find(let_1)
    let_2_pos = string.find(let_2)
    min_pos = min(let_1_pos, let_2_pos)
    max_pos = max(let_1_pos, let_2_pos)
    new_string = string[:min_pos] + string[max_pos] + string[min_pos + 1:max_pos] + string[min_pos] + string[max_pos + 1:]
    return new_string

def rotate_steps(string, dir, steps):
    while steps > len(string):
        steps -= len(string)
    if dir == 'right':
        new_string = string[-steps:] + string[:-steps]
    else:
        new_string = string[steps:] + string[:steps]
    return new_string

def rotate_index(string, index_let):
    index = string.find(index_let)
    dir = 'right'
    if index >= 4:
        steps = 2 + index
    else:
        steps = 1 + index

    new_string = rotate_steps(string, dir, steps)
    return new_string

def reverse(string, pos_1, pos_2):
    rev_section = string[pos_1:pos_2 + 1][::-1]
    new_string = string[:pos_1] + rev_section + string[pos_2 + 1:]
    return new_string

def move_pos(string, pos_1, pos_2):
    insert_char = string[pos_1]
    string = string[:pos_1] + string[pos_1 + 1:]
    new_string = string[:pos_2] + insert_char + string[pos_2:]
    return new_string

unscrambled = 'abcdefgh'

for line in input_text:
    if line.startswith('swap position'):
        pos_1 = int(line.split(' ')[2])
        pos_2 = int(line.split(' ')[5])
        unscrambled = swap_pos(unscrambled, pos_1, pos_2)
    elif line.startswith('swap letter'):
        let_1 = line.split(' ')[2]
        let_2 = line.split(' ')[5]
        unscrambled = swap_letter(unscrambled, let_1, let_2)
    elif line.startswith('rotate') and (line.endswith('steps') or line.endswith('step')):
        dir = line.split(' ')[1]
        steps = int(line.split(' ')[2])
        unscrambled = rotate_steps(unscrambled, dir, steps)
    elif line.startswith('rotate based'):
        index_let = line.split(' ')[6]
        unscrambled = rotate_index(unscrambled, index_let)
    elif line.startswith('reverse'):
        pos_1 = int(line.split(' ')[2])
        pos_2 = int(line.split(' ')[4])
        unscrambled = reverse(unscrambled, pos_1, pos_2)
    elif line.startswith('move'):
        pos_1 = int(line.split(' ')[2])
        pos_2 = int(line.split(' ')[5])
        unscrambled = move_pos(unscrambled, pos_1, pos_2)

print('Part 1 Answer:', unscrambled)

# Part 2

def swap_pos_rev(string, pos_1, pos_2):
    min_pos = min(pos_1, pos_2)
    max_pos = max(pos_1, pos_2)
    new_string = string[:min_pos] + string[max_pos] + string[min_pos + 1:max_pos] + string[min_pos] + string[max_pos + 1:]
    return new_string

def swap_letter_rev(string, let_1, let_2):
    let_1_pos = string.find(let_1)
    let_2_pos = string.find(let_2)
    min_pos = min(let_1_pos, let_2_pos)
    max_pos = max(let_1_pos, let_2_pos)
    new_string = string[:min_pos] + string[max_pos] + string[min_pos + 1:max_pos] + string[min_pos] + string[max_pos + 1:]
    return new_string

def rotate_steps_rev(string, dir, steps):
    while steps > len(string):
        steps -= len(string)
    if dir == 'right':
        new_string = string[-steps:] + string[:-steps]
    else:
        new_string = string[steps:] + string[:steps]
    return new_string

def rotate_index_rev(string, index_let):
    new_string = 'failure'

    for steps in range(len(string)):
        dir = 'left'
        test_string = rotate_steps(string, dir, steps)

        if rotate_index(test_string, index_let) == string:
            new_string = test_string

    return new_string

def reverse_rev(string, pos_1, pos_2):
    rev_section = string[pos_1:pos_2 + 1][::-1]
    new_string = string[:pos_1] + rev_section + string[pos_2 + 1:]
    return new_string

def move_pos_rev(string, pos_1, pos_2):
    insert_char = string[pos_1]
    string = string[:pos_1] + string[pos_1 + 1:]
    new_string = string[:pos_2] + insert_char + string[pos_2:]
    return new_string


scrambled = 'fbgdceah'

reversed_input = input_text[::-1]

for line in reversed_input:
    if line.startswith('swap position'):
        pos_1 = int(line.split(' ')[2])
        pos_2 = int(line.split(' ')[5])
        scrambled = swap_pos_rev(scrambled, pos_1, pos_2)
    elif line.startswith('swap letter'):
        let_1 = line.split(' ')[2]
        let_2 = line.split(' ')[5]
        scrambled = swap_letter_rev(scrambled, let_1, let_2)
    elif line.startswith('rotate') and (line.endswith('steps') or line.endswith('step')):
        dir = line.split(' ')[1]
        if dir == 'right':
            dir = 'left'
        else:
            dir = 'right'
        steps = int(line.split(' ')[2])
        scrambled = rotate_steps_rev(scrambled, dir, steps)
    elif line.startswith('rotate based'):
        index_let = line.split(' ')[6]
        scrambled = rotate_index_rev(scrambled, index_let)
    elif line.startswith('reverse'):
        pos_1 = int(line.split(' ')[2])
        pos_2 = int(line.split(' ')[4])
        scrambled = reverse_rev(scrambled, pos_1, pos_2)
    elif line.startswith('move'):
        pos_1 = int(line.split(' ')[2])
        pos_2 = int(line.split(' ')[5])
        scrambled = move_pos_rev(scrambled, pos_2, pos_1)

print('Part 2 Answer:', scrambled)
