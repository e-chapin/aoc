from helpers import as_list

lines = as_list('2015/day18/input.txt')

def get_lights(part=1):
    global lines
    lights = dict()
    for x, row in enumerate(lines):
        for y, col in enumerate(row):
            light = (x, y)
            lights[light] = True if col == '#' else False
            if part == 2 and light in [(0,0), (0,100), (100,0), (100,000)]:
                lights[light] = True

    return lights


def check_neighbor(light, lights):
    global lines
    count = 0
    lx = light[0]
    ly = light[1]
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == 0 and y == 0:
                continue
            tx = lx+x
            ty = ly + y
            if tx < 0 or ty < 0 or tx >= len(lines) or ty >= len(lines):
                continue
            if lights[(tx, ty)]:
                count += 1
    return count


def run_game(part=1):
    lights = get_lights(part)
    for i in range(100):
        temp = lights.copy()
        for light in lights:
            # print(light)
            n = check_neighbor(light, lights)
            on = lights[light]
            if on and n not in [2, 3]:
                temp[light] = False
            elif not on and n == 3:
                temp[light] = True
            if part == 2 and light in [(0, 0), (0, 99), (99, 0), (99, 99)]:
                temp[light] = True
        lights = temp

    count = 0
    for light in lights:
        if lights[light]:
            count += 1
    return count

print('2015 Day 18 Part 1')
print(run_game(1))
print('2015 Day 18 Part 2')
print(run_game(2))
