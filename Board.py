from Pieces.Piece import Piece

colors = {
    'Black': '\u001b[30m',
    'Red': '\u001b[31m',
    'Green': '\u001b[32m',
    'Yellow': '\u001b[33m',
    'Blue': '\u001b[34m',
    'Magenta': '\u001b[35m',
    'Cyan': '\u001b[36m',
    'White': '\u001b[37m',
    'Normal': '\u001b[0m',
}


class Board:
    ROWS = 5
    COLS = 5

    def __init__(self):
        self.GAME_BOARD = []
        for i in range(2 * Board.ROWS):
            self.GAME_BOARD.append([None] * 2 * Board.COLS)

        self.full_positions = {}  # {tuple Piece -> player}

    def __str__(self, **kwargs):
        # TODO: remove colored print
        selects = kwargs.get('selects', {})
        for piece, player in self.full_positions.items():
            selects[(piece.pos['x'], piece.pos['y'])] = self.full_positions[piece]
        res = " "
        for j in range(Board.COLS):
            res += 3 * "_" + 5 * " "
        res += "\n"

        for i in range(Board.ROWS):
            for j in range(Board.COLS):
                piece_label = 3 * " "

                piece = self.GAME_BOARD[2 * i][2 * j]
                # if piece is None and (i, j) in selects.keys():
                #     color_name = selects.get((i, j))
                #     color = colors.get(color_name)
                #     piece_label = color + "NON" + colors.get('Normal')
                if piece is None:
                    piece_label = "   "
                elif isinstance(piece, Piece):
                    piece_label = piece.name[0] + "-" + piece.color[0]

                res += "/" + piece_label + "\\" + 3 * "_"

            res += "\n"

            for j in range(Board.COLS):
                piece_label = 3 * " "

                piece = self.GAME_BOARD[2 * i + 1][2 * j + 1]
                if piece is None:
                    piece_label = "   "
                elif isinstance(piece, Piece):
                    piece_label = piece.name[0] + "-" + piece.color[0]

                res += "\\" + 3 * "_" + "/" + piece_label

            res += "\n"

        return res

    def contains_enemy(self, list_of_cells, player):
        for cell in list_of_cells:
            if isinstance(cell, tuple) or isinstance(cell, str):
                continue
            if cell.player != player:
                return True
        return False

    def __repr__(self):
        res = ""
        for i in self.GAME_BOARD:
            res += str(i) + "\n"

        return res

    def get_possible_insertions(self, player):
        possible_set = set()  # set of tuples of positions
        if len(self.full_positions) == 0:
            possible_set.add((self.ROWS - 1, self.COLS - 1))
        elif len(self.full_positions) == 1:
            possible_set = set(k for k in list(self.full_positions.keys())[0].get_neighbors().values() if k is not None)
        else:
            for piece, _ in self.full_positions.items():
                neighbors = piece.get_neighbors()
                for neighbor in neighbors.values():
                    # neighbor is tuple of x,y if None else Piece
                    if isinstance(neighbor, Piece):
                        continue
                    if neighbor == "ERROR":
                        continue
                    fake_piece = Piece('')
                    fake_piece.pos['x'] = neighbor[0]
                    fake_piece.pos['y'] = neighbor[1]
                    fake_piece.board = self
                    if isinstance(neighbor[0], str):
                        print()
                    if not self.contains_enemy(fake_piece.get_neighbors().values(), player):
                        possible_set.add(neighbor)
        copy_of_Board = self.GAME_BOARD.copy()
        for x, y in possible_set:
            copy_of_Board[x][y] = 1
        return copy_of_Board

    def add_piece(self, pos, piece, color):
        self.GAME_BOARD[pos[0]][pos[1]] = piece
        self.full_positions[piece] = color

    def is_position_in_board(self, position):
        return 0 <= position[0] < self.ROWS * 2 and 0 <= position[1] < self.COLS * 2


# -------------------------------
if __name__ == '__main__':
    b = Board()
    b.GAME_BOARD[1][1] = Piece("w")
    print(b.GAME_BOARD[0][0])
    print(b.__str__(selects={(2, 3): 'Red', (0, 4): 'Blue'}))
    print(repr(b))
