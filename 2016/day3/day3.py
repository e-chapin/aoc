from helpers import as_list

lines = as_list('2016/day3/input.txt')

count = 0
for line in lines:
    sides = [int(x) for x in line.split()]
    m = max(sides)
    sides.remove(m)
    if sum(sides) > m:
        count += 1
print('2016 Day 3 Part 1')
print(count)

count = 0
ts = []
for line in lines:
    ts.append(line.lstrip().split())
# param 3 is offset.
for x, y, z in zip(ts[::3], ts[1::3], ts[2::3]):
    for a, b, c in zip(x, y, z):
        sides = [int(a), int(b), int(c)]
        m = max(sides)
        sides.remove(m)
        if sum(sides) > m:
            count += 1

print('2016 Day 3 Part 2')
print(count)