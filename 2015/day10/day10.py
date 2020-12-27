from itertools import groupby

look = '3113322113'
for i in range(0, 40):
    say = ''
    for key, group in groupby(look, None):
        say += str(len(list(group))) + str(key)
    look = say
print('2015 Day 10 Part 1')
print(len(look))

look = '3113322113'
for i in range(0, 50):
    say = ''
    for key, group in groupby(look, None):
        say += str(len(list(group))) + str(key)
    look = say
print('2015 Day 10 Part 2')
print(len(look))