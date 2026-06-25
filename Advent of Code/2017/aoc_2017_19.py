import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_19_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def next_char(row, col, direction, maze):
    if direction == 'S':
        new_row = row + 1
        new_col = col
    elif direction == 'W':
        new_row = row
        new_col = col - 1
    elif direction == 'N':
        new_row = row - 1
        new_col = col
    else:
        new_row = row
        new_col = col + 1
    char = maze[new_row][new_col]
    return char, new_row, new_col

def change_dir(row, col, direction, maze, orig_dir):

    if direction in ['N', 'S']:
        dir_options = ['E', 'W']
    else:
        dir_options = ['N', 'S']

    for new_dir in dir_options:
        next_step = next_char(row, col, new_dir, maze)[0]
        if next_step == Space_char:
            continue
        else:
            return new_dir

def check_for_end(row, col, maze):
    count = 0
    if maze[row - 1][col] == Space_char:
        count += 1
    if maze[row + 1][col] == Space_char:
        count += 1
    if maze[row][col - 1] == Space_char:
        count += 1
    if maze[row][col + 1] == Space_char:
        count += 1

    if count >= 3:
        return True
    else:
        return False


maze = input_text
start_dir = 'S'
row_one = input_text[0]
start_char = '|'
start_pos = row_one.index(start_char)
NS_char = '|'
EW_char = '-'
Cross_char = '+'
Space_char = ' '

row = 0
col = start_pos
direction = start_dir
letters = ''

while True:
    new_char, new_row, new_col = next_char(row, col, direction, maze)

    row = new_row
    col = new_col

    # print(new_char)

    if new_char == Cross_char:
        direction = change_dir(row, col, direction, maze, direction)


    if new_char not in [NS_char, EW_char, Cross_char, Space_char]:
        letters += new_char

    if check_for_end(row, col, maze):
        break

print('Part 1 Answer:', letters)

# Part 2

row = 0
col = start_pos
direction = start_dir
letters = ''
count = 1

while True:
    new_char, new_row, new_col = next_char(row, col, direction, maze)

    row = new_row
    col = new_col

    if new_char == Cross_char:
        direction = change_dir(row, col, direction, maze, direction)

    count += 1

    if check_for_end(row, col, maze):
        break

print('Part 2 Answer:', count)