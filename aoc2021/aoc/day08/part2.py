# Advent of Code - Day 8 - Part Two

def result(data):

    digits = {
        2: 1,
        4: 4,
        3: 7,
        7: 8
    }

    count = 0
    for line in data:
        a, b = line.split(' | ')
        for word in b.split(' '):
            x = len(word)
            if digits.get(x):
                count += 1

    return count
