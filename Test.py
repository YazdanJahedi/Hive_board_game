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


# game loop (screen loop)
running = True
while running:
    # screen base color RGB
    screen.fill((200, 230, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    imgX += imgX_changer
    imgY += imgY_changer
    img_display(imgX, imgY)
    pygame.display.update()

# 30:00
