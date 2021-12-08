# Advent of Code - Day 3 - Part Two

def count_index(data, index):

    z = 0
    for line in data:
        if line[index] == '0':
            z += 1
    return z, len(data[0])+1-z


def get_oxygen_rating(data):
    i = 0
    while True:
        if len(data) == 1:
            return int(data[0], 2)
        z, o = count_index(data, i)
        most = '1' if o >= z else '0'
        data = [row for row in data if row[i] == most]
        i += 1


def get_co2_rating(data):
    i = 0
    while True:
        if len(data) == 1:
            return int(data[0], 2)
        z, o = count_index(data, i)
        least = '0' if z <= o else '1'
        data = [row for row in data if row[i] == least]
        i += 1


def result(data):
    oxygen_rating = get_oxygen_rating(data)
    c02_rating = get_co2_rating(data)
    return oxygen_rating*c02_rating