# Advent of Code - Day 15 - Part One


from dijkstras import Graph, dijsktra


def result(data):

    max_y = len(data)-1
    max_x = len(data[0])-1

    risk = {}

    g = Graph()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            g.add_node((x, y))
            risk[(x, y)] = int(c)

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for n in neighbors:
                r = risk.get(n, -1)
                if r > 0:
                    g.add_edge((x, y), n, r)

    visited, path = dijsktra(g, (0,0))
    return visited[(max_x, max_y)]
