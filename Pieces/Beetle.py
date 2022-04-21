from Pieces.Piece import Piece


class Beetle(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.under_piece = None

    def possible_movements(self):
        return self.get_neighbors().items()
