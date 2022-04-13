import Pieces.QueenBee


class Player:
    def __init__(self, name, color):
        self.name = name
        self.pieces = [Pieces] * 6
        self.pieces = {
            'QB': 1,
            'S': 2,
            'B': 2,
            'G': 3,
            'A': 3,
        }
        self.turn = 0
        self.is_won = False
        self.score = 0
        self.color = color
