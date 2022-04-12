import Board as B


class Piece:
    def __init__(self):
        self.pos = {"x": -1, "y": -1}

    def place(self, x, y):
        self.pos = {"x": x, "y": y}

    def get_n(self):
        return B.Board.GAME_BOARD[self.pos["x"] + 2][self.pos["y"]]

    def get_w(self):
        return B.Board.GAME_BOARD[self.pos["x"] - 2][self.pos["y"]]

    def get_nw(self):
        return B.Board.GAME_BOARD[self.pos["x"] + 1][self.pos["y"] - 1]

    def get_ne(self):
        return B.Board.GAME_BOARD[self.pos["x"] + 1][self.pos["y"] + 1]

    def get_sw(self):
        return B.Board.GAME_BOARD[self.pos["x"] - 1][self.pos["y"] - 1]

    def get_se(self):
        return B.Board.GAME_BOARD[self.pos["x"] - 1][self.pos["y"] + 1]
