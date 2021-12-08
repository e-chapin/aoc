# Advent of Code - Day 8 - Part One

import itertools
import re


def result(data):

    count = 0
    # borrowed from reddit to learn about some of these builtins
    for line in data:
        seqs = [frozenset(seq) for seq in re.findall(r'\w+', line)]
        _1, _7, _4, *pending, _8 = sorted(set(seqs), key=len)
        sorter = lambda x: [len(x & _8), len(x & _4), len(x & _1)]
        _2, _5, _3, _6, _0, _9 = sorted(pending, key=sorter)
        ns = [_0, _1, _2, _3, _4, _5, _6, _7, _8, _9]
        count += int(''.join(str(ns.index(x)) for x in seqs[-4:]))
    return count

    # digits = {
    #     'acedgfb': 8,
    #     'cdfbe': 5,
    #     'gcdfa': 2,
    #     'fbcad': 3,
    #     'dab': 7,
    #     'cefabd': 9,
    #     'cdfgeb': 6,
    #     'eafb': 4,
    #     'cagedb': 0,
    #     'ab': 1
    # }
    # # sort key alphabetlically
    # digits = {''.join(sorted(k)): v for k, v in digits.items()}
    #
    # ans = 0
    # for line in data:
    #     a, b = line.split(' | ')
    #     a = a.split(' ')
    #     b = b.split(' ')
    #
    #     # for every combo of a-g
    #     for perm in itertools.permutations('abcdefg'):
    #         # map a-g to the letter in the same position
    #         wires = {a: b for a, b in zip(perm, 'abcdefg')}
    #         # for each word in a and b, map each letter to the generated wire
    #         anew = [''.join(wires[c] for c in x) for x in a]
    #         bnew = [''.join(wires[c] for c in x) for x in b]
    #         if all(''.join(sorted(an)) in digits for an in anew):
    #             bnew = [''.join(sorted(x)) for x in bnew]
    #             ans += int(''.join(str(digits[x]) for x in bnew))
    #             break
    # print(ans)