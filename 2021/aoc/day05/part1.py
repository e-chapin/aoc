# Advent of Code - Day 5 - Part One

from collections import defaultdict


def result(data):

    points = defaultdict(int)

    for line in data:
        a, b = line.split(' -> ')
        x1, y1 = a.split(',')
        x2, y2 = b.split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        min_x, max_x = min(x1,x2), max(x1,x2)
        min_y, max_y = min(y1, y2), max(y1,y2)

        if min_x == max_x or min_y == max_y:
            for x in range(min_x, max_x+1):
                for y in range(min_y, max_y+1):
                    points[(x,y)] += 1

    count = 0
    for k in points.keys():
        if points[k] > 1:
            count += 1

    return count
