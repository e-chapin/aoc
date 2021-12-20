# Advent of Code - Day 19 - Part One


def parse(data):
    signals = []
    for line in data.split('\n')[1:]:
        x, y, z = line.split(",")
        x, y, z = int(x), int(y), int(z)
        signals.append((x, y, z))
    return signals


def permute(coords):
    x, y, z = coords
    
    yield (+x, +y, +z)
    yield (+y, +z, +x)
    yield (+z, +x, +y)
    yield (+z, +y, -x)
    yield (+y, +x, -z)
    yield (+x, +z, -y)

    yield (+x, -y, -z)
    yield (+y, -z, -x)
    yield (+z, -x, -y)
    yield (+z, -y, +x)
    yield (+y, -x, +z)
    yield (+x, -z, +y)

    yield (-x, +y, -z)
    yield (-y, +z, -x)
    yield (-z, +x, -y)
    yield (-z, +y, +x)
    yield (-y, +x, +z)
    yield (-x, +z, +y)

    yield (-x, -y, +z)
    yield (-y, -z, +x)
    yield (-z, -x, +y)
    yield (-z, -y, -x)
    yield (-y, -x, -z)
    yield (-x, -z, -y)


def orients(beacon):
    yield from zip(*(permute(coords) for coords in beacon))


def check_match(coord_a, coord_b, offset):
    for reference in coord_a:
        x, y, z = reference
        for orientation in orients(coord_b):
            for other in orientation:
                a, b, c = other
                shift = (x - a, y - b, z - c)
                if check_shift(coord_a, orientation, shift):
                    if offset != (0, 0, 0):
                        translated_offset = (offset[0]+shift[0], offset[1]+shift[1], offset[2]+shift[2])
                    else:
                        translated_offset = shift
                    return orientation, translated_offset
    return False, False


def check_shift(coord_a, coord_b, shift):
    dx, dy, dz = shift
    count = 0
    for ca in coord_a:
        x, y, z = ca
        for cb in coord_b:
            a, b, c = cb
            if a+dx == x and b+dy == y and c+dz == z:
                count += 1
            if count > 11:
                return True
    return False


def match_beacons(beacons):
    first = beacons.pop(0)
    matches = [(first, (0, 0, 0))]
    i = 0
    while len(beacons):
        if i >= len(beacons):
            i = 0
        for match in matches:
            orientation, offset = check_match(match[0], beacons[i], match[1])
            if orientation:
                matches.append((orientation, offset))
                del beacons[i]
                break
        i += 1

    return matches


def result(data):
    data = list(map(parse, data.split('\n\n')))
    matches = match_beacons(data)
    found = set()
    for match in matches:
        beacons, offset = match
        dx, dy, dz = offset
        for beacon in beacons:
            x, y, z = beacon
            a, b, c = x+dx, y+dy, z+dz
            found.add((a, b, c))

    return len(found)
