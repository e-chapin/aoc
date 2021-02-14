def do_drop(drop_time, discs):
    for t in range(1, (len(discs))+1):
        current_time = drop_time + t
        max, start = discs[t]
        if ((start + current_time) % max) != 0:
            return False
    return True


def calculate_drop(discs):
    drop_time = 0
    while True:
        if do_drop(drop_time, discs):
            return drop_time
        else:
            drop_time+=1


discs = {
    1: (17, 1),
    2: (7, 0),
    3: (19, 2),
    4: (5, 0),
    5: (3, 0),
    6: (13, 5)
}

print('2016 Day 15 Part 1')
print(calculate_drop(discs))

discs[7] = (11, 0)
print('2016 Day 15 Part 2')
print(calculate_drop(discs))





