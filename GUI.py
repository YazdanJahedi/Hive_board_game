import pygame

from Board import Board
from Pieces.Ant import Ant

# Initialise pygame
from Pieces.Beetle import Beetle
from Pieces.Grasshopper import Grasshopper
from Pieces.QueenBee import QueenBee
from Pieces.Spider import Spider

pygame.init()

# Set screen size
screen_size = screen_width, screen_height = (1100, 650)
screen = pygame.display.set_mode(screen_size)

# Title and icon
pygame.display.set_caption("Hive Game-Board")
game_icon = pygame.image.load("images/queen_bee_icon.png")
pygame.display.set_icon(game_icon)

# -------------------------------
board = Board().GAME_BOARD
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
                element = board[i][2 * j]
            else:
                element = board[i][2 * j + 1]

            if element == 1:
                cell_image = pygame.image.load("images/Hexagonal_blue.png")
            elif isinstance(element, Ant):
                if element.color == 'w':
                    cell_image = pygame.image.load("images/ant_white.png")
                else:
                    cell_image = pygame.image.load("images/ant_black.png")
            elif isinstance(element, Beetle):
                if element.color == 'w':
                    cell_image = pygame.image.load("images/insect_white.png")
                else:
                    cell_image = pygame.image.load("images/insect_black.png")
            elif isinstance(element, Grasshopper):
                if element.color == 'w':
                    cell_image = pygame.image.load("images/grasshopper_white.png")
                else:
                    cell_image = pygame.image.load("images/grasshopper_black.png")
            elif isinstance(element, QueenBee):
                if element.color == 'w':
                    cell_image = pygame.image.load("images/queen_bee_white.png")
                else:
                    cell_image = pygame.image.load("images/queen_bee_black.png")
            elif isinstance(element, Spider):
                if element.color == 'w':
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

# Event loop
running = True
c = 0
while running:
    # Background Color
    screen.fill((200, 230, 255))
    x, y = (-10, -10)

    for event in pygame.event.get():
        # Close window event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # print("clicked on ", x, y)
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            # print("mouse released on  ", x, y)

    show_board(x, y)
    #show_pieces()
    pygame.display.update()
