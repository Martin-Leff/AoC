import requests
import hashlib

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_4_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

def md5_hash(string):
    res = hashlib.md5(string.encode()).hexdigest()
    return res

checkstring = '00000'
i = 0
found = False
final_text = ''

while not found:
    text = input_text + str(i)
    result = md5_hash(text)
    if result.startswith(checkstring):
        final_text = text
        found = True
        continue
    i += 1

print('Part 1 Answer:', i)

# Part 2

checkstring = '000000'
i = 0
found = False
final_text = ''

while not found:
    text = input_text + str(i)
    result = md5_hash(text)
    if result.startswith(checkstring):
        final_text = text
        found = True
        continue
    i += 1

print('Part 2 Answer:', i)