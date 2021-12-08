# Advent of Code - Day 7 - Part One

from collections import defaultdict
from defaultlist import defaultlist

def result(data):

    crabs = list(map(int, data[0].split(',')))

    m = max(crabs)
    lowest = 9999999
    for i in range(m):
        total = 0
        for crab in crabs:
            a, b = max(crab, i), min(crab, i)
            total += a-b
        if total < lowest:
            lowest = total
    return lowest
