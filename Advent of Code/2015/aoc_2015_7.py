import requests

url = 'https://raw.githubusercontent.com/Martin-Leff/AoC/refs/heads/main/Advent%20of%20Code/2015/Inputs/aoc_2015_7_input.txt'
resp = requests.get(url)
input_text = resp.text
input_text = input_text.splitlines()

# Part 1

calc = dict()
results = dict()

for command in input_text:
    operators, result = command.split('->')
    calc[result.strip()] = operators.strip().split(' ')

def calculate(wire):
    try:
        return int(wire)
    except ValueError:
        pass

    if wire not in results:
        ops = calc[wire]
        if len(ops) == 1:
            result = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'OR':
                result = calculate(ops[0]) | calculate(ops[2])
            elif op == 'AND':
                result = calculate(ops[0]) & calculate(ops[2])
            elif op == 'LSHIFT':
                result = calculate(ops[0]) << calculate(ops[2])
            elif op == 'RSHIFT':
                result = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'NOT':
                result = ~calculate(ops[1]) & 0xffff
        results[wire] = result
    return results[wire]

a_res = calculate('a')

print('Part 1 Answer:', a_res)

# Part 2

calc = dict()
results = dict()

for command in input_text:
    operators, result = command.split('->')
    calc[result.strip()] = operators.strip().split(' ')

results['b'] = a_res

a_res_2 = calculate('a')

print('Part 2 Answer:', a_res_2)