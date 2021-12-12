# Advent of Code - Day 11 - Part Two

def result(data):

    octs = {}

    def neighbours(x, y):
        r = []
        coords = [(x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1)]
        for c in coords:
            oct = octs.get(c, 0)
            if oct:
                r.append(c)
        return r


    for x, line in enumerate(data):
        for y, energy in enumerate(line):
            octs[(x, y)] = int(energy)

    flashes = 0
    step = 0
    while True:
        step += 1
        for o in octs:
            octs[o] += 1
        flashing = {o for o in octs if octs[o] > 9}

        while flashing:
            f = flashing.pop()
            octs[f] = 0
            flashes += 1
            for n in neighbours(*f):
                octs[n] += 1
                if octs[n] > 9:
                    flashing.add(n)

        if sum(octs.values()) == 0:
            return step
