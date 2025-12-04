import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2016/Inputs/aoc_2016_3_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

triangle_list = []

for row in input_text:
    line = row.split(' ')
    triangle = []
    for element in line:
        if element != '':
            triangle.append(int(element))
    triangle_list.append(triangle)

possible_num = 0

for triangle in triangle_list:
    if (triangle[0] + triangle[1] > triangle[2]) and (triangle[2] + triangle[1] > triangle[0]) and (triangle[0] + triangle[2] > triangle[1]):
        possible_num += 1

print('Part 1 Answer:', possible_num)

# Part 2

tri1 = []
tri2 = []
tri3 = []

for row in input_text:
    line = row.split(' ')
    for element in line:
        if element != '':
            if len(tri1) == len(tri2) and len(tri1) == len(tri3):
                tri1.append(int(element))
            elif len(tri2) == len(tri3):
                tri2.append(int(element))
            else:
                tri3.append(int(element))

element_list = []

element_list.extend(tri1)
element_list.extend(tri2)
element_list.extend(tri3)

triangle_list = []
triangle = []

side = 0

for element in element_list:
    if side < 3:
        triangle.append(element)
        side += 1
    else:
        triangle_list.append(triangle)
        triangle = []
        triangle.append(element)
        side = 1

triangle_list.append(triangle)

possible_num = 0

for triangle in triangle_list:
    if (triangle[0] + triangle[1] > triangle[2]) and (triangle[2] + triangle[1] > triangle[0]) and (triangle[0] + triangle[2] > triangle[1]):
        possible_num += 1

print('Part 2 Answer:', possible_num)
