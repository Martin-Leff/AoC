import collections

import requests
import operator
import networkx as nx
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2017/Inputs/aoc_2017_7_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

top_list = []
bottom_list = []

for line in input_text:
    if '->' in line:
        bottom_list.append(line)
    else:
        top_list.append(line)

holding_list = []
held_list = []

for row in bottom_list:
    holding = row.split('(')[0].strip(' ')
    holding_list.append(holding)
    held_temp = row.split('>')[1].split(',')
    for held_item in held_temp:
        held_item_stripped = held_item.strip(' ')
        if held_item_stripped not in held_list:
            held_list.append(held_item_stripped)

bottom = ''

for item in holding_list:
    if item not in held_list:
        bottom = item

print('Part 1 Answer:', bottom)

# Part 2

G = nx.DiGraph()

for line in input_text:
    if '->' in line:
        base = line.split('->')[0]
        base_weight = int(base.split('(')[1].strip(') '))
        base = base.split('(')[0].strip(' ')
        children_list = line.split('->')[1].strip(' ').split(',')
        children_list = [x.strip() for x in children_list]
        G.add_node(base, weight=base_weight)
        for child in children_list:
            G.add_edge(base, child)
    else:
        node_weight = int(line.split('(')[1].strip(') '))
        node = line.split('(')[0].strip(' ')
        G.add_node(node, weight=node_weight)

ordered = list(nx.topological_sort(G))

weights = {}

for node in reversed(ordered):
    total = G.nodes[node]['weight']
    print(node, total)
    count = collections.Counter(weights[child] for child in G[node])
    unbal = None

    for child in G[node]:
        if len(count) > 1 and count[weights[child]] == 1:
            unbal = child
            break

        val = weights[child]
        total += val


