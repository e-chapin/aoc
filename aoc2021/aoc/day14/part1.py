# Advent of Code - Day 14 - Part One

from collections import defaultdict


def result(data):

    count = defaultdict(int)

    template = data.pop(0)
    insertions = dict(rule.split(' -> ') for rule in data[1:])
    for _ in range(10):
        t = []
        new = ''
        for i in range(len(template)-1):
            t.append(template[i:i+2])
        for j, pair in enumerate(t):
            ins = insertions.get(pair)
            new += pair[0] + ins
            if j == len(t)-1:
                new += pair[1]
        template = new

    for c in template:
        count[c] += 1
    return max(count.values()) - min(count.values())
