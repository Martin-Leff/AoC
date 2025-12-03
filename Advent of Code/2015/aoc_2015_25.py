import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_25_input.txt'

resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

row = int(input_text[0].split(' ')[16].strip(','))
col = int(input_text[0].split(' ')[18].strip('.'))

start_inc = col
start_val = 20151125
mult_val = 252533
div_val = 33554393

i = 0
j = 1

for _ in range(col):
    i += j
    j += 1

col_iter = col

for _ in range(row - 1):
    i += col_iter
    col_iter += 1


cur_val = start_val

for _ in range(i - 1):
    new_val = (cur_val * mult_val) % div_val
    cur_val = new_val

print('Part 1 Answer:', cur_val)
