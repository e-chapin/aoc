import hashlib

input = 'abbhdwsy'

i = 0
pw = ''
while len(pw) < 8:
    to_hash = input+str(i)
    hashed = hashlib.md5(to_hash.encode()).hexdigest()
    if hashed[:5] == '00000':
        pw += hashed[5]
    i += 1
print('2016 Day 5 Part 1')
print(pw)

i = -1
pw = {}
while len(pw) < 8:
    i += 1
    to_hash = input+str(i)
    hashed = hashlib.md5(to_hash.encode()).hexdigest()
    if hashed[:5] == '00000':
        try:
            index = int(hashed[5])
            if index not in range(8):
                continue
            pw.setdefault(index, hashed[6])
        except ValueError:
            continue

print('2016 Day 5 Part 2')
print(''.join([pw[k] for k in sorted(pw.keys())]))