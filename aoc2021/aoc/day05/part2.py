
# Advent of Code - Day 5 - Part Two

from collections import defaultdict


def result(data):

    lines = []
    for d in data:
        a, b = d.split(' -> ')
        x, y = a.split(','), b.split(',')
        lines.append(((int(x[0]), int(x[1])), (int(y[0]), int(y[1]))))

    grid = defaultdict(int)

    for line in lines:
        (x1, y1), (x2, y2) = line

        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2 + 1):
                grid[(x1, y)] += 1
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2 + 1):
                grid[(x, y1)] += 1
        else:
            x1_, x2_ = min(x1, x2), max(x1, x2)
            y1_, y2_ = min(y1, y2), max(y1, y2)

            r = (x2_ - x1_) + 1

            if (x1 < x2) and (y1 < y2):
                for d in range(r):
                    grid[(x1_ + d, y1_ + d)] += 1
            elif (x1 > x2) and (y1 < y2):
                for d in range(r):
                    grid[(x2_ - d, y1_ + d)] += 1
            elif (x1 < x2) and (y1 > y2):
                for d in range(r):
                    grid[(x1_ + d, y2_ - d)] += 1
            else:
                for d in range(r):
                    grid[(x2_ - d, y2_ - d)] += 1
    z = 0
    for y in grid.values():
        if y > 1:
            z += 1


    return z

