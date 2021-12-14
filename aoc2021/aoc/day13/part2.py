# Advent of Code - Day 13 - Part Two

from collections import defaultdict


def result(data):

    max_x, max_y  = 0, 0

    paper = defaultdict(int)
    folds = []
    for i, line in enumerate(data):
        if not line:
            folds = data[i+1:]
            break
        x, y = line.split(',')
        x, y = int(x), int(y)
        paper[(x, y)] = 1
        max_x, max_y = max(x, max_x), max(y, max_y)


    while folds:

        fold = folds.pop(0)

        axis, line = fold.lstrip('fold along ').split('=')
        line = int(line)

        folded = defaultdict(int)
        if axis == 'y':
            y = line+1
            ydiff = 2
            while y <= max_y:
                x = 0
                while x <= max_x:
                    x2, y2 = x, y-ydiff
                    folded[(x2, y2)] = max(paper[(x, y)], paper[(x2, y2)])
                    x += 1
                ydiff += 2
                y += 1

        else:
            x = line+1
            xdiff = 2
            while x <= max_x:
                y = 0
                while y <= max_y:
                    x2, y2 = x-xdiff, y
                    folded[(x2, y2)] = max(paper[(x, y)], paper[(x2, y2)])
                    y += 1
                xdiff += 2
                x += 1
        paper = folded

    max_y = 6
    max_x = 40
    # for x, y in paper.keys():
    #     max_x, max_y = max(x, max_x), max(y, max_y)

    line = '\n'
    for y in range(max_y):
        for x in range(max_x):
            line += '#' if paper[(x,y)] == 1 else '.'
        line += '\n'

    return line
