# Advent of Code - Davertical 2 - Part One


def result(data):
    horizontal, vertical = 0, 0

    for line in data:
        direction, i = line.split(' ')
        i = int(i)
        if direction == 'forward':
            horizontal += i
        if direction == 'up':
            vertical -= i
        if direction == 'down':
            vertical += i

    return horizontal*vertical
