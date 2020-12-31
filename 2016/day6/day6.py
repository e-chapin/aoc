from helpers import as_list

lines = as_list('2016/day6/input.txt')
# lines = as_list('2016/day6/example-input.txt')

length = len(lines[0])

positions = {

}

for line in lines:
    for i, c in enumerate(line):
        v = positions.setdefault(i, dict()).setdefault(c, 0)
        positions[i][c] = v + 1

most_common = ''
least_common = ''

for p in positions.values():
    s = sorted(p.items(), key=lambda kv: kv[1], reverse=True)
    most_common += s[0][0]
    least_common += s[-1][0]
    # word += sorted(p, key=lambda kv: (v), reverse=True)[0]

print('2016 Day 6 Part 1')
print(most_common)
print('2016 Day 6 Part 2')
print(least_common)
