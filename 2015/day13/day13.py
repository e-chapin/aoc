from itertools import permutations


from helpers import as_list

# lines = as_list('2015/day13/example-input.txt')
lines = as_list('2015/day13/input.txt')

arrangement = dict()

for line in lines:
    line = line.split()
    person = line[0]
    neighbor = line[-1].rstrip('.')
    gain = 1 if line[2] == 'gain' else -1
    units = line[3]
    arrangement.setdefault(person, dict())[neighbor] = gain*int(units)


def get_max(arrangement):
    m = -1
    for group in permutations(arrangement, None):
        sum = 0
        for i, g in enumerate(group):
            sum += arrangement[g][group[(i + 1) % len(group)]]
            sum += arrangement[g][group[i + -1]]
            x = 1
        if sum > m:
            m = sum
    return m


m = get_max(arrangement)

print('2015 Day 13 Part 1')
print(m)

arrangement.setdefault('milo', dict())
for k in arrangement.keys():
    arrangement['milo'][k] = 0
    arrangement[k]['milo'] = 0

m = get_max(arrangement)

print('2015 Day 13 Part 2')
print(m)
