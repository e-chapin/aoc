# Advent of Code - Day 6 - Part One

from collections import defaultdict


def result(data):
    fish = list(map(int, data[0].split(',')))
    fishes = defaultdict(int)
    for f in fish:
        fishes[f] += 1

    for _ in range(80):
        new_fishes = defaultdict(int)
        for i, f in fishes.items():
            if i == 0:
                new_fishes[6] += f
                new_fishes[8] += f
            else:
                new_fishes[i-1] += f
        fishes = new_fishes

    return sum(fishes.values())
