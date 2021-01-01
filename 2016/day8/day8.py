from helpers import  as_list

lines = as_list('2016/day8/input.txt')
# lines = as_list('2016/day8/example-input.txt')

coords = {}

max_row = 6
max_col = 50


def do_command(line):
    if line.startswith('rect'):
        line = line.split()[1]
        i, j = line.split('x')
        for x in range(int(j)):
            for y in range(int(i)):
                coords[(x, y)] = True
    elif line.startswith('rotate row'):
        # rotate row y=1 by 1
        new = []
        _, _, r, _, dist = line.split()
        r = int(r.lstrip('y='))
        for col in range(max_col):
            if coords.get((r, col)):
                shifted = (col + int(dist)) % max_col
                new.append((r, shifted))
                coords[(r, col)] = False
        for c in new:
            coords[c] = True
    elif line.startswith('rotate column'):
        # rotate column x=1 by 1
        new = []
        _, _, c, _, dist = line.split()
        c = int(c.lstrip('x='))
        for row in range(max_row):
            if coords.get((row, c)):
                shifted = (row + int(dist)) % max_row
                new.append((shifted, c))
                coords[(row, c)] = False
        for c in new:
            coords[c] = True


for line in lines:
    do_command(line)

print('2016 Day 8 Part 1')
print(sum(coords.values()))

print('2016 Day 8 Part 2')
for row in range(max_row):
    line = ''
    for col in range(max_col):
        line += '#' if coords.get((row, col)) else '.'
    print(line)