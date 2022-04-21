from Pieces.Piece import Piece


class Beetle(Piece):
    def possible_movements(self):
        return {neighbor if isinstance(neighbor, tuple) else tuple(neighbor.pos.values())
                for neighbor in filter(lambda x: not isinstance(x, str), self.get_neighbors().values())}
