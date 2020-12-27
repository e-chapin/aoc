import json

def as_json(input):
    with open(input) as f:
        data = json.load(f)
    return data


def as_list(input):
    lines = []
    with open(input) as f:
        for l in f.readlines():
            lines.append(l.rstrip('\n'))
    return lines
