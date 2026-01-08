import requests
from itertools import combinations

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_4_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

count = 0

for line in input_text:
    line = line.split(' ')
    fail = False
    while line and not fail:
        word = line.pop(0)
        if word in line:
            fail = True

    if not fail:
        count += 1

print('Part 1 Answer:', count)

# Part 2

def check_anagram(string, words):
    anagram = False
    for word in words:
        if sorted(string) == sorted(word):
            anagram = True
            return anagram

    return anagram

count = 0

for line in input_text:
    line = line.split(' ')
    fail = False
    while line and not fail:
        word = line.pop(0)
        if check_anagram(word, line):
            fail = True

    if not fail:
        count += 1

print('Part 2 Answer:', count)