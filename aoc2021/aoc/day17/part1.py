# Advent of Code - Day 17 - Part One

from collections import defaultdict


def step(coord, velocity):
    # The probe's x position increases by its x velocity.
    # The probe's y position increases by its y velocity.
    # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is
    #   greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
    # Due to gravity, the probe's y velocity decreases by 1.

    x, y = coord
    xd, yd = velocity
    x += xd
    y += yd
    if xd > 0:
        xd -= 1
    elif xd < 0:
        xd += 1
    yd -= 1

    return (x, y), (xd, yd)


def result(data):
    # target area: x=211..232, y=-124..-69
    targets = defaultdict(int)
    for x in range(211, 233):
        for y in range(69, 125):
            targets[(x,-1*y)] = 1

    max_y = -1
    for x in range(125):
        for y in range(125):
            coord = (0, 0)
            velocity = (x, y)
            apex = -1
            while True:
                coord, velocity = step(coord, velocity)
                if coord[1] > apex:
                    apex = coord[1]
                if coord in targets.keys():
                    if apex > max_y:
                        max_y = apex
                    break
                if coord[1] < -124:
                    break

    return max_y
