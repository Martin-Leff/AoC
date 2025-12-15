import requests
import hashlib

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_5_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

input_text = input_text[0]
pass_len = 8
code = ''
i = 0

while len(code) < pass_len:
    string_num = str(i)
    code_to_test = input_text + string_num
    x = hashlib.md5()
    x.update(code_to_test.encode('utf-8'))
    hex_code = x.hexdigest()

    if hex_code[:5] == '00000':
        char = hex_code[5]
        code += char

    i += 1

print('Part 1 Answer:', code)

# Part 2

pass_len = 8
code_list = []
i = 0
pos_taken = []
code = ''

while len(code_list) < pass_len:
    string_num = str(i)
    code_to_test = input_text + string_num
    x = hashlib.md5()
    x.update(code_to_test.encode('utf-8'))
    hex_code = x.hexdigest()

    if (hex_code[:5] == '00000') and (hex_code[5].isdigit()) and (hex_code[5] not in pos_taken) and (int(hex_code[5]) < pass_len):
        pos = hex_code[5]
        pos_taken.append(pos)
        char = hex_code[6]
        code_list.append((pos, char))

    i += 1

for i in range(pass_len):
    for code_ex in code_list:
        if code_ex[0] == str(i):
            code += code_ex[1]

print('Part 2 Answer:', code)