import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_2_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def surface_area(l, w, h):
    s1 = l * w
    s2 = h * w
    s3 = l * h
    smallest = min(s1, s2, s3)
    surface_area_total = (2 * (s1 + s2 + s3)) + smallest
    return surface_area_total

def parse_dimensions(line_string):
    l, w, h = line_string.split('x')
    return int(l), int(w), int(h)

total = 0

for string in input_text:
    l, w, h = parse_dimensions(string)
    surface_area_total = surface_area(l, w, h)
    total += surface_area_total

print('Part 1 Answer:', total)

# Part 2

def perimeter(l, w, h):
    p1 = 2 * (l + w)
    p2 = 2 * (l + h)
    p3 = 2 * (h + w)
    perim = min(p1, p2, p3)

    return perim

def volume(l, w, h):
    volume = l * w * h
    return volume

bow_total = 0

for string in input_text:
    l, w, h = parse_dimensions(string)
    perim = perimeter(l, w, h)
    bow = volume(l, w, h)
    ribbon_total = perim + bow
    bow_total += ribbon_total

print('Part 2 Answer:', bow_total)
