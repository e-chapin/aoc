import re

wires = dict()
values = dict()

with open('input.txt') as f:
    lines = f.readlines()


for line in lines:
    op, destination = line.strip('\n').split(' -> ')
    wires[destination] = op.strip()


def calculate(wire):

    try:
        return int(wire)
    except ValueError:
        pass

    if wire in values:
        return values[wire]

    gate = wires[wire].split(' ')
    # handle 123 -> x, gate would be '123'
    if len(gate) == 1:
        return calculate(gate[0])

    if gate[0] == 'NOT':
        values[wire] = ~ calculate(gate[1])
    elif gate[1] == 'AND':
        values[wire] = calculate(gate[0]) & calculate(gate[2])
    elif gate[1] == 'OR':
        values[wire] = calculate(gate[0]) | calculate(gate[2])
    elif gate[1] == 'LSHIFT':
        values[wire] = calculate(gate[0]) << calculate(gate[2])
    elif gate[1] == 'RSHIFT':
        values[wire] = calculate(gate[0]) >> calculate(gate[2])

    return values[wire]


print("2015 Day 6 Part 1")
p1 = calculate('a')
print(p1)

wires['b'] = str(p1)
values = dict()
print("2015 Day 6 Part 2")
print(calculate('a'))