# Advent of Code - Day 20 - Part Two


scan = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
key = []


def bools_to_int(grid):
    r = ''
    for c in grid:
        r += '1' if c else '0'
    return int(r, 2)


def pixel_is_on(c):
    return c == '#'


def get_pixel(image, x, y, default):
    if x < 0 or y < 0: return default
    try:
        return image[x][y]
    except IndexError:
        return default


def enhance(image, default):
    margin = 3
    height = len(image)
    length = len(image[0])
    new_image = []

    for i in range(-margin, height + margin):
        row = []
        for j in range(-margin, length + margin):
            grid = [get_pixel(image, i + dx, j + dy, default) for (dx, dy) in scan]
            row.append(key[bools_to_int(grid)])
        new_image.append(row)
    return new_image


def count(new_image):
    sum = 0
    for row in new_image:
        for col in row:
            sum += 1 if col else 0
    return sum


def result(data):
    global pixels
    global key
    key = [pixel_is_on(c) for c in data[0]]
    image = data[2:]

    original = []
    for i in range(len(image)):
        original.append([pixel_is_on(c) for c in image[i]])

    grid_on = False
    for _ in range(50):
        original = enhance(original, grid_on)
        grid_on = not grid_on

    return count(original)