# Advent of Code - Day 1 - Part One

def result(data):
    count = 0
    for i, line in enumerate(data):
        if i > 0:
            line, prev = int(line), int(data[i-1])
            if line > prev:
                count += 1
    return count
