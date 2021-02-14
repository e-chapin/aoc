
def is_valid(x, y):
    value = x * x + 3 * x + 2 * x * y + y + y * y + 1358
    return bin(value).count('1') % 2 == 0 and x >= 0 and y >= 0


q = [(1,1,0)]

visited = set()

part1 = None
part2 = None

while not (part1 and part2):
    x, y, steps = q.pop(0)

    if (x, y) == (31, 39) and not part1:
        part1 = steps

    if steps > 50 and not part2:
        part2 = len(visited)
        # break

    visited.add((x, y))

    if is_valid(x-1, y) and (x-1, y) not in visited:
        q.append((x-1, y, steps+1))

    if is_valid(x+1, y) and (x+1, y) not in visited:
        q.append((x+1, y, steps+1))

    if is_valid(x, y-1) and (x, y-1) not in visited:
        q.append((x, y-1, steps+1))

    if is_valid(x, y+1) and (x, y+1) not in visited:
        q.append((x, y+1, steps+1))

print('2016 Day 13 Part 1')
print(part1)
print('2016 Day 13 Part 2')
print(part2)
