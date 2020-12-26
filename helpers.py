
def as_list(input):
    lines = []
    with open(input) as f:
        for l in f.readlines():
            lines.append(l.rstrip('\n'))
    return lines
