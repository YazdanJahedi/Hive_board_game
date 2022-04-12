from Pieces import Piece


class Board:
    ROWS = 5
    COLS = 5
    GAME_BOARD = [[None] * 2 * COLS] * 2 * ROWS

    def __init__(self):
        pass

    def __str__(self):
        res = " "
        for j in range(Board.COLS):
            res += 2 * "_" + 4 * " "
        res += "\n"

        for i in range(Board.ROWS):
            for j in range(Board.COLS):
                piece_label = "  "

                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 0):
                    piece = Board.GAME_BOARD[i][j]
                    if piece is None:
                        piece_label = "N "
                    # elif isinstance(piece, Piece):
                    # piece_label = piece.name[0] + piece.color
                    # pass

                res += "/" + piece_label + "\\" + 2 * "_"

            res += "\n"

            for j in range(Board.COLS):
                piece_label = "  "

                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 0):
                    piece = Board.GAME_BOARD[i][j]
                    if piece is None:
                        piece_label = "N "
                    # elif isinstance(piece, Piece):
                    # piece_label = piece.name[0] + piece.color
                    # pass
                res += "\\" + 2 * "_" + "/" + piece_label

            res += "\n"

        return res

    def __repr__(self):
        res = ""
        for i in Board.GAME_BOARD:
            res += str(i) + "\n"

        return res


# -------------------------------
b = Board()
print(b)
print(repr(b))
