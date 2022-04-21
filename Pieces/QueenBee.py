from Pieces.Piece import Piece


class QueenBee(Piece):

    def __init__(self, color):
        super(QueenBee, self).__init__(color)
        self.name = 'QB'

    def possible_movements(self):
        output = set()
        for _, neighbor in self.get_neighbors().items():
            if not isinstance(neighbor, Piece) and self.is_valid_slipping(tuple(self.pos.values()), neighbor):
                output.add(neighbor)
        return output
