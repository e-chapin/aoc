from helpers import as_list

children = dict()

ticker = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

# lines = as_list('2015/day16/example-input.txt')
lines = as_list('2015/day16/input.txt')
print('2015 Day 16 Part 1')
for line in lines:
    sue, stats = line.split(': ', 1)
    name = sue.lstrip('Sue ')
    # print(name, stats)
    match = True
    for stat in stats.split(', '):
        n, v = stat.split(': ')
        if ticker[n] != int(v):
            match = False
            break
    if match:
        print(name, stats)
        break

print('2015 Day 16 Part 2')
for line in lines:
    sue, stats = line.split(': ', 1)
    name = sue.lstrip('Sue ')
    match = True
    for stat in stats.split(', '):
        n, v = stat.split(': ')
        v = int(v)
        tval = ticker[n]

        if n in ['cats', 'trees'] and v <= tval:
            match = False
            break

        elif n in ['pomeranians', 'goldfish'] and v >= tval:
            match = False
            break

        elif n not in ['cats', 'trees', 'pomeranians', 'goldfish'] and tval != v:
            match = False
            break

    if match:
        print(name, stats)


