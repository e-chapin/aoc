items_part_one = [4, 5, 1, 0]
items_part_two = [8, 5, 1, 0]

# hint from reddit: to move n items up 1 floor, it requires 2 * (n - 1) - 1 moves
def count_moves(items):
    moves = 0
    total_items = sum(items)
    while items[-1] < total_items:
        floor = 0
        # check for empty floors. while loop in case multiple in a row are empty.
        while items[floor] == 0:
            floor += 1
        moves += 2 * (items[floor] - 1) - 1
        items[floor+1] += items[floor]
        items[floor] = 0
    return moves


print('2016 Day 11 Part 1')
print(count_moves(items_part_one))
print('2016 Day 11 Part 2')
print(count_moves(items_part_two))
