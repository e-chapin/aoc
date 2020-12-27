from itertools import groupby


password = 'cqjxjnds'
# password = 'ghijklmn'

alphabet = 'abcdefghijklmnopqrstuvwxyz'

cvals = {c: i for i, c in enumerate(alphabet)}


def increment(pw):
    cval = cvals[pw[-1]]
    if cval == 25:
        return increment(pw[:-1]) + 'a'
    else:
        pw = pw[:-1] + alphabet[cval+1]
        return pw


def check_valid(pw):

    if 'i' in pw or 'o' in pw or 'l' in pw:
        return False

    valid = False
    i = 0
    while i < len(pw)-2:
        a, b, c = cvals[pw[i]], cvals[pw[i+1]], cvals[pw[i+2]]
        if b == a+1 and c == a+2:
            valid = True
            break
        i += 1
    if not valid:
        return False

    groups = {key: len(list(group)) for key, group in groupby(pw, None)}
    pairs = 0
    for v in groups.values():
        if v == 2:
            pairs +=1
    if pairs < 2:
        return False
    return True


def next_pw(password):
    valid = False
    while not valid:
        password = increment(password)
        if 'i' in password:
            pre, post = password.split('i', 1)
            password = pre + 'j' + 'a' * len(post)
            continue
        if 'o' in password:
            pre, post = password.split('o', 1)
            password = pre + 'p' + 'a' * len(post)
            continue
        if 'l' in password:
            pre, post = password.split('l', 1)
            password = pre + 'm' + 'a' * len(post)
        valid = check_valid(password)
    return password

print('2015 Day 11 Part 1')
password = next_pw(password)
print(password)
print('2015 Day 11 Part 2')
password = next_pw(password)
print(password)


