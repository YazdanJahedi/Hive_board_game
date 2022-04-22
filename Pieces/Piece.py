from functools import reduce


class Piece:
    def __init__(self, color):
        self.name = "piece"
        self.number_of_pieces = -1
        self.pos = {"x": -1, "y": -1}
        self.color = color
        self.board = None
        self.player = None
        self.bottom = None

    def place(self, x, y):
        self.pos = {"x": x, "y": y}

    # TODO: handle possible index out of bound exception
    def get_n(self):
        if self.board.is_position_in_board((self.pos["x"] - 2, self.pos["y"])):
            return self.board.GAME_BOARD[self.pos["x"] - 2][self.pos["y"]]
        return "ERROR"

    def get_s(self):
        if self.board.is_position_in_board((self.pos["x"] + 2, self.pos["y"])):
            return self.board.GAME_BOARD[self.pos["x"] + 2][self.pos["y"]]
        return "ERROR"

    def get_nw(self):
        if self.board.is_position_in_board((self.pos["x"] - 1, self.pos["y"] - 1)):
            return self.board.GAME_BOARD[self.pos["x"] - 1][self.pos["y"] - 1]
        return "ERROR"

    def get_ne(self):
        if self.board.is_position_in_board((self.pos["x"] - 1, self.pos["y"] + 1)):
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

    def get_n_pos(self):
        return self.pos["x"] - 2, self.pos["y"]

    def get_s_pos(self):
        return self.pos["x"] + 2, self.pos["y"]

    def get_nw_pos(self):
        return self.pos["x"] - 1, self.pos["y"] - 1

    def get_ne_pos(self):
        return self.pos["x"] - 1, self.pos["y"] + 1

    def get_sw_pos(self):
        return self.pos["x"] + 1, self.pos["y"] - 1

    def get_se_pos(self):
        return self.pos["x"] + 1, self.pos["y"] + 1

    def get_neighbors(self):
        return {
            'n': self.get_n() if self.get_n() is not None else (self.pos["x"] - 2, self.pos["y"]),
            'w': self.get_s() if self.get_s() is not None else (self.pos["x"] + 2, self.pos["y"]),
            'nw': self.get_nw() if self.get_nw() is not None else (self.pos["x"] - 1, self.pos["y"] - 1),
            'ne': self.get_ne() if self.get_ne() is not None else (self.pos["x"] - 1, self.pos["y"] + 1),
            'sw': self.get_sw() if self.get_sw() is not None else (self.pos["x"] + 1, self.pos["y"] - 1),
            'se': self.get_se() if self.get_se() is not None else (self.pos["x"] + 1, self.pos["y"] + 1),
        }

    def get_null_adjacent_neighbors(self, base_piece):
        output = []
        neighbors = self.get_neighbors().values()
        for neighbor in neighbors:
            if isinstance(neighbor, Piece):
                continue
            fake = Piece('')
            fake.pos = {'x': neighbor[0], 'y': neighbor[1]}
            fake.board = self.board
            not_null_neighbors = \
                reduce(lambda before, n: before + [n] if isinstance(n, Piece) else before,
                       fake.get_neighbors().values(), [])
            if len(not_null_neighbors) == 1:
                temp = not_null_neighbors.pop()
                if temp.pos['x'] != base_piece.pos['x'] or temp.pos['y'] != base_piece.pos['y']:
                    output.append(neighbor)
            elif len(not_null_neighbors) > 0:
                output.append(neighbor)

        return output

    def get_not_null_neighbors(self):
        return filter(lambda x: isinstance(x, Piece), self.get_neighbors().values())

    def move(self):
        pass

    def is_valid_slipping(self, src_pos, dst_pos):
        if dst_pos[0] - src_pos[0] == 2 and dst_pos[1] == src_pos[1]:
            # V
            if self.board.GAME_BOARD[dst_pos[0] - 1][dst_pos[1] - 1] and self.board.GAME_BOARD[dst_pos[0] - 1][
                dst_pos[1] + 1]:
                return False
        if dst_pos[0] - src_pos[0] == -2 and dst_pos[1] == src_pos[1]:
            # ^
            if self.board.GAME_BOARD[dst_pos[0] + 1][dst_pos[1] + 1] and self.board.GAME_BOARD[dst_pos[0] + 1][
                dst_pos[1] - 1]:
                return False
        if dst_pos[0] - src_pos[0] == -1 and dst_pos[1] - src_pos[1] == -1:
            # '\
            if self.board.GAME_BOARD[dst_pos[0] + 2][dst_pos[1]] and self.board.GAME_BOARD[dst_pos[0] - 1][
                dst_pos[1] + 1]:
                return False
        if dst_pos[0] - src_pos[0] == +1 and dst_pos[1] - src_pos[1] == +1:
            # \.
            if self.board.GAME_BOARD[dst_pos[0] + 2][dst_pos[1]] and self.board.GAME_BOARD[dst_pos[0] + 1][
                dst_pos[1] - 1]:
                return False
        if dst_pos[0] - src_pos[0] == +1 and dst_pos[1] - src_pos[1] == -1:
            # ./
            if self.board.GAME_BOARD[dst_pos[0] - 2][dst_pos[1]] and self.board.GAME_BOARD[dst_pos[0] + 1][
                dst_pos[1] + 1]:
                return False
        if dst_pos[0] - src_pos[0] == -1 and dst_pos[1] - src_pos[1] == +1:
            # /'
            if self.board.GAME_BOARD[dst_pos[0] + 2][dst_pos[1]] and self.board.GAME_BOARD[dst_pos[0] - 1][
                dst_pos[1] - 1]:
                return False
        return True
