from itertools import permutations

from helpers import as_list

lines = as_list('2015/day9/input.txt')
# lines = as_list('2015/day9/example-input.txt')

destinations = set()
distances = dict()

for l in lines:
    places, distance = l.split(' = ')
    depart, arrive = places.split(' to ')
    destinations.add(depart)
    destinations.add(arrive)
    distances.setdefault(depart, dict())[arrive] = int(distance)
    distances.setdefault(arrive, dict())[depart] = int(distance)

min, max = 0, 0
for r in permutations(distances):
    d = 0
    start = r[0]
    for i in range(1, len(r)):
        end = r[i]
        d += distances[start][end]
        start = end
    if not min or d < min:
        min = d
    if not max or d > max:
        max = d

print('2015 Day 9 Part 1')
print(min)
print('2015 Day 9 Part 2')
print(max)
