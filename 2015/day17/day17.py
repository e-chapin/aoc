import sys
from itertools import combinations

from helpers import as_list_ints

containers = as_list_ints('2015/day17/input.txt')
# containers = as_list_ints('2015/day17/example-input.txt')

total = 150
count = 0
min_containers = sys.maxsize
min_count = 0
for i in range(len(containers)):
    for c in combinations(containers, i):
        liquid = sum(c)
        if liquid == total:
            if i <= min_containers:
                min_containers = i
                min_count += 1
            count += 1

print('2015 Day 17 Part 1')
print(count)
print('2015 Day 17 Part 2')
print(min_containers, min_count)