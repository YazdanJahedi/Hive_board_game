from Pieces import Piece

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
    GAME_BOARD = []

    def __init__(self):
        for i in range(2 * Board.ROWS):
            Board.GAME_BOARD.append([None] * 2 * Board.COLS)
        pass

    def __str__(self, **kwargs):
        selects = kwargs.get('selects', {})
        res = " "
        for j in range(Board.COLS):
            res += 3 * "_" + 5 * " "
        res += "\n"

        for i in range(Board.ROWS):
            for j in range(Board.COLS):
                piece_label = 3 * " "

                piece = Board.GAME_BOARD[2 * i][2 * j]
                if piece is None and (i, j) in selects.keys():
                    color_name = selects.get((i, j))
                    color = colors.get(color_name)
                    piece_label = color + "NON" + colors.get('Normal')
                elif piece is None:
                    piece_label = "NON"

                # elif isinstance(piece, Piece):
                #    piece_label = piece.name[0] + piece.color

                res += "/" + piece_label + "\\" + 3 * "_"

            res += "\n"

            for j in range(Board.COLS):
                piece_label = 3 * " "

                piece = Board.GAME_BOARD[2 * i + 1][2 * j + 1]
                if piece is None:
                    piece_label = "NON"
                # elif isinstance(piece, Piece):
                #    piece_label = piece.name[0] + piece.color

                res += "\\" + 3 * "_" + "/" + piece_label

            res += "\n"

        return res

    def __repr__(self):
        res = ""
        for i in Board.GAME_BOARD:
            res += str(i) + "\n"

        return res


# -------------------------------
if __name__ == '__main__':
    b = Board()
    b.GAME_BOARD[0][0] = 9
    print(b.GAME_BOARD[0][0])
    print(b.__str__(selects={(2, 3): 'Red', (0, 4): 'Blue'}))
    # print(repr(b))
