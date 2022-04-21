from Board import Board
from Pieces.Ant import Ant
from Pieces.Beetle import Beetle
from Pieces.Grasshopper import Grasshopper
from Pieces.Spider import Spider
from Player import Player
from Pieces.QueenBee import QueenBee

turn = 0
p1 = Player("P1", "White")
p2 = Player("P2", "Black")
board = Board()
debug = True
# TODO: refactor these
while True:
    in_turn_player = p1 if turn % 2 == 0 else p2
    color = 'Blue' if turn % 2 == 0 else 'Red'
    print(board)
    print(f'it is {color} turn')
    command = input('move or insert?\n')
    if command == 'insert':
        print('You have these pieces:')
        print(in_turn_player.pieces)
        if in_turn_player.should_insert_queen():
            print("You should insert queen. because this is your 4'th turn!")
            piece = "QB"
        else:
            piece = input('Choose one exist piece with enter id. ex) QB\n')
        piece_num = in_turn_player.pieces.get(piece, -1)
        if piece_num <= 0:
            print("You don't have this piece")
            continue
        piece_obj = None
        if piece == 'QB':
            piece_obj = QueenBee(color)
            in_turn_player.queen = piece_obj
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
        if not debug and board.GAME_BOARD[pos[0]][pos[1]]:
            print('destination cell is not empty!')
            continue
        piece_obj.pos['x'] = pos[0]
        piece_obj.pos['y'] = pos[1]
        piece_obj.player = in_turn_player
        board.add_piece(pos, piece_obj, color)
    elif command == 'move':
        if not in_turn_player.can_move():
            print('Your Queen is not in board!')
            continue
        x, y = map(int, input('insert x y to move it:\n').split())
        if not board.GAME_BOARD[x][y]:
            print('source cell is empty!')
            continue
        if not debug and board.GAME_BOARD[x][y].player != in_turn_player:
            print('this piece is not yours!')
            continue
        to_move_piece = board.GAME_BOARD[x][y]
        print(f"possible destinations: {to_move_piece.possible_movements()}")
        x, y = map(int, input('enter destination x y:\n').split())
        if not debug and board.GAME_BOARD[x][y]:
            print('destination cell is not empty!')
            continue
        copy_of_board = board.copy()
        copy_of_board.move(to_move_piece, (x, y), True)
        if Board.is_connected(copy_of_board):
            board.move(to_move_piece, (x, y), False)
        else:
            print("connectivity of hive is important!")
    if p1.is_lost():
        print(f'player {p2.name} is won!')
        break
    elif p2.is_lost():
        print(f'player {p1.name} is won!')
        break
    # Board.is_connected(board)
    turn += 1
    in_turn_player.turn += 1
