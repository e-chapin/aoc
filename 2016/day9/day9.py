from helpers import as_list

lines = as_list('2016/day9/input.txt')
line = lines[0]


def decompress_line(line, recurse=True):
    new_line = ''
    i = 0

    if '(' not in line:
        return line

    while i < len(line):
        if line[i] == '(':
            i += 1
            marker, remaining = line[i:].split(')', 1)
            count, repeat = marker.split('x')
            count, repeat = int(count), int(repeat)
            decompressed = remaining[:count]
            if '(' in decompressed and recurse:
                decompressed = decompress_line(decompressed, True)
            new_line += decompressed*repeat
            line = remaining[count:]
            i = 0
            # move forward one char, plus account for marker: (AxB).
            # 3 for (, x, and ), and len of A and B

        else:
            new_line += line[i]
            i += 1

    return new_line


print('2016 Day 9 Part 1')
new_line = decompress_line(line, recurse=False)
print(len(new_line))


print('2016 Day 9 Part 2')
new_line = decompress_line(line, recurse=True)
print(len(new_line))