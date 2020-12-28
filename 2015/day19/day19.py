import re
import sys

from helpers import as_list

lines = as_list('2015/day19/input.txt')
# lines = as_list('2015/day19/example-input.txt')

replacements = dict()
molecules = set()
start = lines[-1]
scan = set()

for line in lines:
    if not line:
        break
    a, b = line.split(' => ')
    replacements.setdefault(a, []).append(b)
    scan.add(a)

scan = '|'.join(scan)

for x in re.finditer(scan, start):
    pre = start[:x.span()[0]]
    post = start[x.span()[1]:]
    match = x.group()
    for r in replacements.get(match, []):
        molecules.add(pre + r + post)

print('2015 Day 19 Part 1')
print(len(molecules))
print('2015 Day 19 Part 2')
# didn't really like part 2, got some help from reddit.
replacements = [tuple(reversed(line.split())) for line in lines[:-2]]
starts = [start]
for i in range(10000):
    newstarts = set()
    for data in starts:
        for pattern, _, replacement in replacements:
            st = 0
            while True:
                loc = data.find(pattern, st)
                if loc == -1:
                    break
                new = data[:loc] + replacement + data[loc + len(pattern):]
                if new == "e":
                    print(i + 1)
                    sys.exit()
                newstarts.add(new)
                st = loc + 1
    starts = sorted(newstarts, key=len)[:10]
