from Pieces import Piece


class Board:
    ROWS = 6
    COLS = 5
    GAME_BOARD = [[None] * 2 * COLS] * 2 * ROWS

    def __init__(self):
        # This part is written just for testing...
        # Board.GAME_BOARD[0][0] = 1
        pass

    def __str__(self):
        res = " "
        for j in range(Board.COLS):
            res += 3 * "_" + 5 * " "
        res += "\n"

        for i in range(Board.ROWS):
            for j in range(Board.COLS):
                piece_label = 3 * " "

                piece = Board.GAME_BOARD[2 * i][2 * j]
                if piece is None:
                    piece_label = "NON"
                elif isinstance(piece, Piece):
                    piece_label = piece.name[0] + piece.color

                res += "/" + piece_label + "\\" + 3 * "_"

            res += "\n"

            for j in range(Board.COLS):
                piece_label = 3 * " "

                piece = Board.GAME_BOARD[2 * i + 1][2 * j + 1]
                if piece is None:
                    piece_label = "NON"
                elif isinstance(piece, Piece):
                    piece_label = piece.name[0] + piece.color

                res += "\\" + 3 * "_" + "/" + piece_label

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
