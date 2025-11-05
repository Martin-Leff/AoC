import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_8_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

char_count = 0
eval_count = 0

for string in input_text:
    string_char_count = len(string)
    char_count += string_char_count

for string in input_text:
    eval_string = eval(string)
    eval_char_count = len(eval_string)
    eval_count += eval_char_count

answer = char_count - eval_count

print('Part 1 Answer:', answer)

# Part 2

repr_count = 0

for string in input_text:
    backslash_count = string.count('\\')
    quote_count = string.count('"')
    string_total = 2 + backslash_count + quote_count
    repr_count += string_total

print('Part 2 Answer:', repr_count)