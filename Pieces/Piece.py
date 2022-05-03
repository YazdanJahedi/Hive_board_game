from functools import reduce


class Piece:
    def __init__(self, color):
        self.name = 'piece'
        self.number_of_pieces = -1
        self.pos = {'x': -1, 'y': -1}
        self.color = color
        self.board = None
        self.player = None
        self.bottom = None

    def place(self, x, y):
        self.pos['x'] = x
        self.pos['y'] = y

    # ------------------------------------------------------------------------------
    # get north cell piece
    def get_n(self):
        if self.board.is_in_board((self.pos["x"] - 2, self.pos["y"])):
            return self.board.GAME_BOARD[self.pos["x"] - 2][self.pos["y"]]
        return "ERROR"

    # get south cell piece
    def get_s(self):
        if self.board.is_in_board((self.pos["x"] + 2, self.pos["y"])):
            return self.board.GAME_BOARD[self.pos["x"] + 2][self.pos["y"]]
        return "ERROR"

    # get north west cell piece
    def get_nw(self):
        if self.board.is_in_board((self.pos["x"] - 1, self.pos["y"] - 1)):
            return self.board.GAME_BOARD[self.pos["x"] - 1][self.pos["y"] - 1]
        return "ERROR"

    # get north east cell piece
    def get_ne(self):
        if self.board.is_in_board((self.pos["x"] - 1, self.pos["y"] + 1)):
            return self.board.GAME_BOARD[self.pos["x"] - 1][self.pos["y"] + 1]
        return "ERROR"

    # get south west cell piece
    def get_sw(self):
        if self.board.is_in_board((self.pos["x"] + 1, self.pos["y"] - 1)):
            return self.board.GAME_BOARD[self.pos["x"] + 1][self.pos["y"] - 1]
        return "ERROR"

    # get south east cell piece
    def get_se(self):
        if self.board.is_in_board((self.pos["x"] + 1, self.pos["y"] + 1)):
            return self.board.GAME_BOARD[self.pos["x"] + 1][self.pos["y"] + 1]
        return "ERROR"

    # ------------------------------------------------------------------------------
    # get north position
    def get_n_pos(self):
        return self.pos['x'] - 2, self.pos['y']

    # get south position
    def get_s_pos(self):
        return self.pos['x'] + 2, self.pos['y']

    # get north west position
    def get_nw_pos(self):
        return self.pos['x'] - 1, self.pos['y'] - 1

    # get north east position
    def get_ne_pos(self):
        return self.pos['x'] - 1, self.pos['y'] + 1

    # get south west position
    def get_sw_pos(self):
        return self.pos['x'] + 1, self.pos['y'] - 1

    # get south east position
    def get_se_pos(self):
        return self.pos['x'] + 1, self.pos['y'] + 1

    # ------------------------------------------------------------------------------
    # This method returns all adjacent neighbours of a cell as a dictionary
    def get_all_neighbours(self):
        return {
            'n': self.get_n() if self.get_n() is not None else self.get_n_pos(),
            's': self.get_s() if self.get_s() is not None else self.get_s_pos(),
            'nw': self.get_nw() if self.get_nw() is not None else self.get_nw_pos(),
            'ne': self.get_ne() if self.get_ne() is not None else self.get_ne_pos(),
            'sw': self.get_sw() if self.get_sw() is not None else self.get_sw_pos(),
            'se': self.get_se() if self.get_se() is not None else self.get_se_pos(),
        }

    # This method returns all NULL adjacent neighbours of a cell as a dictionary
    def get_null_neighbours_pos(self, base_piece):
        output = []
        neighbors = self.get_all_neighbours().values()
        for neighbor in neighbors:
            if isinstance(neighbor, Piece):
                continue
            fake = Piece('')
            fake.pos = {'x': neighbor[0], 'y': neighbor[1]}
            fake.board = self.board
            not_null_neighbors = \
                reduce(lambda before, n: before + [n] if isinstance(n, Piece) else before,
                       fake.get_all_neighbours().values(), [])
            if len(not_null_neighbors) == 1:
                temp = not_null_neighbors.pop()
                if temp.pos['x'] != base_piece.pos['x'] or temp.pos['y'] != base_piece.pos['y']:
                    output.append(neighbor)
            elif len(not_null_neighbors) > 0:
                output.append(neighbor)

        return output

    # This method returns all NOT-NULL neighbours of a cell as a dictionary
    def get_not_null_neighbors(self):
        return filter(lambda x: isinstance(x, Piece), self.get_all_neighbours().values())

    # ------------------------------------------------------------------------------
    # TODO: add some comments and description to this method!
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

    def get_possible_movements(self):
        pass
