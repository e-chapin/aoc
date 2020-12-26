import re

lights = {}
brightness = {}

with open('input.txt') as f:
    lines = f.readlines()


count = 0
for line in lines:
    groups = re.search('(turn on|turn off|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)', line)

    action = groups[1]
    low = (int(groups[2]), int(groups[3]))
    high = (int(groups[4]), int(groups[5]))

    for x in range(low[0], high[0]+1):
        for y in range(low[1], high[1]+1):
            light = (x, y)
            if action == 'turn on':
                lights[light] = True
                try:
                    brightness[light] = brightness[light] + 1
                except KeyError:
                    brightness[light] = 1
            elif action == 'turn off':
                if light in lights.keys():
                    del lights[light]
                if light in brightness.keys():

                    brightness[light] = brightness[light] - 1
                    if brightness[light] == 0:
                        del brightness[light]
            else:
                if light in lights.keys():
                    del lights[light]
                else:
                    lights[light] = True
                try:
                    brightness[light] = brightness[light] + 2
                except KeyError:
                    brightness[light] = 2
print("2015 Day 6 Part 1")
print(len(lights))

count = 0
print("2015 Day 6 Part 2")
for brightness in brightness.values():
    count += brightness
print(count)