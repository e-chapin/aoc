# Advent of Code - Day 12 - Part Two

from collections import defaultdict

connections = defaultdict(list)


def traverse(node, seen, part=2):
    if node == 'end':
        return 1
    if node in seen:
        if node == 'start':
            return 0
        if node.islower():
            if part == 1:
                return 0
            else:
                part = 1
    return sum(traverse(n, seen+[node], part) for n in connections[node])


def result(data):

    for link in data:
        a, b = link.split('-')
        connections[a].append(b)
        connections[b].append(a)

    return traverse('start', [])
