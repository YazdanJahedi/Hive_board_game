from Pieces.Piece import Piece


class Grasshopper(Piece):

    def __init__(self, color):
        super(Grasshopper, self).__init__(color)
        self.name = 'G'

    def get_possible_movements(self):
        output = set()

        piece_ptr = self.get_ne()
        if piece_ptr:
            north_east_dest = piece_ptr.get_ne()
            while north_east_dest:
                piece_ptr = north_east_dest
                north_east_dest = piece_ptr.get_ne()
            if piece_ptr != "ERROR":
                output.add(piece_ptr.get_ne_pos())

        piece_ptr = self.get_n()
        if piece_ptr:
            north_dest = piece_ptr.get_n()
            while north_dest:
                piece_ptr = north_dest
                north_dest = piece_ptr.get_n()
            if piece_ptr != "ERROR":
                output.add(piece_ptr.get_n_pos())

        piece_ptr = self.get_s()
        if piece_ptr:
            south_dest = piece_ptr.get_s()
            while south_dest:
                piece_ptr = south_dest
                south_dest = piece_ptr.get_s()
            if piece_ptr != "ERROR":
                output.add(piece_ptr.get_s_pos())

        piece_ptr = self.get_nw()
        if piece_ptr:
            north_west_dest = piece_ptr.get_nw()
            while north_west_dest:
                piece_ptr = north_west_dest
                north_west_dest = piece_ptr.get_nw()
            if piece_ptr != "ERROR":
                output.add(piece_ptr.get_nw_pos())

        piece_ptr = self.get_sw()
        if piece_ptr:
            south_west_dest = piece_ptr.get_sw()
            while south_west_dest:
                piece_ptr = south_west_dest
                south_west_dest = piece_ptr.get_sw()
            if piece_ptr != "ERROR":
                output.add(piece_ptr.get_sw_pos())

        piece_ptr = self.get_se()
        if piece_ptr:
            south_east_dest = piece_ptr.get_se()
            while south_east_dest:
                piece_ptr = south_east_dest
                south_east_dest = piece_ptr.get_se()
            if piece_ptr != "ERROR":
                output.add(piece_ptr.get_se_pos())

        return output
