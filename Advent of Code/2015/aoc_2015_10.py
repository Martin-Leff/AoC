import requests
import re
from itertools import groupby

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_10_input.txt'
resp = requests.get(url)
input_text = resp.text

def order_of_chars(string):
    res = re.findall(r"(.)\1*", string)
    return res

def count_occurs(string, res):
    new_string = ''
    index = 0
    count = 0
    i = 0
    string_len = len(string)
    for num in string:
        i += 1
        if num == res[index]:
            count += 1
        else:
            new_string = new_string + str(count) + res[index]
            index += 1
            count = 1
            if i == string_len:
                new_string = new_string + str(count) + res[index]
    return new_string

process_count = 40
string = input_text
i = 0
length = 0

while i < process_count:
    res = order_of_chars(string)
    new_string = count_occurs(string, res)
    string = new_string
    length = len(string)
    i += 1

print('Part 1 Answer:', length)

# Part 2

def look_and_say(string):
    return ''.join(str(len(list(v))) + k for k, v in groupby(string))

process_count = 50
string = input_text
i = 0

while i < process_count:
    string = look_and_say(string)
    print(i)
    i += 1

length = len(string)

print('Part 2 Answer:', length)