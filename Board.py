from Pieces.Piece import Piece
import copy


class Board:
    ROWS = 10
    COLS = 10

    def __init__(self, p1, p2, board=None, full_positions=None):
        self.full_positions = {}  # {tuple Piece -> player}
        self.GAME_BOARD = []

        # creating the GAME_BOARD
        for i in range(2 * Board.ROWS):
            self.GAME_BOARD.append([None] * 2 * Board.COLS)

        if board is not None:
            self.GAME_BOARD = copy.deepcopy(board)
        if full_positions is not None:
            new_full_pos = {}
            for piece, player in self.full_positions.items():
                pass
                # TODO: resolve copy problems
                # new_full_pos[piece.copy(self.GAME_BOARD, p1.copy(), p2.copy())] = player

    def __str__(self, **kwargs):
        res = " "
        for i in range(self.COLS):
            res += ' ' + str(i * 2) + (7 - len(str(i * 2))) * ' '
        res += '\n '
        for j in range(Board.COLS):
            res += 3 * "_" + 5 * " "
        res += "\n"

        for i in range(Board.ROWS):
            for j in range(Board.COLS):
                piece_label = 3 * " "

                piece = self.GAME_BOARD[2 * i][2 * j]
                # if piece is None and (i, j) in selects.keys():
                #     color_name = selects.get((i, j))
                #     color = colors.get(color_name)
                #     piece_label = color + "NON" + colors.get('Normal')
                if piece is None:
                    piece_label = "   "
                elif isinstance(piece, Piece):
                    piece_label = piece.name[0] + ("-" if not piece.bottom else "+") + piece.color[0]

                res += "/" + piece_label + "\\" + 3 * "_"

            res += f"{i * 2}\n"

            for j in range(Board.COLS):
                piece_label = 3 * " "

                piece = self.GAME_BOARD[2 * i + 1][2 * j + 1]
                if piece is None:
                    piece_label = "   "
                elif isinstance(piece, Piece):
                    piece_label = piece.name[0] + ("-" if not piece.bottom else "+") + piece.color[0]

                res += "\\" + 3 * "_" + "/" + piece_label

            res += "\n"

        return res

    def contains_enemy(self, list_of_cells, player):
        for cell in list_of_cells:
            if isinstance(cell, tuple) or isinstance(cell, str):
                continue
            if cell.player != player:
                return True
        return False

    def __repr__(self):
        res = ""
        for i in self.GAME_BOARD:
            res += str(i) + "\n"

        return res

    def get_possible_insertions(self, player):
        if len(self.full_positions) == 0:
            return {(self.ROWS - 1, self.COLS - 1)}
        if len(self.full_positions) == 1:
            return set(k for k in list(self.full_positions.keys())[0].get_all_neighbours().values() if k is not None)
        output = set()  # set of tuples of positions
        for piece, _ in self.full_positions.items():
            neighbors = piece.get_all_neighbours()
            for neighbor in neighbors.values():
                # neighbor is tuple of x,y if None else Piece
                if isinstance(neighbor, Piece):
                    continue
                if neighbor == "ERROR":
                    continue
                fake_piece = Piece('')
                fake_piece.pos['x'] = neighbor[0]
                fake_piece.pos['y'] = neighbor[1]
                fake_piece.board = self
                if not self.contains_enemy(fake_piece.get_all_neighbours().values(), player):
                    output.add(neighbor)
        return output

    def add_piece(self, pos, piece, color):
        self.GAME_BOARD[pos[0]][pos[1]] = piece
        self.full_positions[piece] = color

    # This method returns a boolean determine if a position in in the board or not
    def is_in_board(self, position):
        return 0 <= position[0] < self.ROWS * 2 and 0 <= position[1] < self.COLS * 2

    def get_move_sources(self, player):
        return dict(filter(lambda key_val: key_val[1] == player.color, self.full_positions.items()))

    def move_if_can(self, piece, destination):
        x0, y0 = tuple(piece.pos.values())
        self.move(piece, destination)
        if not Board.is_connected(self):
            self.move(piece, (x0, y0))
            return False
        return True

    def move(self, piece, destination):
        source_x, source_y = piece.pos.values()
        dest_x, dest_y = destination
        self.GAME_BOARD[source_x][source_y] = piece.bottom

        # if self.GAME_BOARD[dest_x][dest_y]:
        piece.bottom = self.GAME_BOARD[dest_x][dest_y]

        self.GAME_BOARD[dest_x][dest_y] = piece
        # else:
        #     self.GAME_BOARD[dest_x][dest_y] = Piece('')
        #     self.GAME_BOARD[dest_x][dest_y].pos = {
        #         'x': dest_x,
        #         'y': dest_y
        #     }
        # if not to_test_move:
        piece.pos = {
            'x': dest_x,
            'y': dest_y
        }

        # self.full_positions[dest_x][dest_y] = piece
        # if self.GAME_BOARD[source_x][source_y] is None:
        #     del self.full_positions[source_x][source_y]

    # def copy(self):
    #     result = Board()
    #     result.GAME_BOARD = [row[:] for row in self.GAME_BOARD]
    #     result.full_positions = self.full_positions.copy()
    #     return result

    @staticmethod
    def is_connected(temp_board):
        start_piece = list(temp_board.full_positions.keys())[0]
        open_list = []
        visited = set()
        open_list.append(start_piece)
        visited.add(start_piece)
        while len(open_list) != 0:
            this_pos = open_list.pop()
            for n in this_pos.get_not_null_neighbors():
                if n not in visited:
                    visited.add(n)
                    open_list.append(n)
        covered_cells = {tuple(key.pos.values()) for key, _ in temp_board.full_positions.items()}
        print("nodes count: ", len(covered_cells))
        covered_and_visited_cells = {tuple(piece.pos.values()) for piece in visited}
        print("visited: ", len(covered_and_visited_cells))
        return len(covered_and_visited_cells) == len(covered_cells)

    def filter_valid_moves(self, piece: Piece, dest_poses: set):
        output = dest_poses.copy()
        for dest in dest_poses:
            source_x, source_y = piece.pos.values()
            self.move(piece, dest)
            if not Board.is_connected(self):
                output.remove(dest)
            self.move(piece, (source_x, source_y))
        return output


# -------------------------------
if __name__ == '__main__':
    b = Board()
    print(b.__str__(selects={(2, 3): 'Red', (0, 4): 'Blue'}))
    print(repr(b))
