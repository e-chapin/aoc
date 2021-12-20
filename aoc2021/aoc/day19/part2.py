# Advent of Code - Day 19 - Part Two

from part1 import *


def distance(coord_a, coord_b):
    a, b, c = coord_a
    x, y, z = coord_b

    return abs(a - x) + abs(b - y) + abs(c - z)


def result(data):
    data = list(map(parse, data.split('\n\n')))
    matches = match_beacons(data)

    max_distance = 0
    distances = [x[1] for x in matches]
    for a in distances:
        for b in distances:
            max_distance = max(distance(a, b), max_distance)
    return max_distance

