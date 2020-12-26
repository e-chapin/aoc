import codecs

from helpers import as_list

lines = as_list('2015/day8/input.txt')

code_len = 0
mem_len = 0
encode_diff = 0
for line in lines:
    code_len += len(line)
    mem_len += len(eval(line))
    # add up the characters that will add length when encoded. Don't have to actually do encoding.
    # outer "'s are always 2, each # will add an \ when encoded to \", and each \ (\\) will add one when encoded to \\
    encode_diff += 2 + line.count('"') + line.count('\\')

print("2015 Day 8 Part 1")
print(code_len - mem_len)
print("2015 Day 8 Part 2")
print(encode_diff)

# print(sum(2+s.count('\\')+s.count('"') for s in open('2015/day8/example-input.txt')))