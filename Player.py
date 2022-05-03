class Player:
    def __init__(self, name, color):
        self.name = name
        self.pieces = {
            'QB': 1,
            'S': 2,
            'B': 2,
            'G': 3,
            'A': 3,
        }
        self.turn = 0
        self.is_won = False
        self.score = 0
        self.color = color
        self.queen_bee = None

    # when all cells beside the queen be is filled, player is lost!
    def is_lost(self):
        if self.queen_bee is None:
            return False
        return len(list(self.queen_bee.get_not_null_neighbors())) == 6

    # This method returns a boolean determines if player can move his/her pieces or not.
    # technically player can move his/her pieces when the queen bee is inserted in the board
    def can_move(self):
        return self.queen_bee is not None

    # This method checks if the player has inserted queen be piece in the board or not in the proper turn
    # Player should insert queen be piece upto 4th turn
    def should_insert_queen(self):
        return self.turn == 4 and self.queen_bee is None
