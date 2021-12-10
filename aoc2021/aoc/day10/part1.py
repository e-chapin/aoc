# Advent of Code - Day 10 - Part One

def result(data):

    pairs = {
        ')': {'open': '(', 'score': 3},
        ']': {'open': '[', 'score': 57},
        '}': {'open': '{', 'score': 1197},
        '>': {'open': '<', 'score': 25137}
    }
    opens = [o['open'] for o in pairs.values()]
    stack = []
    score = 0
    for line in data:
        for c in line:
            if c in opens:
                stack.append(c)
            elif c in pairs:
                last_open = stack.pop()
                if pairs[c] != last_open:
                    score += pairs[c]['score']
                    continue
    return score
