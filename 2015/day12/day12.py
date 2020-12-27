from helpers import as_json

input = as_json('2015/day12/input.txt')

def get_sum(input, part=1):
    sum  = 0

    if type(input) == str:
        return sum

    try:
        try:i = int(input)
        except ValueError:
            x = 1
        return i
    except TypeError:
        pass

    if type(input) == dict:

        if 'red' in input.values() and part == 2:
            return 0

        for k in input.keys():
            sum += get_sum(input[k], part)

    elif type(input) == list:
        for i in input:
            sum += get_sum(i, part)
    else:
        for k in input.keys():
            if type(input[k]) == list:
                for i in input[k]:
                    try:
                        i = int(i)
                        sum += i
                    except ValueError:
                        continue
    return sum

print('2015 Part 1')
print(get_sum(input))
print('2015 Part 2')
print(get_sum(input, 2))