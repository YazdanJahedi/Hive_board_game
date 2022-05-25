from Pieces.Piece import Piece


class Ant(Piece):

    def __init__(self, color):
        super(Ant, self).__init__(color)
        self.name = 'A'

    def get_possible_movements(self):
        output = []
        open_list = []
        visited = []
        open_list.append(self)
        visited.append(tuple(self.pos.values()))
        while len(open_list) != 0:
            this_pos = open_list.pop()
            output.append(tuple(this_pos.pos.values()))
            for n in this_pos.get_null_neighbours_pos(self):
                if n not in visited and self.is_valid_slipping(tuple(this_pos.pos.values()), n):
                    fake = Piece('')
                    fake.pos = {'x': n[0], 'y': n[1]}
                    fake.board = self.board
                    visited.append(n)
                    open_list.append(fake)
        output.remove(tuple(self.pos.values()))
        return self.board.filter_valid_moves(self, output)
