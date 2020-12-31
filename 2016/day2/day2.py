from helpers import as_list

# lines = as_list('2016/day2/example-input.txt')
lines = as_list('2016/day2/input.txt')

i, j = 1, 1

keypad = {
    (0, 0): '1',
    (0, 1): '2',
    (0, 2): '3',
    (1, 0): '4',
    (1, 1): '5',
    (1, 2): '6',
    (2, 0): '7',
    (2, 1): '8',
    (2, 2): '9'
}

code = ''

for line in lines:
    for c in line:
        if c == 'U':
            i = max(0, i-1)
        elif c == 'D':
            i = min(2, i+1)
        elif c == 'L':
            j = max(0, j-1)
        elif c == 'R':
            j = min(2, j+1)
    code += keypad[(i, j)]

print('2016 Day 2 Part 1')
print(code)

i, j = 2, 0

keypad = {
    (0, 2): '1',
    (1, 1): '2',
    (1, 2): '3',
    (1, 3): '4',
    (2, 0): '5',
    (2, 1): '6',
    (2, 2): '7',
    (2, 3): '8',
    (2, 4): '9',
    (3, 1): 'A',
    (3, 2): 'B',
    (3, 3): 'C',
    (4, 2): 'D'
}

code = ''

keys = keypad.keys()
for line in lines:
    for c in line:
        if c == 'U':
            if (i-1, j) in keys:
                i -= 1
        elif c == 'D':
            if (i+1, j) in keys:
                i += 1
        elif c == 'L':
            if (i, j-1) in keys:
                j -= 1
        elif c == 'R':
            if (i, j+1) in keys:
                j += 1
    code += keypad[(i, j)]

print('2016 Day 2 Part 2')
print(code)
