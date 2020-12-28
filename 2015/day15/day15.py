from helpers import as_list

ingredients = dict()

# lines = as_list('2015/day15/example-input.txt')
lines = as_list('2015/day15/input.txt')

for line in lines:
    name, stats = line.split(': ')
    ingredients.setdefault(name, dict())
    for stat in stats.split(', '):
        t, v = stat.split()
        ingredients[name][t] = int(v)


def max_ingredients(ingredients, count_cals=False):

    high = -1
    for a in range(1,100):
        for b in range(1, 100):
            for c in range(1, 100):
                for d in range(1, 100):
                    if a + b + c + d> 100:
                        continue
                    # a: Frosting
                    # b: Candy
                    # c: Butterscotch
                    # d: Sugar
                    frosting = ingredients['Frosting']
                    candy = ingredients['Candy']
                    butterscotch = ingredients['Butterscotch']
                    sugar = ingredients['Sugar']

                    if count_cals:
                        cals = a*frosting['calories'] + b*candy['calories'] + c*butterscotch['calories'] + d*sugar['calories']
                        if cals != 500:
                            continue

                    capacity = max(0, a*frosting['capacity'] + b*candy['capacity'] + c*butterscotch['capacity'] + d*sugar['capacity'])
                    durability = max(0, a*frosting['durability'] + b*candy['durability'] + c*butterscotch['durability'] + d*sugar['durability'])
                    flavor = max(0, a*frosting['flavor'] + b*candy['flavor'] + c*butterscotch['flavor'] + d*sugar['flavor'])
                    texture = max(0, a*frosting['texture'] + b*candy['texture'] + c*butterscotch['texture'] + d*sugar['texture'])


                    val = capacity * durability * flavor * texture
                    high = max(high, val)

    return high

print('2015 Day 15 Part 1')
print(max_ingredients(ingredients, False))
print('2015 Day 15 Part 2')
print(max_ingredients(ingredients, True))