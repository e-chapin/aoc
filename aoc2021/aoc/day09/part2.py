# Advent of Code - Day 9 - Part Two

from collections import defaultdict

seen = defaultdict(int)
points = dict()


def check_basin(x, y):
    point = points.get((x, y), 9)
    if point == 9 or seen[(x, y)] == 1:
        return 0

    else:
        seen[(x, y)] = 1
        return 1 + check_basin(x + 1, y) + check_basin(x - 1, y) + check_basin(x, y + 1) + check_basin(x, y - 1)


def result(data):

    for x, line in enumerate(data):
        for y, c in enumerate(line):
            points[(x, y)] = int(c)

    max_x, max_y = len(data), len(data[0])
    basins = []
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
                basins.append(check_basin(x, y))

    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]