# Advent of Code - Day 18 - Part One

import math
#
#


def parse(inpt):
    inpt = inpt.replace('[', '[,').replace(']', ',]')
    inpt = inpt.split(',')
    return [int(c) if c.isnumeric() else c for c in inpt]


def add(a, b):
    return ['['] + a + b + [']']


def check_explode(element):
    depth = 0
    last_num_idx = False
    for pos in range(len(element)):
        if element[pos] == ']':
            depth -= 1
        elif element[pos] == '[':
            depth += 1
            if depth >= 5:
                exploded_left = element[pos + 1]
                exploded_right = element[pos + 2]
                next_num_idx = False
                for g in range(pos + 3, len(element)):
                    if isinstance(element[g], int):
                        element[g] += exploded_right
                        break
                if last_num_idx:
                    element[last_num_idx] += exploded_left
                for x in range(4):
                    del element[pos]
                element.insert(pos, 0)
                return True
        elif isinstance(element[pos], int):
            last_num_idx = pos
    return False


def check_split(element):
    for i in range(len(element)):
        e = element[i]
        if isinstance(e, int) and e >= 10:
            element.insert(i+1, ']')
            element.insert(i+1, math.ceil(e / 2))
            element.insert(i+1, e // 2)
            element[i] = '['
            return True
    return False


def reduce(element):
    while check_explode(element) or check_split(element):
        continue
    return element


def magnitude(element):

    # pair of ints?.
    if isinstance(element[0], int):
        return element[0], element[1:]

    # otherwise recurse deeper
    if element[0] == '[':
        left, rest = magnitude(element[1:])
        right, rest = magnitude(rest)
        return 3*left + 2*right, rest[1:]


def result(data):

    exprs = [parse(l.strip()) for l in data]

    total = exprs[0]
    for expr in exprs[1:]:
        total = add(total, expr)
        reduce(total)
    mag, _ = magnitude(total)

    return mag

    return 'done'
