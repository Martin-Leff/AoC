import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_6_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

string_len = len(input_text[0])

password = ''

for char_pos in range(string_len):
    char_pos_dict = {}
    for string in input_text:
        char = string[char_pos]
        if char in char_pos_dict:
            cur_count = char_pos_dict[char]
            char_pos_dict.update({char: cur_count + 1})
        else:
            char_pos_dict.update({char: 0})

    password += max(char_pos_dict, key=char_pos_dict.get)

print('Part 1 Answer:', password)

# Part 2

string_len = len(input_text[0])

password = ''

for char_pos in range(string_len):
    char_pos_dict = {}
    for string in input_text:
        char = string[char_pos]
        if char in char_pos_dict:
            cur_count = char_pos_dict[char]
            char_pos_dict.update({char: cur_count + 1})
        else:
            char_pos_dict.update({char: 0})

    password += min(char_pos_dict, key=char_pos_dict.get)

print('Part 2 Answer:', password)