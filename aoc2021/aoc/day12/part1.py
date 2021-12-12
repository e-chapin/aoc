# Advent of Code - Day 12 - Part One

from collections import defaultdict

connections = defaultdict(list)


def traverse(node, seen):
    if node == 'end':
        return 1
    if node in seen:
        if node == 'start':
            return 0
        if node.islower():
            return 0
    return sum(traverse(n, seen+[node]) for n in connections[node])


def result(data):

    for link in data:
        a, b = link.split('-')
        connections[a].append(b)
        connections[b].append(a)

    return traverse('start', [])
