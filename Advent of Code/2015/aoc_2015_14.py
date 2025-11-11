import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_14_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

race_length = 2503
reindeer_dict = {}
reindeer_list = []

for row in input_text:
    items = row.split(' ')
    reindeer = items[0]
    speed = int(items[3])
    move_time = int(items[6])
    rest_time = int(items[13])
    total_cycle = move_time + rest_time
    if reindeer not in reindeer_list:
        reindeer_list.append(reindeer)

    reindeer_dict.update({reindeer:{'speed': speed, 'move': move_time, 'rest': rest_time, 'cycle': total_cycle}})

distance_max = 0

for reindeer in reindeer_list:
    reindeer_dist = 0
    for second in range(race_length):
        cycle_location = (second) % reindeer_dict[reindeer]['cycle']
        if cycle_location < reindeer_dict[reindeer]['move']:
            reindeer_dist += reindeer_dict[reindeer]['speed']
        else:
            pass
    if reindeer_dist > distance_max:
        distance_max = reindeer_dist

print('Part 1 Answer:', distance_max)

# Part 2

distance_dict = {}
reindeer_tuple_list = []

# for reindeer in reindeer_list:
#     reindeer_dist = 0
#     for second in range(race_length):
#         cycle_location = second % reindeer_dict[reindeer]['cycle']
#         if cycle_location < reindeer_dict[reindeer]['move']:
#             reindeer_dist += reindeer_dict[reindeer]['speed']
#         reindeer_tuple = (second, {reindeer:reindeer_dist})
#         reindeer_tuple_list.append(reindeer_tuple)

reindeer_dist_dict = {}
reindeer_points_dict = {}

for reindeer in reindeer_list:
    reindeer_dist_dict[reindeer] = 0
    reindeer_points_dict[reindeer] = 0

for second in range(race_length):

    max_second_dist = 0

    for reindeer in reindeer_list:
        reindeer_dist = reindeer_dist_dict[reindeer]
        cycle_location = second % reindeer_dict[reindeer]['cycle']
        if cycle_location < reindeer_dict[reindeer]['move']:
            reindeer_dist += reindeer_dict[reindeer]['speed']
        reindeer_dist_dict[reindeer] = reindeer_dist
        if reindeer_dist > max_second_dist:
            max_second_dist = reindeer_dist

    for reindeer in reindeer_list:
        if reindeer_dist_dict[reindeer] == max_second_dist:
            reindeer_points_dict[reindeer] += 1

winner = max(reindeer_points_dict.values())

print('Part 2 Answer:', winner)