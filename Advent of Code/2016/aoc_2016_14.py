import requests
import hashlib
from sys import setrecursionlimit
setrecursionlimit(10000)

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_14_input.txt'
resp = requests.get(url)
input_text = resp.text

# Part 1

i = 0

key_list = []

limit = 64

while len(key_list) < limit:
    indexed = input_text + str(i)
    res = hashlib.md5(indexed.encode()).hexdigest()
    match_found = False
    for j in range(len(res) - 2):
        char = res[j]
        trip_found = False
        if res[j + 1] == char and res[j + 2] == char:
            trip_found = True
            string_check = char * 5
            for k in range(1000):
                check_index = k + i + 1
                hash_to_check = hashlib.md5((input_text + str(check_index)).encode()).hexdigest()
                if hash_to_check.find(string_check) != -1:
                    match_found = True
                    break
            if match_found:
                key_list.append(i)
                break
            elif trip_found and not match_found:
                break
        if match_found:
            break

    i += 1

last_key = key_list[limit - 1]

print('Part 1 Answer:', last_key)

# Part 2

def hashloop(string):
    for _ in range(2017):
        hash_to_check = hashlib.md5((string).encode()).hexdigest()
        string = hash_to_check

    return string


i = 0

key_list = []

limit = 64

hashed_dict = {}

while len(key_list) < limit:
    indexed = input_text + str(i)
    res = hashloop(indexed)
    match_found = False
    for j in range(len(res) - 2):
        char = res[j]
        trip_found = False
        if res[j + 1] == char and res[j + 2] == char:
            trip_found = True
            string_check = char * 5
            for k in range(1000):
                check_index = k + i + 1
                if check_index in hashed_dict:
                    hash_to_check = hashed_dict[check_index]
                else:
                    hash_to_check = hashloop((input_text + str(check_index)))
                    hashed_dict.update({check_index: hash_to_check})
                if hash_to_check.find(string_check) != -1:
                    # print(res, hash_to_check, string_check, k, i)
                    match_found = True
                    break
            if match_found:
                key_list.append(i)
                break
            elif trip_found and not match_found:
                break
        if match_found:
            break

    i += 1

last_key = key_list[limit - 1]

print('Part 2 Answer:', last_key)
