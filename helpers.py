import json


def as_json(file):
    with open(file) as f:
        data = json.load(f)
    return data


def as_list_ints(file):
    lines = []
    with open(file) as f:
        for l in f.readlines():
            lines.append(int(l.rstrip('\n')))
    return lines


def as_list(file):
    lines = []
    with open(file) as f:
        for l in f.readlines():
            lines.append(l.rstrip('\n'))
    return lines

