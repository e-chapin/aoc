import collections
from helpers import as_list

lines = as_list('2016/day10/input.txt')

bots = collections.defaultdict(list)
output = collections.defaultdict(list)

instructions = {}

for line in lines:
    instr = line.split(' ')
    f = instr[0]
    if f == 'value':
        value = int(instr[1])
        destination = int(instr[-1])
        bots[destination].append(value)

    else:
        target = int(instr[1])
        instructions[target] = [(instr[5], int(instr[6])), (instr[10], int(instr[11]))]

while bots:
    for bot, values in dict(bots).items():
        if len(values) == 2:
            values.sort()
            low, high = values
            if low == 17 and high == 61:
                print('2016 Day 10 Part 1')
                print(bot)

            low_d, high_d = instructions[bot]

            if low_d[0] == 'bot':
                bots[low_d[1]].append(low)
            else:
                output[low_d[1]].append(low)
            if high_d[0] == 'bot':
                bots[high_d[1]].append(high)
            else:
                output[high_d[1]].append(high)
            bots.pop(bot)

print('2016 Day 10 Part 2')
