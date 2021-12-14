# Advent of Code - Day 14 - Part Two

from collections import defaultdict


def result(data):

    template = data.pop(0)
    insertions = dict(rule.split(' -> ') for rule in data[1:])

    count = defaultdict(int)
    for i in range(len(template) - 1):
        count[template[i: i + 2]] += 1

    for _ in range(40):
        next_counts = defaultdict(int)
        for key, value in count.items():
            next_counts[key[0] + insertions[key]] += value
            next_counts[insertions[key] + key[1]] += value
        count = next_counts

    final = defaultdict(int)
    for key, value in count.items():
        final[key[0]] += value
    final[template[-1]] += 1

    return max(final.values()) - min(final.values())


# 2188189693529