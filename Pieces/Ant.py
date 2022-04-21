from Pieces.Piece import Piece


class Ant(Piece):

    def __init__(self, color):
        super(Ant, self).__init__(color)
        self.name = 'A'

    def possible_movements(self):
        output = []
        open_list = []
        visited = []
        open_list.append(self)
        visited.append(tuple(self.pos.values()))
        while len(open_list) != 0:
            this_pos = open_list.pop()
            output.append(tuple(this_pos.pos.values()))
            for n in this_pos.get_null_adjacent_neighbors(self):
                if n not in visited:
                    fake = Piece('')
                    fake.pos = {'x': n[0], 'y': n[1]}
                    fake.board = self.board
                    visited.append(n)
                    open_list.append(fake)
        output.remove(tuple(self.pos.values()))
        return output
