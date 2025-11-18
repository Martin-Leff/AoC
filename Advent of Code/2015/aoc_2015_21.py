import requests
import math

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_21_input.txt'

resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

self_HP = 100

enemy_HP = int(input_text[0].split(' ')[2])
enemy_damage = int(input_text[1].split(' ')[1])
enemy_armor = int(input_text[2].split(' ')[1])

shop_weapons = {
    'dagger': {'cost': 8, 'damage': 4, 'armor': 0},
    'shortsword': {'cost': 10, 'damage': 5, 'armor': 0},
    'warhammer': {'cost': 25, 'damage': 6, 'armor': 0},
    'longsword': {'cost': 40, 'damage': 7, 'armor': 0},
    'greataxe': {'cost': 74, 'damage': 8, 'armor': 0}
}

shop_armor = {
    'none': {'cost': 0, 'damage': 0, 'armor': 0},
    'leather': {'cost': 13, 'damage': 0, 'armor': 1},
    'chainmail': {'cost': 31, 'damage': 0, 'armor': 2},
    'splintmail': {'cost': 53, 'damage': 0, 'armor': 3},
    'bandedmail': {'cost': 75, 'damage': 0, 'armor': 4},
    'platemail': {'cost': 102, 'damage': 0, 'armor': 5}
}

shop_rings = {
    'none_left': {'cost': 0, 'damage': 0, 'armor': 0},
    'none_right': {'cost': 0, 'damage': 0, 'armor': 0},
    'damage 1': {'cost': 25, 'damage': 1, 'armor': 0},
    'damage 2': {'cost': 50, 'damage': 2, 'armor': 0},
    'damage 3': {'cost': 100, 'damage': 3, 'armor': 0},
    'defense 1': {'cost': 20, 'damage': 0, 'armor': 1},
    'defense 2': {'cost': 40, 'damage': 0, 'armor': 2},
    'defense 3': {'cost': 80, 'damage': 0, 'armor': 3}
}

min_cost = math.inf

for weapon in shop_weapons:
    w_cost = shop_weapons[weapon]['cost']
    w_damage = shop_weapons[weapon]['damage']
    w_armor = shop_weapons[weapon]['armor']
    for armor in shop_armor:
        a_cost = shop_armor[armor]['cost']
        a_damage = shop_armor[armor]['damage']
        a_armor = shop_armor[armor]['armor']
        for ring_1 in shop_rings:
            r1_cost = shop_rings[ring_1]['cost']
            r1_damage = shop_rings[ring_1]['damage']
            r1_armor = shop_rings[ring_1]['armor']
            for ring_2 in shop_rings:
                if ring_1 == ring_2:
                    break
                r2_cost = shop_rings[ring_2]['cost']
                r2_damage = shop_rings[ring_2]['damage']
                r2_armor = shop_rings[ring_2]['armor']
                total_cost = w_cost + a_cost + r1_cost + r2_cost
                total_armor = w_armor + a_armor + r1_armor + r2_armor
                total_damage = w_damage + a_damage + r1_damage + r2_damage

                if (total_damage - enemy_armor) <= 0:
                    attack = 1
                else:
                    attack = total_damage - enemy_armor

                if (enemy_damage - total_armor) <= 0:
                    defense = 1
                else:
                    defense = enemy_damage - total_armor

                enemy_turns = math.ceil(enemy_HP / attack)
                self_turns = math.ceil(self_HP / defense)

                if self_turns >= enemy_turns:
                    if total_cost < min_cost:
                        min_cost = total_cost

print('Part 1 Answer:', min_cost)

# Part 2

max_cost = 0

for weapon in shop_weapons:
    w_cost = shop_weapons[weapon]['cost']
    w_damage = shop_weapons[weapon]['damage']
    w_armor = shop_weapons[weapon]['armor']
    for armor in shop_armor:
        a_cost = shop_armor[armor]['cost']
        a_damage = shop_armor[armor]['damage']
        a_armor = shop_armor[armor]['armor']
        for ring_1 in shop_rings:
            r1_cost = shop_rings[ring_1]['cost']
            r1_damage = shop_rings[ring_1]['damage']
            r1_armor = shop_rings[ring_1]['armor']
            for ring_2 in shop_rings:
                if ring_1 == ring_2:
                    break
                r2_cost = shop_rings[ring_2]['cost']
                r2_damage = shop_rings[ring_2]['damage']
                r2_armor = shop_rings[ring_2]['armor']
                total_cost = w_cost + a_cost + r1_cost + r2_cost
                total_armor = w_armor + a_armor + r1_armor + r2_armor
                total_damage = w_damage + a_damage + r1_damage + r2_damage

                if (total_damage - enemy_armor) <= 0:
                    attack = 1
                else:
                    attack = total_damage - enemy_armor

                if (enemy_damage - total_armor) <= 0:
                    defense = 1
                else:
                    defense = enemy_damage - total_armor

                enemy_turns = math.ceil(enemy_HP / attack)
                self_turns = math.ceil(self_HP / defense)

                if self_turns < enemy_turns:
                    if total_cost > max_cost:
                        max_cost = total_cost

print('Part 2 Answer:', max_cost)