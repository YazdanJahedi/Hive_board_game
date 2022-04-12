from Board import Board


class Piece:
    def __init__(self, color):
        self.name = "piece"
        self.number_of_pieces = -1
        self.pos = {"x": -1, "y": -1}
        self.color = color

    def place(self, x, y):
        self.pos = {"x": x, "y": y}

    def get_n(self):
        return Board.GAME_BOARD[self.pos["x"] + 2][self.pos["y"]]

    def get_w(self):
        return Board.GAME_BOARD[self.pos["x"] - 2][self.pos["y"]]

    def get_nw(self):
        return Board.GAME_BOARD[self.pos["x"] + 1][self.pos["y"] - 1]

    def get_ne(self):
        return Board.GAME_BOARD[self.pos["x"] + 1][self.pos["y"] + 1]

    def get_sw(self):
        return Board.GAME_BOARD[self.pos["x"] - 1][self.pos["y"] - 1]

    def get_se(self):
        return Board.GAME_BOARD[self.pos["x"] - 1][self.pos["y"] + 1]
