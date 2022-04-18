from Pieces.Piece import Piece


class QueenBee(Piece):
    def possible_movements(self):
        output = set()
        for _, neighbor in self.get_neighbors().items():
            if not isinstance(neighbor, Piece):
                output.add(neighbor)
        return output
