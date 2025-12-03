import requests
import math
from copy import deepcopy
from sys import maxsize

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_22_input.txt'

resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

def sim(enemy_HP, enemy_damage, self_HP, current_mana, active_spells, my_turn, total_mana_used):

    new_active_spells = []
    current_armor = 0

    for active_spell in active_spells:
        spell_cast = active_spell[0]
        spell_count = active_spell[1]

        enemy_HP -= spells[spell_cast]['damage']
        self_HP += spells[spell_cast]['heal']
        current_mana += spells[spell_cast]['recharge']
        current_armor += spells[spell_cast]['armor']
        if spell_count > 0:
            new_active_spells.append((spell_cast, (spell_count - 1)))

    if enemy_HP <= 0:
        global min_total_mana
        if total_mana_used < min_total_mana:
            min_total_mana = total_mana_used
        return True

    if total_mana_used >= min_total_mana:
        return False

    if my_turn:
        for spell in spells:
            active_flag = False
            for new_active_spell in new_active_spells:
                if new_active_spell[0] == spell:
                    active_flag = True
                    break
            spell_cost = spells[spell]['cost']
            if (spell_cost <= current_mana) and not active_flag:
                a = deepcopy(new_active_spells)
                a.append((spell, spells[spell]['turns'] - 1))
                my_turn = False
                sim(enemy_HP, enemy_damage, self_HP, current_mana - spell_cost, a, my_turn, total_mana_used + spell_cost)
    else:
        self_HP += current_armor - enemy_damage if current_armor - enemy_damage < 0 else -1
        if self_HP > 0:
            my_turn = True
            sim(enemy_HP, enemy_damage, self_HP, current_mana, new_active_spells, my_turn, total_mana_used)

self_HP = 50
enemy_HP = int(input_text[0].split(' ')[2])
enemy_damage = int(input_text[1].split(' ')[1])
current_mana = 500
min_total_mana = math.inf

spells = {
    'mm': {'cost': 53, 'damage': 4, 'heal': 0, 'armor': 0, 'recharge': 0, 'turns': 0},
    'drain': {'cost': 73, 'damage': 2, 'heal': 2, 'armor': 0, 'recharge': 0, 'turns': 0},
    'shield': {'cost': 113, 'damage': 0, 'heal': 0, 'armor': 7, 'recharge': 0, 'turns': 6},
    'poison': {'cost': 173, 'damage': 3, 'heal': 0, 'armor': 0, 'recharge': 0, 'turns': 6},
    'recharge': {'cost': 229, 'damage': 0, 'heal': 0, 'armor': 0, 'recharge': 101, 'turns': 5}
}

active_spells = []
my_turn = True
total_mana_used = 0

sim(enemy_HP, enemy_damage, self_HP, current_mana, active_spells, my_turn, total_mana_used)

print('Part 1 Answer:', min_total_mana)

# Part 2

def sim2(enemy_HP, enemy_damage, self_HP, current_mana, active_spells, my_turn, total_mana_used):
    new_active_spells = []
    current_armor = 0

    if my_turn:
        self_HP -= 1
        if self_HP <= 0:
            return False

    for active_spell in active_spells:
        spell_cast = active_spell[0]
        spell_count = active_spell[1]

        enemy_HP -= spells[spell_cast]['damage']
        self_HP += spells[spell_cast]['heal']
        current_mana += spells[spell_cast]['recharge']
        current_armor += spells[spell_cast]['armor']
        if spell_count > 0:
            new_active_spells.append((spell_cast, (spell_count - 1)))

    if enemy_HP <= 0:
        global min_total_mana
        if total_mana_used < min_total_mana:
            min_total_mana = total_mana_used
        return True

    if total_mana_used >= min_total_mana:
        return False

    if my_turn:
        for spell in spells:
            active_flag = False
            for new_active_spell in new_active_spells:
                if new_active_spell[0] == spell:
                    active_flag = True
                    break
            spell_cost = spells[spell]['cost']
            if (spell_cost <= current_mana) and not active_flag:
                a = deepcopy(new_active_spells)
                a.append((spell, spells[spell]['turns'] - 1))
                my_turn = False
                sim2(enemy_HP, enemy_damage, self_HP, current_mana - spell_cost, a, my_turn, total_mana_used + spell_cost)
    else:
        self_HP += current_armor - enemy_damage if current_armor - enemy_damage < 0 else -1
        if self_HP > 0:
            my_turn = True
            sim2(enemy_HP, enemy_damage, self_HP, current_mana, new_active_spells, my_turn, total_mana_used)

self_HP = 50
enemy_HP = int(input_text[0].split(' ')[2])
current_mana = 500
min_total_mana = math.inf
active_spells = []
my_turn = True
total_mana_used = 0

sim2(enemy_HP, enemy_damage, self_HP, current_mana, active_spells, my_turn, total_mana_used)

print('Part 2 Answer:', min_total_mana)

