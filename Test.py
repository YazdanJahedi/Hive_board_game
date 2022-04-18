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
imgX = 0
imgY = 0


def img_display():
    screen.blit(img, (imgX, imgY))


# game loop (screen loop)
running = True
while running:
    # screen base color RGB
    screen.fill((200, 230, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    img_display()
    pygame.display.update()

# 30:00