from helpers import as_list

lines = as_list('2015/day14/input.txt')
# lines = as_list('2015/day14/example-input.txt')
seconds = 2503

reindeer = dict()

for line in lines:
    # Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    line = line.split()
    name = line[0]
    speed = int(line[3])
    duration = int(line[6])
    rest = int(line[-2])
    reindeer.setdefault(name, dict())['stats'] = {'speed': speed, 'duration': duration, 'rest': rest}
    reindeer[name]['current'] = {'flying': True, 'duration': duration, 'distance': 0, 'points': 0}


def assign_points(reindeer):
    m = -1
    for r in reindeer:
        d = reindeer[r]['current']['distance']
        if d > m:
            m = d

    for r in reindeer:
        d = reindeer[r]['current']['distance']
        if d == m:
            reindeer[r]['current']['points'] += 1

for i in range(0, seconds):
    for r in reindeer.items():
        name, info = r
        if info['current']['duration'] >= 1:
            if info['current']['flying']:
                info['current']['distance'] += info['stats']['speed']
        else:
            if info['current']['flying']:
                info['current']['flying'] = False
                info['current']['duration'] = info['stats']['rest']
            else:
                info['current']['flying'] = True
                info['current']['duration'] = info['stats']['duration']
                info['current']['distance'] += info['stats']['speed']

        info['current']['duration'] -= 1
    assign_points(reindeer)

m = -1
for r in reindeer:
    d = reindeer[r]['current']['distance']
    if d > m:
        m = d
print('2015 Day 14 Part 1')
print(m)

part2 = -1
for r in reindeer:
    p = reindeer[r]['current']['points']
    if p > part2:
        part2 = p
print('2015 Day 14 Part 2')
print(part2)
