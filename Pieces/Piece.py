class Piece:
    def __init__(self, color):
        self.name = "piece"
        self.number_of_pieces = -1
        self.pos = {"x": -1, "y": -1}
        self.color = color
        self.board = None
        self.player = None


    def place(self, x, y):
        self.pos = {"x": x, "y": y}

    # TODO: handle possible index out of bound exception
    def get_n(self):
        if self.board.is_position_in_board((self.pos["x"] - 2,self.pos["y"])):
            return self.board.GAME_BOARD[self.pos["x"] - 2][self.pos["y"]]
        return "ERROR"

    def get_s(self):
        if self.board.is_position_in_board((self.pos["x"] + 2,self.pos["y"])):
            return self.board.GAME_BOARD[self.pos["x"] + 2][self.pos["y"]]
        return "ERROR"

    def get_nw(self):
        if self.board.is_position_in_board((self.pos["x"] - 1,self.pos["y"] - 1)):
            return self.board.GAME_BOARD[self.pos["x"] - 1][self.pos["y"] - 1]
        return "ERROR"

    def get_ne(self):
        if self.board.is_position_in_board((self.pos["x"] - 1,self.pos["y"] + 1)):
            return self.board.GAME_BOARD[self.pos["x"] - 1][self.pos["y"] + 1]
        return "ERROR"

    def get_sw(self):
        if self.board.is_position_in_board((self.pos["x"] + 1, self.pos["y"] - 1)):
            return self.board.GAME_BOARD[self.pos["x"] + 1][self.pos["y"] - 1]
        return "ERROR"

    def get_se(self):
        if self.board.is_position_in_board((self.pos["x"] + 1, self.pos["y"] + 1)):
            return self.board.GAME_BOARD[self.pos["x"] + 1][self.pos["y"] + 1]
        return "ERROR"

    def get_neighbors(self):
        return {
            'n':  self.get_n() if self.get_n() is not None else (self.pos["x"] - 2, self.pos["y"]),
            'w':  self.get_s() if self.get_s() is not None else (self.pos["x"] + 2, self.pos["y"]),
            'nw': self.get_nw() if self.get_nw() is not None else (self.pos["x"] - 1, self.pos["y"] - 1),
            'ne': self.get_ne() if self.get_ne() is not None else (self.pos["x"] - 1, self.pos["y"] + 1),
            'sw': self.get_sw() if self.get_sw() is not None else (self.pos["x"] + 1, self.pos["y"] - 1),
            'se': self.get_se() if self.get_se() is not None else (self.pos["x"] + 1, self.pos["y"] + 1),
        }

    def move(self):
        pass

