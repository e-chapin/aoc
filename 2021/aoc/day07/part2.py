# Advent of Code - Day 7 - Part One

from collections import defaultdict
from defaultlist import defaultlist

def result(data):

    crabs = list(map(int, data[0].split(',')))

    m = max(crabs)
    lowest = None
    for i in range(m):
        total = 0
        for crab in crabs:
            a, b = max(crab, i), min(crab, i)
            n = a-b
            total += (n*(n+1))/2
            if lowest and total > lowest:
                continue
        if not lowest or total < lowest:
            lowest = int(total)
    return lowest  # 98925151


