from Board import Board
from Pieces.Ant import Ant
from Pieces.Beetle import Beetle
from Pieces.Grasshopper import Grasshopper
from Pieces.Spider import Spider
from Player import Player
from Pieces.QueenBee import QueenBee

turn = 0
p1 = Player("P1")
p2 = Player("P2")
board = Board()
# TODO: refactor these
while True:
    in_turn_player = p1 if turn % 2 == 0 else p2
    color = 'Blue' if turn % 2 == 0 else 'Red'
    print(board)
    print('You have these pieces:')
    print(in_turn_player.pieces)
    piece = input('Choose one exist piece with enter id. ex) QB\n')
    piece_num = in_turn_player.pieces.get(piece, -1)
    if piece_num <= 0:
        print("You don't have this piece")
        continue
    piece_obj = None
    if piece == 'QB':
        piece_obj = QueenBee(color)
    elif piece == 'S':
        piece_obj = Spider(color)
    elif piece == 'B':
        piece_obj = Beetle(color)
    elif piece == 'G':
        piece_obj = Grasshopper(color)
    elif piece == 'A':
        piece_obj = Ant(color)
    piece_obj.board = board
    in_turn_player.pieces[piece] = piece_num - 1
    print(board.get_possible_insertions(in_turn_player))
    # validate pos
    pos = list(map(int, input('enter position in form of x y. ex) 5 4\n').split()))
    piece_obj.pos['x'] = pos[0]
    piece_obj.pos['y'] = pos[1]
    piece_obj.player = in_turn_player
    board.add_piece(pos, piece_obj, color)
    turn += 1