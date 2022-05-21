from Pieces.Piece import Piece


class Beetle(Piece):

    def __init__(self, color):
        super(Beetle, self).__init__(color)
        self.name = 'B'

    def get_possible_movements(self):
        return {neighbor if isinstance(neighbor, tuple) else tuple(neighbor.pos.values())
                for neighbor in filter(lambda x: not isinstance(x, str), self.get_all_neighbours().values())}
