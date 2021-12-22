# Advent of Code - Day 22 - Part Two


def get_instructions(data):

    def get_range(t):
        t = t.split('=')[1].split('..')
        return range(int(t[0]), int(t[1])+1)

    for line in data:
        onoff, coords = line.split(' ')
        x, y, z = coords.split(',')
        yield onoff, get_range(x), get_range(y), get_range(z)
    

def get_overlap(a, b):

    if a.stop <= b.start or a.start >= b.stop:
        return range(0)
    return range(max(a.start, b.start), min(a.stop, b.stop))


def do_instructions(instruction, remaining):

    _, xrange, yrange, zrange = instruction

    total = len(xrange)*len(yrange)*len(zrange)

    conflicts = []

    c = (xrange, yrange, zrange)
    for r in remaining:

        xr = get_overlap(c[0], r[1])
        yr = get_overlap(c[1], r[2])
        zr = get_overlap(c[2], r[3])

        if len(xr) == 0 or len(yr) == 0 or len(zr) == 0:
            continue

        conflicts.append((_, xr, yr, zr))

    for i, item in enumerate(conflicts):
        # conflicts either overlap and will be turn on in the future instruction
        # or they turn off, so remove from total
        total -= do_instructions(item, conflicts[i+1:])

    return total


def result(data):

    instructions = list(get_instructions(data))
    total = 0
    for i, instruction in enumerate(instructions):
        if instruction[0] == 'off':
            continue  # don't care about counting ones that are turned off, yet.
        total += do_instructions(instruction, instructions[i+1:])

    return total
