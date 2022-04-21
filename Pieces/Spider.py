from Pieces.Piece import Piece


class Spider(Piece):

    def __init__(self, color):
        super(Spider, self).__init__(color)
        self.name = 'S'

    def possible_movements(self):
        self.output = set()
        self.bfs(self, [], 0)
        return self.output

    output = set()

    def bfs(self, piece, visited, level):
        if level == 3 and piece.pos not in visited:
            self.output.add(tuple(piece.pos.values()))
        else:
            for n in piece.get_null_adjacent_neighbors(self):
                if piece.pos not in visited and self.is_valid_slipping(tuple(piece.pos.values()),
                                                                       n if not isinstance(n, Piece) else tuple(
                                                                               n.pos.values())):
                    fake = n
                    if not isinstance(n, Piece):
                        fake = Piece('')
                        fake.pos = {
                            'x': n[0],
                            'y': n[1]
                        }
                        fake.board = self.board
                    self.bfs(fake, visited + [piece.pos], level + 1)
