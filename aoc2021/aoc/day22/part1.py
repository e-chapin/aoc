# Advent of Code - Day 22 - Part One

from collections import defaultdict


def do_instruction(instruction, cubes):

    onoff, xrange, yrange, zrange = instruction
    for x in xrange:
        if x < -50 or x > 50:
            continue
        for y in yrange:
            if y < -50 or y > 50:
                continue
            for z in zrange:
                if z < -50 or z > 50:
                    continue
                if (x, y, z) not in cubes.keys():
                    pass
                else:
                    cubes[(x, y, z)] = 1 if onoff else 0
    else:
        pass


def get_instruction(line):
    # on x=36365..49950,y=-70986..-41449,z=16562..51419
    onoff, coords = line.split(' ')
    onoff = onoff == 'on'
    x, y, z = coords.split(',')
    x = x.lstrip('x=').split('..')
    y = y.lstrip('y=').split('..')
    z = z.lstrip('z=').split('..')
    xrange = [xr for xr in range(int(x[0]), int(x[1])+1)]
    yrange = [yr for yr in range(int(y[0]), int(y[1]) + 1)]
    zrange = [yr for yr in range(int(z[0]), int(z[1]) + 1)]
    return onoff, xrange, yrange, zrange


def count_cubes(cubes):
    return sum([x for x in cubes.values() if x == 1])


def result(data):

    # cubes = defaultdict(int)
    #
    # for x in range(-50, 51):
    #     for y in range(-50, 51):
    #         for z in range(-50, 51):
    #             cubes[(x, y, z)] = 0
    #
    # for line in data:
    #     instruction = get_instruction(line)
    #     do_instruction(instruction, cubes)
    #
    # return count_cubes(cubes)

    return 'done'
