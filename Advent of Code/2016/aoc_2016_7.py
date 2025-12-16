import requests
import regex as re

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_7_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

abba_count = 0

def abba_checkstring(i, string):
    return (string[i] == string[i + 3]) and (string[i + 1] == string[i + 2]) and (string[i] != string[i + 1])

for string in input_text:
    abba_check = True
    abba_found = False
    hypernet_abba = False
    for i in range(len(string) - 3):
        if abba_checkstring(i, string) and abba_check:
            abba_found = True
        elif string[i] == '[':
            abba_check = False
        elif string[i] == ']':
            abba_check = True
        elif abba_checkstring(i, string) and not abba_check:
            hypernet_abba = True
    if abba_found and not hypernet_abba:
        abba_count += 1

print('Part 1 Answer:', abba_count)

# Part 2

# input_text = ['adncdhtushtvtfcbez[rvaycmplefdvbrchc]vtviiplkpfhsyhwzz[pdpnsseaizogzvtkcq]piorguaivfpummlo']
# print(input_text)

ssl_count = 0

def ssl_check(i, string):
    return (string[i] == string[i + 2]) and (string[i] != string[i + 1])

for string in input_text:
    aba_check = True
    aba_found = False
    for i in range(len(string) - 2):
        char1 = string[i]
        if ssl_check(i, string) and aba_check:
            char2 = string[i + 1]
            string_check = string[:i] + string[i + 3:]
            bab = char2 + char1 + char2

            matches = re.findall(r"\[.*?\]", string)
            for match in matches:
                if bab in match:
                    ssl_count += 1
                    aba_found = True
        elif string[i] == '[':
            aba_check = False
        elif string[i] == ']':
            aba_check = True
        if aba_found:
            # print(string)
            break


print('Part 2 Answer:', ssl_count)
