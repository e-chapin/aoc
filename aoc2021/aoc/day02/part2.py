# Advent of Code - Day 2 - Part Two

def result(data):
    horizontal, vertical, aim = 0, 0, 0

    for line in data:
        direction, i = line.split(' ')
        i = int(i)
        if direction == 'forward':
            horizontal += i
            vertical += aim*i
        if direction == 'up':
            aim -= i
        if direction == 'down':
            aim += i

    return horizontal*vertical
