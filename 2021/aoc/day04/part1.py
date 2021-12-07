# Advent of Code - Day 4 - Part One

from collections import defaultdict
from defaultlist import defaultlist


class Board(object):

    def __init__(self, data):
        self.rows = {}
        self.max_x, self.max_y = None, None
        for x, row in enumerate(data):
            for y, col in enumerate(row.split()):
                self.max_x = x+1
                self.max_y = y+1
                self.rows[(x, y)] = {'val': int(col), 'seen': False}

    def see(self, val):
        for x in range(self.max_x):
            for y in range(self.max_y):
                if self.rows[(x, y)]['val'] == val:
                    self.rows[(x, y)]['seen'] = True

    def bingo(self):
        for x in range(self.max_x):
            bingo = True
            for y in range(self.max_y):
                bingo = bingo and self.rows[(x, y)]['seen']
            if bingo:
                return bingo

        for y in range(self.max_y):
            bingo = True
            for x in range(self.max_x):
                bingo = bingo and self.rows[(x, y)]['seen']
            if bingo:
                return bingo

        return False

    def score(self, val):
        score = 0
        for x in range(self.max_x):
            for y in range(self.max_y):
                if not self.rows[(x, y)]['seen']:
                    score += self.rows[(x, y)]['val']

        return score * val


def result(data):

    numbers = [int(x) for x in data[0].split(',')]
    data.pop(0)
    data.pop(0)

    # next 5 lines are a board, and then a blank line
    boards = []
    while data:
        boards.append(Board(data[:5]))
        data = data[6:]

    for number in numbers:
        for board in boards:
            board.see(number)
            if board.bingo():
                return board.score(number)

    return input
