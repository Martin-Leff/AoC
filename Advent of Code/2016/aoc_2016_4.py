import requests
from collections import Counter

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_4_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

sector_id_total = 0

for line in input_text:
    checksum = line.split('[')[1].strip(']')
    num = int(line[-10:-7])
    string = line[:-11].replace('-', '')

    rank_letters = sorted((-string.count(letter), letter) for letter in set(string))
    check_string = ''.join(letter for _, letter in rank_letters[:5])

    if checksum == check_string:
        sector_id_total += num

print('Part 1 Answer:', sector_id_total)

# Part 2

def cipher(string, number):
    result = ''

    # traverse text
    for i in range(len(string)):
        char = string[i]
        # Encrypt uppercase characters
        if char == '-':
            result += ' '
        elif (char.isupper()):
            result += chr((ord(char) + number - 65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + number - 97) % 26 + 97)

    return result

find_string = 'northpole object storage'
id_num = 0

for line in input_text:
    num = int(line[-10:-7])
    string = line[:-11]
    if cipher(string, num) == find_string:
        id_num = num

print('Part 2 Answer:', id_num)