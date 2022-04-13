from Pieces.Piece import Piece


class Board:
    ROWS = 5
    COLS = 5
    GAME_BOARD = [[None] * 2 * COLS for i in range(2 * ROWS)]

    def __init__(self):

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
                    piece_label = piece.name[0] + "-" + piece.color

                res += "/" + piece_label + "\\" + 3 * "_"

            res += "\n"

            for j in range(Board.COLS):
                piece_label = 3 * " "

                piece = Board.GAME_BOARD[2 * i + 1][2 * j + 1]
                if piece is None:
                    piece_label = "NON"
                elif isinstance(piece, Piece):
                    piece_label = piece.name[0] + "-" + piece.color

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
b.GAME_BOARD[0][0] = Piece(color="w")
print(b.GAME_BOARD[0][0])
print(b)
print(repr(b))
