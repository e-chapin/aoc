import collections
from helpers import as_list

lines = as_list('2016/day12/input.txt')

registers = collections.defaultdict(int)


def get_value(v):
    try:
        return int(v)
    except ValueError:
        return registers[v]


def do_command(command):

    # print('doing command: ', command)
    cmd = command.split(' ')
    if cmd[0] == 'cpy':
        registers[cmd[2]] = get_value(cmd[1])
    elif cmd[0] == 'inc':
        registers[cmd[1]] += 1
    elif cmd[0] == 'dec':
        registers[cmd[1]] -= 1
    elif cmd[0] == 'jnz':
        # cmd[1] is either an int or a register name
        v = get_value(cmd[1])
        if v != 0:
            return get_value(cmd[2])
    return 1


line = 0
while line < len(lines):
    # print('doing line: ', line)
    offset = do_command(lines[line])
    line += offset


print('2016 day 12 part 1')
print(registers.get('a'))

registers = collections.defaultdict(int)
registers['c'] = 1
line = 0
while line < len(lines):
    # print('doing line: ', line)
    offset = do_command(lines[line])
    line += offset

print('2016 day 12 part 2')
print(registers.get('a'))