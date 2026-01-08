import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_2_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

i = 0
total = 0

for i in range(len(input_text)):
    char = input_text[i]
    if i < len(input_text) - 1:
        compare = input_text[i + 1]
    else:
        compare = input_text[0]

    if char == compare:
        total += int(char)

print('Part 1 Answer:', total)

# Part 2

total = 0

len_text = len(input_text)

half_length = len_text / 2

for i in range(len_text):
    char = input_text[i]
    compare_index = int(i + half_length)

    if compare_index >= len_text:
        compare_index = compare_index - len_text

    compare = input_text[compare_index]

    if char == compare:
        total += int(char)

print('Part 2 Answer:', total)