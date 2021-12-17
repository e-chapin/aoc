# Advent of Code - Day 16 - Part Two

# My algorith was really close but I got tired. Got some help from reddit on this one

total = 0


def parse(data):
    global total

    version = int(data[:3],2)
    total += version
    data = data[3:]

    type = int(data[:3],2)
    data = data[3:]

    if type == 4:
        nums = ''
        while True:
            c = data[0]
            nums += data[1:5]
            data = data[5:]
            if c == '0':
                return data, int(nums, 2)
    else:
        length = data[:1]
        data = data[1:]
        sub_packet_values = []

        if length == '0':
            # the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet
            n = int(data[:15], 2)
            data = data[15:]
            subpackets = data[:n]
            while subpackets:
                subpackets, value = parse(subpackets)
                sub_packet_values.append(value)
            data = data[n:]

        else:
            # the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet
            n = int(data[:11], 2)
            data = data[11:]
            for i in range(n):
                data, value = parse(data)
                sub_packet_values.append(value)

        if type == 0:
            return data, sum(sub_packet_values)
        if type == 1:
            p = 1
            for x in sub_packet_values:
                p *= x
            return data, p
        if type == 2:
            return data, min(sub_packet_values)
        if type == 3:
            return data, max(sub_packet_values)
        if type == 5:
            return data, 1 if sub_packet_values[0] > sub_packet_values[1] else 0
        if type == 6:
            return data, 1 if sub_packet_values[0] < sub_packet_values[1] else 0
        if type == 7:
            return data, 1 if sub_packet_values[0] == sub_packet_values[1] else 0


def result(data):

    translate = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    global total
    data = data[0]
    data = "".join([translate[x] for x in data])
    return parse(data)[1]
