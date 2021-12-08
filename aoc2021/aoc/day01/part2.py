# Advent of Code - Day 1 - Part Two

def result(data):
    count = 0
    for i, line in enumerate(data):
        if i > 2:
            try:
                current = int(data[i - 2]) + int(data[i - 1]) + int(data[i])
                prev = int(data[i - 3]) + int(data[i - 2]) + int(data[i - 1])
                if current > prev:
                    count += 1
            except IndexError:
                return count
    return count
