# This file provides some functions for AI part of the game
from Pieces.Ant import Ant
from Pieces.Beetle import Beetle

# This function provides an estimated heuristic for the game.
# Using this method, minMax tree can be used in an efficient way!
""""
This function calculates heuristic for the player1.
So we should maximize heuristic for player1
and minimize for player2
"""


def get_heuristic(board, player1, player2, turn):
    h = 0

    # if player 1 is won the h is the biggest possible number
    if player2.is_lost:
        h += 1000000
        return h
    if player1.is_lost:
        h -= 1000000
        return h

    if get_number_of_inserted_beetles(player1) != 0:
        h += 30
    if is_queen_bee_inserted(player1):
        h += 120

    h += 50 * get_number_of_inserted_ants(player1)

    return h


# this method checks if a piece in the game board can move or not.
def is_piece_a_bridge(board, piece):
    pass


# This method returns number of beetles that player has inserted
def get_number_of_inserted_beetles(player):
    n = 0
    for i in player.inserted_pieces:
        if isinstance(i, Beetle):
            n += 1
    return n


# This method checks if the player has inserted his queen bee or not
def is_queen_bee_inserted(player):
    return player.can_move()


# This method returns number of inserted ants in the game board belongs to the player
def get_number_of_inserted_ants(player):
    n = 0
    for i in player.inserted_pieces:
        if isinstance(i, Ant):
            n += 1
    return n
