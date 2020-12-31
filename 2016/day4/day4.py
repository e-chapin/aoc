from collections import Counter

from helpers import as_list

lines = as_list('2016/day4/input.txt')
# lines = as_list('2016/day4/example-input.txt')


alph = 'abcdefghijklmnopqrstuvwxyz'

def check_room(parts, checksum):

    freq = Counter(parts)
    full_cs = [x[0] for x in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))]
    return checksum == ''.join(full_cs[:5])


def shift_name(n, sector_id):
    decrypted = ''
    for c in n:
        if c == '-':
            decrypted += '-'
            continue
        d_index = alph.index(c) + sector_id
        d_index %= 26

        decrypted += alph[d_index]

    return decrypted

total = 0
names = {}
for line in lines:

    name, metadata = line.rsplit('-', 1)
    sector_id, checksum = metadata.rstrip(']').split('[')

    # name = name.replace('-', '')
    sector_id = int(sector_id)


    if check_room(name.replace('-', ''), checksum):
        total += sector_id

    names[name] = sector_id

print('2016 Day 4 Part 1')
print(total)

for k, v in names.items():
    decrypted = shift_name(k, v)
    if decrypted == 'northpole-object-storage':
        print('2016 Day 4 Part 2')
        print(v)
        break


