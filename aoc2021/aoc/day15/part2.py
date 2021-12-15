# Advent of Code - Day 15 - Part Two

# This is so slow lol

from dijkstras import Graph, dijsktra


def result(data):

    max_y = len(data) * 5 - 1
    max_x = len(data[0]) * 5 - 1

    xfactor = len(data[0])
    yfactor = len(data)

    risk = {}

    g = Graph()
    for i in range(5):
        for y, line in enumerate(data):
            for j in range(5):
                for x, c in enumerate(line):
                    x_ = x + j * xfactor
                    y_ = y + i * yfactor
                    g.add_node((x_, y_))
                    r = (int(c) + i + j)
                    risk[(x_, y_)] = r % 9 if r > 9 else r

    for i in range(5):
        for y, line in enumerate(data):
            for j in range(5):
                for x, c in enumerate(line):
                    x_ = x + j * xfactor
                    y_ = y + i * yfactor
                    neighbors = [(x_+1, y_), (x_-1, y_), (x_, y_+1), (x_, y_-1)]
                    for n in neighbors:
                        r = risk.get(n, -1)
                        if r > 0:
                            g.add_edge((x_, y_), n, r)

    visited, path = dijsktra(g, (0,0))
    return visited[(max_x, max_y)]
