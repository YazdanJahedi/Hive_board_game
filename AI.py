# This file provides some functions for AI part of the game
import Board
import GUI
from Pieces.Ant import Ant
from Pieces.Beetle import Beetle
import Minimax

""""
# This function provides an estimated heuristic for the game.
# Using this method, minMax tree can be used in an efficient way!
from Pieces.Piece import Piece
This function calculates heuristic for the player1.
So we should maximize heuristic for player1
and minimize for player2
"""


class AI:
    def __init__(self, player):
        self.player = player

    def get_heuristic(self, board, player1, player2):
        h = 0

        # if player 1 is won the h is the biggest possible number
        if player2.is_lost:
            h += 1000000
            return h
        if player1.is_lost:
            h -= 1000000
            return h

        if self.get_number_of_inserted_beetles(player1) != 0:
            h += 30
        if self.is_queen_bee_inserted(player1):
            h += 120
        if self.can_bee_queen_move(board, player1):
            h += 170

        # todo : beetle on beetle ??
        # todo : number of neighbours of queen bee ??

        h += 50 * self.get_number_of_inserted_ants(player1)
        h += 100 * self.get_number_of_locked_pieces(board, player2)
        # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
        if self.get_number_of_inserted_beetles(player2) != 0:
            h -= 30
        if self.is_queen_bee_inserted(player2):
            h -= 120
        if self.can_bee_queen_move(board, player2):
            h -= 170

        h -= 50 * self.get_number_of_inserted_ants(player2)
        h -= 100 * self.get_number_of_locked_pieces(board, player1)

        return h

    # this method checks if a piece in the game board can move or not.
    def is_piece_a_bridge(self, board, piece):
        possible_movements = piece.get_possible_movements()
        for i in possible_movements:
            pre_pos = piece.pos
            board.move(piece, i)
            if board.is_connected():
                board.move(piece, pre_pos)
                return False
            board.move(piece, pre_pos)

        return True

    # This method returns number of beetles that player has inserted
    def get_number_of_inserted_beetles(self, player):
        n = 0
        for i in player.inserted_pieces:
            if isinstance(i, Beetle):
                n += 1
        return n

    # This method checks if the player has inserted his queen bee or not
    def is_queen_bee_inserted(self, player):
        return player.can_move()

    # This method returns number of inserted ants in the game board belongs to the player
    def get_number_of_inserted_ants(self, player):
        n = 0
        for i in player.inserted_pieces:
            if isinstance(i, Ant):
                n += 1
        return n

    # This method returns number of locked pieces that can not to move, for given player!
    def get_number_of_locked_pieces(self, board, player):
        n = 0
        for i in player.inserted_pieces:
            if self.is_piece_a_bridge(board, i):
                n += 1
        return n

    # This function checks if queen bee piece can move or not
    def can_bee_queen_move(self, board, player):
        if not self.is_queen_bee_inserted(player) or self.is_piece_a_bridge(board, player.queen_bee):
            return False
        return True

    def make_tree(self, root_board: Board.Board, tree: Minimax.MinimaxTree, node: Minimax.Node):

        for piece_name in self.player.get_valid_pieces():
            for pi in node.state.get_possible_insertions(self.player):
                pos = {'x': pi[0], 'y': pi[1]}
                piece = GUI.create_piece_instance(piece_name, self.player.color, pos, self.player)
                new_node = Minimax.Node(Board.Board(root_board, root_board.full_positions))
                node.add_child(new_node)
                new_node.state.add_piece(pos, piece, self.player.color)

        # insertion section
        # I wanna get all insertion conditions and add that state to this node children

        # movement section
        # I wanna get all movement conditions and add that state to this node children
