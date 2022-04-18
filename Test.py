import pygame

# initial the pygame
pygame.init()

# create the screen (x, y)
screen = pygame.display.set_mode((1000, 600))

# title and icon
pygame.display.set_caption("Hive Game Board")
icon = pygame.image.load("images/queen_bee_icon.png")
pygame.display.set_icon(icon)

# adding image
img = pygame.image.load("images/spider.png")
imgX = 400
imgY = 400
imgX_changer = 0
imgY_changer = 0


def img_display(x, y):
    screen.blit(img, (x, y))


# adding a text
text_message = "this is a test"
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10


def show_text(x, y):
    text = font.render(text_message, True, (0, 0, 0))
    screen.blit(text, (x, y))


# game loop (screen loop)
running = True
while running:
    # screen base color RGB
    screen.fill((200, 230, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # movement by arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("right key is pressed")
                imgX_changer += 0.3
            if event.key == pygame.K_LEFT:
                print("left key is pressed")
                imgX_changer -= 0.3
            if event.key == pygame.K_UP:
                print("up key is pressed")
                imgY_changer -= 0.3
            if event.key == pygame.K_DOWN:
                print("down key is pressed")
                imgY_changer += 0.3
        if event.type == pygame.KEYUP:
            print("key is released!")
            imgX_changer = 0
            imgY_changer = 0

    # limit x in the page
    if imgX <= 0:
        imgX = 0
    elif imgX >= 1000 - icon.get_height():
        imgX = 1000 - icon.get_height()

    # limit y in the page
    if imgY <= 0:
        imgY = 0
    elif imgY >= 600 - icon.get_width():
        imgY = 600 - icon.get_width()

    imgX += imgX_changer
    imgY += imgY_changer
    img_display(imgX, imgY)
    show_text(textX, textY)
    pygame.display.update()

# 30:00
