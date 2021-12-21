# Advent of Code - Day 21 - Part Two

import functools

@functools.cache
def play_game(positions, score, player=0):

    positions = list(positions)
    score = list(score)

    rolls = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]

    original_position = positions[player]
    original_score = score[player]

    wins = [0] * len(positions)

    for move, numuniverses in rolls:
        positions[player] = (original_position + move - 1) % 10 + 1
        score[player] = original_score + positions[player]

        if score[player] >= 21:
            wins[player] += numuniverses
        else:
            sub_wins = play_game(tuple(positions), tuple(score), (player+1) % 2)
            for i, count in enumerate(sub_wins):
                wins[i] += numuniverses * count
    return wins


def result(data):

    positions = (8, 3)
    scores = (0, 0)

    return max(play_game(positions, scores))

