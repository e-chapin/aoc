# Advent of Code - Day 21 - Part One

def result(data):

    positions = [8, 3]
    score = [0, 0]
    dice = 1

    while True:
        for p in range(2):
            new_position = (positions[p] + dice + dice+1 + dice+2 - 1) % 10 + 1
            dice += 3
            score[p] += new_position
            positions[p] = new_position

            if score[p] >= 1000:
                return score[1-p]*(dice-1)
