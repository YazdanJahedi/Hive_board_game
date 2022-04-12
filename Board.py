class Board:
    ROWS = 10
    COLS = 10
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
                #if i % 2 == 0:
                 #   pass
                res += "/" + 2 * " " + "\\" + 2 * "_"

            res += "\n"

            for j in range(Board.COLS):
                res += "\\" + 2 * "_" + "/" + 2 * " "
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
