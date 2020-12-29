from helpers import as_list

registers = {
  'a': 0,
  'b': 0
}


def apply_instruction(i):

    # jio a, +2
    line = i.split(', ')
    instr, reg = line[0].split()

    r = registers.get(reg)

    if instr == 'hlf':
        registers[reg] = int(r/2)
        return 1

    elif instr == 'tpl':
        registers[reg] = r*3
        return 1

    elif instr == 'inc':
        registers[reg] = r+1
        return 1

    elif instr == 'jmp':
        return int(reg)

    elif instr == 'jie':
        if r % 2 == 0:
            return int(line[1])
        return 1

    elif instr == 'jio':
        if r == 1:
            return int(line[1])
        return 1


lines = as_list('2015/day23/example-input.txt')
lines = as_list('2015/day23/input.txt')
i = 0
while True:
    if i >= len(lines):
        print('done', i)
        break
    print(lines[i])
    i = i + apply_instruction(lines[i])
    print(i)
print('2015 Day 23 Part 1')
print(registers)


registers = {
  'a': 1,
  'b': 0
}
i = 0
print('2015 Day 23 Part 2')
while True:
    if i >= len(lines):
        print('done', i)
        break
    print(lines[i])
    i = i + apply_instruction(lines[i])
    print(i)
print(registers)