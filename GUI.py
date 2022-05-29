import pygame

from Board import Board
from Pieces.Ant import Ant
from Pieces.Beetle import Beetle
from Pieces.Grasshopper import Grasshopper
from Pieces.QueenBee import QueenBee
from Pieces.Spider import Spider
from Player import Player

# _ _ - - - ~ ~ ~ ~ ^ ^ ^ NONE GRAPHICAL METHODS AND PROPERTIES ^ ^ ^ ~ ~ ~ ~ - - - _ _
# an instance of the Board class
board = Board()
board_rows = Board().ROWS
board_cols = Board().COLS

turn = 0
p1 = Player("P1", "White")
p2 = Player("P2", "Black")
debug = True


def create_piece_instance(piece_name, color, pos, player):
    global p1, p2
    piece_instance = None
    if piece_name == 'QB':
        piece_instance = QueenBee(color)
        in_turn_player.queen_bee = piece_instance
    elif piece_name == 'S':
        piece_instance = Spider(color)
    elif piece_name == 'B':
        piece_instance = Beetle(color)
    elif piece_name == 'G':
        piece_instance = Grasshopper(color)
    elif piece_name == 'A':
        piece_instance = Ant(color)
    # TODO: else: if the piece_name was incorrect...
    piece_instance.board = board

    # adding new pieces to the list of each player
    if p1.color == color:
        p1.inserted_pieces.append(piece_instance)
    else:
        p2.inserted_pieces.append(piece_instance)
    piece_instance.pos = pos
    piece_obj.player = player
    return piece_instance


# _ _ - - - ~ ~ ~ ~ ~ ^ ^ ^ GRAPHICAL METHODS AND PROPERTIES ^ ^ ^ ~ ~ ~ ~ ~ - - - _ _
# Initialise pygame
pygame.init()

# Set screen size
screen_size = screen_width, screen_height = (1100, 650)
screen = pygame.display.set_mode(screen_size)

# set title and icon for the graphical screen
pygame.display.set_caption("Hive Game-Board")
game_icon = pygame.image.load("images/queen_bee_icon.png")
pygame.display.set_icon(game_icon)

# Set the default size for the images
DEFAULT_CELL_SIZE = cell_width, cell_height = (50, 50)


def choose_image_for_cell(element):
    # default image of each cell
    cell_image = pygame.image.load("images/Hexagonal.png")

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

    return cell_image


def show_board():
    current_x = 0
    current_y = 0
    for i in range(2 * board_rows):
        if i % 2 == 0:
            current_x = 0
        else:
            current_x = 38  # TODO: this number is better to be calculated!

        for j in range(board_cols):

            element = None
            if i % 2 == 0:
                element = board.GAME_BOARD[i][2 * j]
            else:
                element = board.GAME_BOARD[i][2 * j + 1]

            cell_image = choose_image_for_cell(element)

            # Scale the image based on default image size
            cell_image = pygame.transform.scale(cell_image, DEFAULT_CELL_SIZE)
            screen.blit(cell_image, (current_x, current_y))

            current_x += (3 / 2) * cell_width
        current_y += cell_height / 2


# THIS PART NEEDS MORE FOCUS! NOT COMPLETED
'''
# index: queen_bee  /  spider  /  ant  /  grasshopper  /  beetle
white_pieces_image = []
black_pieces_image = []

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

init_pieces_image()
'''

# Event loop
running = True
while running:
    # -------------- graphical part --------------
    #  set background color
    # screen.fill((200, 230, 255))

    # shoe the game board and update the display to show recent changes
    # show_board()
    # pygame.display.update()

    for event in pygame.event.get():
        # Close window event
        if event.type == pygame.QUIT:
            running = False

    # - - - - - - - - - - - - - - - - - - - - - - - -
    # determine players turn and color
    in_turn_player = p1 if turn % 2 == 0 else p2
    color = 'White' if turn % 2 == 0 else 'Black'

    print(board)
    print(f"it is {color}'s turn")

    command = input('move or insert? ')
    if command == 'i':
        print('You have these pieces:')
        print(in_turn_player.pieces)
        if in_turn_player.should_insert_queen():
            print("You should insert queen. because this is your 4'th turn!")
            piece_name = "QB"
        else:
            piece_name = input('Choose one exist piece with enter id. ex) QB\n')
        piece_num = in_turn_player.pieces.get(piece_name, -1)
        if piece_num <= 0:
            print("You don't have this piece")
            continue

        # piece_obj will be an instance of the selected piece with proper color

        in_turn_player.pieces[piece_name] = piece_num - 1
        print(board.get_possible_insertions(in_turn_player))
        # validate pos
        pos = list(map(int, input('enter position in form of x y. ex) 5 4\n').split()))
        if not debug and board.GAME_BOARD[pos[0]][pos[1]]:
            print('destination cell is not empty!')
            continue
        piece_obj = create_piece_instance(piece_name, color, {'x': pos[0], 'y': pos[1]}, in_turn_player)
        board.add_piece(pos, piece_obj, color)
    elif command == 'm':
        if not in_turn_player.can_move():
            print('Your Queen is not in board!')
            continue
        print(board.get_move_sources(in_turn_player))
        x, y = map(int, input('insert x y to move it:\n').split())
        if not board.GAME_BOARD[x][y]:
            print('source cell is empty!')
            continue
        if not debug and board.GAME_BOARD[x][y].player != in_turn_player:
            print('this piece is not yours!')
            continue
        to_move_piece = board.GAME_BOARD[x][y]
        print(f"possible destinations: {to_move_piece.get_possible_movements()}")
        x, y = map(int, input('enter destination x y:\n').split())
        if not debug and board.GAME_BOARD[x][y]:
            print('destination cell is not empty!')
            continue

        if not board.move_if_can(to_move_piece, (x, y)):
            print("connectivity of hive is important!")
            continue

    else:
        print("ERROR: incorrect command")
        continue

    # check if each player is lost or not!
    if p1.is_lost():
        print(f'player {p2.name} is won!')
        break
    elif p2.is_lost():
        print(f'player {p1.name} is won!')
        break

    # update turn's number
    turn += 1
    in_turn_player.turn += 1
