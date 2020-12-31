import re

from helpers import as_list

lines = as_list('2016/day7/input.txt')
# lines = as_list('2016/day7/example-input.txt')


def find_aba_bab(outside, insides):
    match = []
    for a, b, c in zip(outside, outside[1:], outside[2:]):
        if a == c and a != b:
            for inside in insides:
                match.append(b+a+b in inside)
    return any(match)


def find_abba(s):
    match = []
    for a, b, c, d in zip(s, s[1:], s[2:], s[3:]):
        match.append(a == d and b == c and a != c)
    return any(match)


matches = []
matches_ssl = set()
for line in lines:
    splits = re.split('\[([^\]]+)\]', line)
    outside = []
    inside = []
    # ssl = set()

    inners = []
    outers = []

    it = iter(splits)

    for o in it:
        try:
            i = next(it)
        except StopIteration:
            i = ""
        outside.append(find_abba(o))
        inside.append(find_abba(i))
        outers.append(o)
        inners.append(i)

    if any(outside) and not any(inside):
        matches.append(True)

    for o in outers:
        if find_aba_bab(o, inners):
            matches_ssl.add(line)

print('2016 Day 7 Part 1')
print(len(matches))

print('2016 Day 7 Part 2')
print(len(matches_ssl))