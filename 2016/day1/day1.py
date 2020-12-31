direction, north, east = 0, 0, 0
visited = {}
p2 = False

input = 'L3, R2, L5, R1, L1, L2, L2, R1, R5, R1, L1, L2, R2, R4, L4, L3, L3, R5, L1, R3, L5, L2, R4, L5, R4, R2, L2, L1, R1, L3, L3, R2, R1, L4, L1, L1, R4, R5, R1, L2, L1, R188, R4, L3, R54, L4, R4, R74, R2, L4, R185, R1, R3, R5, L2, L3, R1, L1, L3, R3, R2, L3, L4, R1, L3, L5, L2, R2, L1, R2, R1, L4, R5, R4, L5, L5, L4, R5, R4, L5, L3, R4, R1, L5, L4, L3, R5, L5, L2, L4, R4, R4, R2, L1, L3, L2, R5, R4, L5, R1, R2, R5, L2, R4, R5, L2, L3, R3, L4, R3, L2, R1, R4, L5, R1, L5, L3, R4, L2, L2, L5, L5, R5, R2, L5, R1, L3, L2, L2, R3, L3, L4, R2, R3, L1, R2, L5, L3, R4, L4, R4, R3, L3, R1, L3, R5, L5, R1, R5, R3, L1'

for d in input.split(', '):
    turn = d[:1]
    distance = int(d[1:])

    if turn == 'R':
        direction += 90
        direction %= 360
    else:
        if direction == 0:
            direction = 270
        else:
            direction -= 90

    while distance > 0:
        if direction == 0:
            north += 1
        elif direction == 90:
            east += 1
        elif direction == 180:
            north -= 1
        else:
            east -= 1

        distance -= 1

        if (north, east) in visited.keys() and not p2:
            print('2016 Day 1 Part 2')
            print((north, east))
            print(abs(north) + abs(east))
            p2 = True
        else:
            visited[(north, east)] = True

print('2016 Day 1 Part 1')
print(abs(north) + abs(east))
