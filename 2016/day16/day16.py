

# a = ['1']

def get_checksum(a):
    r = []
    i = iter(a)
    for x in i:
        y = next(i)
        r.append('1' if x == y else '0')
    return r


def calculate(length):
    a = ['0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '0']
    while len(a) < length:
        b = a.copy()
        b.reverse()
        b = ['0' if x == '1' else '1' for x in b]
        a.append('0')
        a = a + b
    a = a[:length]

    a = get_checksum(a)
    while len(a) % 2 == 0:
        a = get_checksum(a)
    return ''.join(a)


print('2016 Day 16 Part 1')
print(calculate(272))

print('2016 Day 16 Part 2')
print(calculate(35651584))



