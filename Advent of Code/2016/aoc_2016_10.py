import requests
import regex as re
import collections

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_10_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

bot = collections.defaultdict(list)
output = collections.defaultdict(list)
pipeline = {}

val_comp_1 = 61
val_comp_2 = 17
part_1_ans = 0

for line in input_text:
    if line.startswith('value'):
        val = int(line.split(' ')[1])
        target = line.split(' ')[5]
        bot[target].append(val)
    else:
        start_bot = line.split(' ')[1]
        low_bot = line.split(' ')[6]
        high_bot = line.split(' ')[11]
        t1, t2 = re.findall(r' (bot|output)', line)
        pipeline[start_bot] = (t1,low_bot),(t2,high_bot)

while bot:
    for key, value in dict(bot).items():
        if len(value) == 2:
            v1, v2 = sorted(bot.pop(key))
            if v1 == val_comp_2 and v2 == val_comp_1:
                part_1_ans = key
            (t1, n1), (t2, n2) = pipeline[key]
            eval(t1)[n1].append(v1)
            eval(t2)[n2].append(v2)

print('Part 1 Answer:', part_1_ans)

# Part 2

output_0 = output['0'][0]
output_1 = output['1'][0]
output_2 = output['2'][0]

total = output_0 * output_1 * output_2

print('Part 2 Answer:', total)