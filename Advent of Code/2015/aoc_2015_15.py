import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_15_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

cookie_dict = {}

for line in input_text:
    items = line.split(' ')
    cookie = items[0].strip(':')
    cap = int(items[2].strip(','))
    dur = int(items[4].strip(','))
    flav = int(items[6].strip(','))
    txt = int(items[8].strip(','))
    cal = int(items[10].strip(','))
    cookie_dict[cookie] = {'cap': cap, 'dur': dur, 'flav': flav, 'txt': txt, 'cal': cal}

tsp_max = 100
max_score = 0

for i in range(tsp_max):
    for j in range(tsp_max - i):
        for k in range (tsp_max - (i + j)):
            h = tsp_max - (i + j + k)
            cap_total = ((i * cookie_dict['Sprinkles']['cap']) + (j * cookie_dict['PeanutButter']['cap']) +
                         (k * cookie_dict['Frosting']['cap']) + (h * cookie_dict['Sugar']['cap']))
            dur_total = ((i * cookie_dict['Sprinkles']['dur']) + (j * cookie_dict['PeanutButter']['dur']) +
                         (k * cookie_dict['Frosting']['dur']) + (h * cookie_dict['Sugar']['dur']))
            flav_total = ((i * cookie_dict['Sprinkles']['flav']) + (j * cookie_dict['PeanutButter']['flav']) +
                         (k * cookie_dict['Frosting']['flav']) + (h * cookie_dict['Sugar']['flav']))
            txt_total = ((i * cookie_dict['Sprinkles']['txt']) + (j * cookie_dict['PeanutButter']['txt']) +
                         (k * cookie_dict['Frosting']['txt']) + (h * cookie_dict['Sugar']['txt']))
            if any (x < 0 for x in [cap_total, dur_total, flav_total, txt_total]):
                score = 0
            else:
                score = cap_total * dur_total * flav_total * txt_total

            if score > max_score:
                max_score = score

print('Part 1 Answer:', max_score)

# Part 2

max_score = 0

for i in range(tsp_max):
    for j in range(tsp_max - i):
        for k in range (tsp_max - (i + j)):
            h = tsp_max - (i + j + k)
            cap_total = ((i * cookie_dict['Sprinkles']['cap']) + (j * cookie_dict['PeanutButter']['cap']) +
                         (k * cookie_dict['Frosting']['cap']) + (h * cookie_dict['Sugar']['cap']))
            dur_total = ((i * cookie_dict['Sprinkles']['dur']) + (j * cookie_dict['PeanutButter']['dur']) +
                         (k * cookie_dict['Frosting']['dur']) + (h * cookie_dict['Sugar']['dur']))
            flav_total = ((i * cookie_dict['Sprinkles']['flav']) + (j * cookie_dict['PeanutButter']['flav']) +
                         (k * cookie_dict['Frosting']['flav']) + (h * cookie_dict['Sugar']['flav']))
            txt_total = ((i * cookie_dict['Sprinkles']['txt']) + (j * cookie_dict['PeanutButter']['txt']) +
                         (k * cookie_dict['Frosting']['txt']) + (h * cookie_dict['Sugar']['txt']))
            cal_total = ((i * cookie_dict['Sprinkles']['cal']) + (j * cookie_dict['PeanutButter']['cal']) +
                         (k * cookie_dict['Frosting']['cal']) + (h * cookie_dict['Sugar']['cal']))
            if any (x < 0 for x in [cap_total, dur_total, flav_total, txt_total]):
                score = 0
            elif cal_total != 500:
                score = 0
            else:
                score = cap_total * dur_total * flav_total * txt_total
            if score > max_score:
                max_score = score

print('Part 2 Answer:', max_score)