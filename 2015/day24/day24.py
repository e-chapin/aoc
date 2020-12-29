from itertools import combinations

from helpers import as_list_ints

lines = as_list_ints('2015/day24/input.txt')


# lots of assumptions... lines is sorted small to big, and the first match to weight will also evenly split the other
# groups equally.
def get_qe(l, parts):
    weight = sum(lines) / parts
    for i in range(1, len(l)):
        for group in combinations(l, i):
            if sum(group) == weight:
                qe = 1
                for g in group:
                    qe *= g
                return qe


print('2015 Day 24 Part 1')
print(get_qe(lines, 3))
print('2015 Day 24 Part 2')
print(get_qe(lines, 4))
