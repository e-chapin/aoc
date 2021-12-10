# Advent of Code - Day 10 - Part Two

def result(data):

    pairs = {
        ')': {'open': '(', 'score': 1},
        ']': {'open': '[', 'score': 2},
        '}': {'open': '{', 'score': 3},
        '>': {'open': '<', 'score': 4}
    }
    opens = [o['open'] for o in pairs.values()]
    points = {o.get('open'): o.get('score') for o in pairs.values()}

    scores = []
    for line in data:
        stack = []
        corrupt = False
        for c in line:
            if c in opens:
                stack.append(c)
            elif c in pairs.keys():
                last_open = stack.pop()
                if pairs.get(c).get('open') != last_open:
                    corrupt = True
                    break
        if not corrupt:
            score = 0
            stack.reverse()
            for x in stack:
                score = 5*score + points.get(x)
            scores.append(score)

    scores.sort()
    return scores[int((len(scores) - 1)/2)]
