import collections

import requests
import networkx as nx

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
    name = line.split()[0]

    G.add_node(name, weight=int(line.split()[1].strip('()')))

    if '->' in line:
        children = [n.strip() for n in line.split('->')[1].split(',')]

        for child in children:
            G.add_edge(name, child)

ordered = list(nx.topological_sort(G))

weights = {}

answer_weight = 0

for node in reversed(ordered):
    total = G.nodes[node]['weight']

    counts = collections.Counter(weights[child] for child in G[node])
    unbal = None
    val = 0

    for child in G[node]:
        if len(counts) > 1 and counts[weights[child]] == 1:
            unbal = child
            break

        val = weights[child]
        total += weights[child]

    if unbal:
        diff = weights[unbal] - val
        answer_weight = G.nodes[unbal]['weight'] - diff
        break

    weights[node] = total

print('Part 2 Answer:', answer_weight)

