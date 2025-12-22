import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_16_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

max_length = 272

string = input_text

while len(string) < max_length:
    flipped = string[::-1]
    new_string = ''
    for char in flipped:
        if char == '1':
            new_string = new_string + '0'
        else:
            new_string = new_string + '1'
    string = string + '0' + new_string

string = string[:max_length]

checksum = ''

while len(checksum) % 2 == 0:
    checksum = ''
    for i in range(len(string)):
        if i % 2 != 0:
            continue
        else:
            if string[i] == string[i + 1]:
                checksum += '1'
            else:
                checksum += '0'
    string = checksum

print('Part 1 Answer:', checksum)

# Part 2

max_length = 35651584

string = input_text

while len(string) < max_length:
    flipped = string[::-1]
    new_string = flipped.replace('1', 'x').replace('0', '1').replace('x', '0')
    string = string + '0' + new_string

string = string[:max_length]

while len(string) % 2 == 0:
    string = ''.join('1' if a==b else '0' for a,b in zip(string[::2], string[1::2]))

print('Part 2 Answer:', string)