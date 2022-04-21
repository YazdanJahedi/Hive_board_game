import pygame

from Board import Board
from Pieces.Ant import Ant
from Pieces.Beetle import Beetle
from Pieces.Grasshopper import Grasshopper
from Pieces.QueenBee import QueenBee
from Pieces.Spider import Spider

# Initialise pygame
from Player import Player

pygame.init()

# Set screen size
screen_size = screen_width, screen_height = (1100, 650)
screen = pygame.display.set_mode(screen_size)

# Title and icon
pygame.display.set_caption("Hive Game-Board")
game_icon = pygame.image.load("images/queen_bee_icon.png")
pygame.display.set_icon(game_icon)

# -------------------------------
board = Board()
board_rows = Board().ROWS
board_cols = Board().COLS

# Set the size for the image
DEFAULT_CELL_SIZE = cell_width, cell_height = (50, 50)

current_x = 0
current_y = 0


def show_board(x, y):
    is_an_image_clicked = False

    global current_y, current_x
    current_x = 0
    current_y = 0
    for i in range(2 * board_rows):
        if i % 2 == 0:
            current_x = 0
        else:
            current_x = 38  # TODO: this number is better to be calculated!

        for j in range(board_cols):
            # loading image
            # default image of each cell
            cell_image = pygame.image.load("images/Hexagonal.png")

            # ------------ select correct image for each element -----------
            element = None
            if i % 2 == 0:
                element = board.GAME_BOARD[i][2 * j]
            else:
                element = board.GAME_BOARD[i][2 * j + 1]

            if element == 1:
                cell_image = pygame.image.load("images/Hexagonal_blue.png")
            elif isinstance(element, Ant):
                if element.color[0] == 'W':
                    cell_image = pygame.image.load("images/ant_white.png")
                else:
                    cell_image = pygame.image.load("images/ant_black.png")
            elif isinstance(element, Beetle):
                if element.color[0] == 'W':
                    cell_image = pygame.image.load("images/insect_white.png")
                else:
                    cell_image = pygame.image.load("images/insect_black.png")
            elif isinstance(element, Grasshopper):
                if element.color[0] == 'W':
                    cell_image = pygame.image.load("images/grasshopper_white.png")
                else:
                    cell_image = pygame.image.load("images/grasshopper_black.png")
            elif isinstance(element, QueenBee):
                if element.color[0] == 'W':
                    cell_image = pygame.image.load("images/queen_bee_white.png")
                else:
                    cell_image = pygame.image.load("images/queen_bee_black.png")
            elif isinstance(element, Spider):
                if element.color[0] == 'W':
                    cell_image = pygame.image.load("images/spider_white.png")
                else:
                    cell_image = pygame.image.load("images/spider_black.png")
            # -------------------------------------------------------------------

            # Scale the image
            cell_image = pygame.transform.scale(cell_image, DEFAULT_CELL_SIZE)
            screen.blit(cell_image, (current_x, current_y))

            if cell_image.get_rect().collidepoint(x, y):
                print(" ~~~~")
                is_an_image_clicked = True

            current_x += (3 / 2) * cell_width
        current_y += cell_height / 2

    if is_an_image_clicked:
        print("** clicked on cell at ", x, y)


# index: queen_bee  /  spider  /  ant  /  grasshopper  /  beetle
white_pieces_image = []
black_pieces_image = []

'''
def is_clicked_on_pieces(x, y):
    for i in white_pieces_image:
        if i.get_rect().collidepoint(x, y):
            print("     White Piece", i)
            break

    for i in black_pieces_image:
        if i.get_rect().collidepoint(x, y):
            print("     Black Piece", i)
            break
'''


def init_pieces_image():
    # load image
    queen_bee_white = pygame.image.load("images/queen_bee_white.png")
    # Scale the image
    queen_bee_white = pygame.transform.scale(queen_bee_white, DEFAULT_CELL_SIZE)
    white_pieces_image.append(queen_bee_white)

    spider_white = pygame.image.load("images/spider_white.png")
    spider_white = pygame.transform.scale(spider_white, DEFAULT_CELL_SIZE)
    white_pieces_image.append(spider_white)

    ant_white = pygame.image.load("images/ant_white.png")
    ant_white = pygame.transform.scale(ant_white, DEFAULT_CELL_SIZE)
    white_pieces_image.append(ant_white)

    grasshopper_white = pygame.image.load("images/grasshopper_white.png")
    grasshopper_white = pygame.transform.scale(grasshopper_white, DEFAULT_CELL_SIZE)
    white_pieces_image.append(grasshopper_white)

    beetle_white = pygame.image.load("images/insect_white.png")
    beetle_white = pygame.transform.scale(beetle_white, DEFAULT_CELL_SIZE)
    white_pieces_image.append(beetle_white)
    # - - - - - - - - - - - - - - - - - - -
    queen_bee_black = pygame.image.load("images/queen_bee_black.png")
    queen_bee_black = pygame.transform.scale(queen_bee_black, DEFAULT_CELL_SIZE)
    black_pieces_image.append(queen_bee_black)

    spider_black = pygame.image.load("images/spider_black.png")
    spider_black = pygame.transform.scale(spider_black, DEFAULT_CELL_SIZE)
    black_pieces_image.append(spider_black)

    ant_black = pygame.image.load("images/ant_black.png")
    ant_black = pygame.transform.scale(ant_black, DEFAULT_CELL_SIZE)
    black_pieces_image.append(ant_black)

    grasshopper_black = pygame.image.load("images/grasshopper_black.png")
    grasshopper_black = pygame.transform.scale(grasshopper_black, DEFAULT_CELL_SIZE)
    black_pieces_image.append(grasshopper_black)

    beetle_black = pygame.image.load("images/insect_black.png")
    beetle_black = pygame.transform.scale(beetle_black, DEFAULT_CELL_SIZE)
    black_pieces_image.append(beetle_black)


def show_pieces():
    starting_x = 800
    starting_y = 50
    for i in white_pieces_image:
        screen.blit(i, (starting_x, starting_y))
        starting_x += 60

    starting_x = 800
    starting_y = 150
    for i in black_pieces_image:
        screen.blit(i, (starting_x, starting_y))
        starting_x += 60


# -------------------------------
init_pieces_image()

turn = 0
p1 = Player("P1", "White")
p2 = Player("P2", "Black")
debug = True
# Event loop
running = True
while running:
    # Background Color
    print("1")
    screen.fill((200, 230, 255))
    x, y = (-10, -10)

    show_board(x, y)
    # show_pieces()
    pygame.display.update()
    print("2")
    for event in pygame.event.get():
        # Close window event
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #    x, y = event.pos
        # print("clicked on ", x, y)
        # if event.type == pygame.MOUSEBUTTONUP:
        #    x, y = event.pos
        # print("mouse released on  ", x, y)
    print("3")
    in_turn_player = p1 if turn % 2 == 0 else p2
    color = 'White' if turn % 2 == 0 else 'Black'
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


