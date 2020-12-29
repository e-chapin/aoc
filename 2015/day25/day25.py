def get_next_value(v):
    v *= 252533
    return v % 33554393


x = 1
y = 1
val = 20151125
while True:
    if y == 1:
        y = x + 1
        x = 1
    else:
        x += 1
        y -= 1
    # print(x, y)
    val = get_next_value(val)
    if x == 3083 and y == 2978:
        print(val)
        break
