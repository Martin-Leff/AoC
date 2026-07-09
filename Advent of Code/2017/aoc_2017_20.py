import requests
import math
import collections

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_20_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def calc_distance(pos):
    distance = abs(pos[0]) + abs(pos[1]) + abs(pos[2])
    return distance

def calc_attributes(pos, vel, acc):
    x_pos = pos[0]
    y_pos = pos[1]
    z_pos = pos[2]

    x_vel = vel[0]
    y_vel = vel[1]
    z_vel = vel[2]

    x_acc = acc[0]
    y_acc = acc[1]
    z_acc = acc[2]

    x_vel_new = x_vel + x_acc
    y_vel_new = y_vel + y_acc
    z_vel_new = z_vel + z_acc
    x_pos_new = x_pos + x_vel_new
    y_pos_new = y_pos + y_vel_new
    z_pos_new = z_pos + z_vel_new

    pos_new = [x_pos_new, y_pos_new, z_pos_new]
    vel_new = [x_vel_new, y_vel_new, z_vel_new]

    return pos_new, vel_new

def calc_init_val(value):
    start = '<'
    end = '>'
    idx1 = value.find(start)
    idx2 = value.find(end, idx1 + len(start))
    if idx1 != -1 and idx2 != -1:
        res = value[idx1 + len(start):idx2]
    else:
        res = ''

    res = list(map(int,res.split(',')))

    return res

point_dict = {}
i = 0

for point in input_text:

    pos = calc_init_val(point.split(' ')[0])
    vel = calc_init_val(point.split(' ')[1])
    acc = calc_init_val(point.split(' ')[2])

    point_dict.update({i: {'Position': pos, 'Velocity': vel, 'Accel': acc}})
    i += 1

min_point = ''

for _ in range(1000):
    min_dist = math.inf
    for point in point_dict:
        pos = point_dict[point]['Position']
        vel = point_dict[point]['Velocity']
        acc = point_dict[point]['Accel']
        distance = calc_distance(pos)

        if distance < min_dist:
            min_dist = distance
            min_point = point

        pos_new, vel_new = calc_attributes(pos, vel, acc)

        point_dict.update({point: {'Position': pos_new, 'Velocity': vel_new, 'Accel': acc}})

print('Part 1 Answer:', min_point)

# Part 2


point_dict = {}
i = 0

for point in input_text:

    pos = calc_init_val(point.split(' ')[0])
    vel = calc_init_val(point.split(' ')[1])
    acc = calc_init_val(point.split(' ')[2])

    point_dict.update({i: {'Position': pos, 'Velocity': vel, 'Accel': acc}})
    i += 1

min_point = ''

for _ in range(100):
    min_dist = math.inf
    pos_check = {}
    for point in point_dict:
        pos = point_dict[point]['Position']
        vel = point_dict[point]['Velocity']
        acc = point_dict[point]['Accel']
        distance = calc_distance(pos)

        if distance < min_dist:
            min_dist = distance
            min_point = point

        pos_new, vel_new = calc_attributes(pos, vel, acc)

        point_dict.update({point: {'Position': pos_new, 'Velocity': vel_new, 'Accel': acc}})
        pos_check.update({point: pos_new})


    keys = set()
    for key1 in pos_check:
        for key2 in pos_check:
            if key1 == key2: continue
            if pos_check[key1] == pos_check[key2]:
                keys |= {key1, key2}

    for key in keys:
        point_dict.pop(key)

particles_left = len(point_dict)

print('Part 2 Answer:', particles_left)