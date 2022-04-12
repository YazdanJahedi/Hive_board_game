from Pieces import Piece


class Board:
    GAME_BOARD = [[Piece] * 2] * 2

    def __init__(self):
        self.a = 3


    def __repr__(self):
        print(Board.GAME_BOARD)


