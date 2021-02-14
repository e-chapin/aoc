import functools
import hashlib
import re


@functools.lru_cache(maxsize=None)
def get_hash(secret):
    return hashlib.md5(secret.encode('utf8')).hexdigest()


@functools.lru_cache(maxsize=None)
def get_stretch_hash(secret):
    for _ in range(2017):
        secret = hashlib.md5(secret.encode('utf8')).hexdigest()
    return secret


def find_index(salt, stretch=False):

    hashfunc = get_stretch_hash if stretch else get_hash
    salt += '{}'
    keys, index = 0, 0

    while True:
        hash = hashfunc(salt.format(index))
        valid = re.search(r'(\w)\1{2,}', hash)
        if valid:
            next_match = valid.group(0)[0]*5

            if any(next_match in hashfunc(salt.format(j)) for j in range(index+1, index+1001)):
                keys += 1
                if keys == 64:
                    return index

        index += 1

print('2016 Day 14 Part 1')
print(find_index(salt='jlmsuwbz'))

print('2016 Day 14 Part 2')
print(find_index(salt='jlmsuwbz', stretch=True))
