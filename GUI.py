import pygame

from Board import Board

# Initialise pygame
pygame.init()

# Set screen size
screen_size = screen_width, screen_height = (1000, 600)
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


def show_board():
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
            cell_image = pygame.image.load("images/Hexagonal.png")

            # Scale the image
            cell_image = pygame.transform.scale(cell_image, DEFAULT_CELL_SIZE)
            screen.blit(cell_image, (current_x, current_y))
            current_x += (3 / 2) * cell_width
        current_y += cell_height / 2


# -------------------------------
# Event loop
running = True
while running:
    # Background Color
    screen.fill((200, 230, 255))

    for event in pygame.event.get():
        # Close window event
        if event.type == pygame.QUIT:
            running = False

    show_board()
    pygame.display.update()
