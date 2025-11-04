import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_5_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def vowel_check(string):
    nice = False
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in vowel_list:
        count += string.count(char)
    if count >= 3:
        nice = True
    return nice

def double_char(string):
    nice = False
    for i in range(len(string)):
        if (string[i] == string[i - 1]) and (i > 0):
            nice = True
    return nice

def naughty_strings(string):
    nice = False
    bad_list = ['ab', 'cd', 'pq', 'xy']
    count = 0
    for char in bad_list:
        count += string.count(char)
    if count == 0:
        nice = True
    return nice

def string_test(string):
    nice = False
    if vowel_check(string) and double_char(string) and naughty_strings(string):
        nice = True
    return nice

count = 0

for string in input_text:
    if string_test(string):
        count += 1

print('Part 1 Answer:', count)

# Part 2

def double_char_split(string):
    nice = False
    for i in range(len(string)):
        if (string[i] == string[i - 2]) and (i > 1):
            nice = True
    return nice

def pair_repeat(string):
    nice = False
    for i in range(len(string)):
        if (i > 0):
            segment = string[i - 1] + string[i]
            remainder = string[(i + 1):]
            if segment in remainder:
                nice = True
    return nice

def string_test_v2(string):
    nice = False
    if pair_repeat(string) and double_char_split(string):
        nice = True
    return nice

count = 0

for string in input_text:
    if string_test_v2(string):
        count += 1

print('Part 2 Answer:', count)
