import requests
import regex as re
import collections
from collections import deque, Counter
from itertools import chain, combinations

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_11_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def is_valid(floor):
    valid = False
    if len(set(type for _, type in floor)) < 2 or all((obj, 'generator') in floor for (obj, type) in floor if type == 'microchip'):
        valid = True

    return valid

def next_phase(state):
    moves, el, floor_list = state

    possible_moves = chain(combinations(floor_list[el], 2), combinations(floor_list[el], 1))

    for move in possible_moves:
        for direction in [-1, 1]:
            next_el = el + direction
            if not 0 <= next_el < len(floor_list):
                continue

            next_floors = floor_list.copy()
            next_floors[el] = next_floors[el].difference(move)
            next_floors[next_el] = next_floors[next_el].union(move)

            if (is_valid(next_floors[el])) and is_valid(next_floors[next_el]):
                yield (moves + 1, next_el, next_floors)

def all_at_top(floor_list):
    complete = False
    if all(not floor for number, floor, in enumerate(floor_list) if number < len(floor_list) - 1):
        complete = True
    return complete

def min_moves(floor_list):
    seen = set()
    queue = deque([(0, 0, floor_list)])

    while queue:
        state = queue.popleft()
        moves, _, floor_list = state

        if all_at_top(floor_list):
            return moves

        for next_state in next_phase(state):
            key = count_objects(next_state)
            if key not in seen:
                seen.add(key)
                queue.append(next_state)

def count_objects(state):
    _, el, floor_list = state
    count = el, tuple(tuple(Counter(type for _, type in floor).most_common()) for floor in floor_list)
    return count


floor_list = [set(re.findall(r'(\w+)(?:-compatible)? (microchip|generator)', line)) for line in input_text]

total_moves = min_moves(floor_list)

print('Part 1 Answer:', total_moves)

# Part 2

floor_list[0] = floor_list[0].union([('elerium', 'generator'), ('elerium', 'microchip'), ('dilithium', 'generator'), ('dilithium', 'microchip')])

total_moves = min_moves(floor_list)

print('Part 2 Answer:', total_moves)