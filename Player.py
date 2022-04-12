import Pieces.QueenBee


class Player:
    def __init__(self, name):
        self.name = name
        self.pieces = [Pieces] * 6
        self.is_won = False
        self.score = 0
