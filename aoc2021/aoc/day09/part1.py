# Advent of Code - Day 9 - Part One

from collections import defaultdict

def result(data):

    points = defaultdict(int)
    for x, line in enumerate(data):
        for y, c in enumerate(line):
            points[(x, y)] = int(c)

    max_y = len(data[0])
    max_x = len(data)

    risk = 0
    for x in range(max_x):
        for y in range(max_y):
            point = points[(x, y)]
            low_point = True
            if points.get((x+1, y), 99) <= point:
                low_point = False
            elif points.get((x, y+1), 99) <= point:
                low_point = False
            elif points.get((x, y - 1), 99) <= point:
                low_point = False
            elif points.get((x-1, y), 99) <= point:
                low_point = False
            if low_point:
                risk += 1+point


    return risk
