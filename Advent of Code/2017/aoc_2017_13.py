import requests
import collections

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_13_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

firewall_dict = {}

for line in input_text:
    layer = int(line.split(':')[0].strip(' '))
    depth = int(line.split(':')[1].strip(' '))
    firewall_dict.update({layer: depth})

# firewall_dict = {0: 3, 1: 2, 4: 4, 6: 4}

steps = max(firewall_dict) + 1

severity = 0

for step in range(steps):
    if step in firewall_dict:
        depth = firewall_dict[step]
        modulo = depth + (depth - 2)

        if step % modulo == 0:
            severity += depth * step

print('Part 1 Answer:', severity)

# Part 2

steps = max(firewall_dict) + 1
step_start = -1
modulo = 0
depth = 0

caught = True

while caught:
    caught = False
    step_start += 1
    for step in range(steps):
        if step in firewall_dict:
            depth = firewall_dict[step]
            modulo = depth + (depth - 2)

            if (step + step_start) % modulo == 0:
                # print(step, step_start, modulo)
                caught = True


print('Part 2 Answer:', step_start)