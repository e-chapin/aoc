# Advent of Code - Day 3 - Part One

from defaultlist import  defaultlist


def result(data):

    positions = defaultlist(int)

    for line in data:
        for i, c in enumerate(line):
            if c == '1':
                positions[i] += 1

    a = ''
    b = ''
    for row in positions:
        if row > len(data)/2:
            a += '0'
            b += '1'
        else:
            a += '1'
            b += '0'

    return int(a, 2) * int(b, 2)

    # 3813416