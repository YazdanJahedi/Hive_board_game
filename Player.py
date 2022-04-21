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
        self.queen = None

    def is_lost(self):
        if self.queen is None:
            return False
        return len(list(self.queen.get_not_null_neighbors())) == 6

    def can_move(self):
        return self.queen is not None

    def should_insert_queen(self):
        return self.turn == 4 and self.queen is None
