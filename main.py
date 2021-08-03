import pygame

#initialize the pygame
pygame.init()

#create the screen
SCREENWIDTH = 800
SCREENHEIGHT = 600
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('player.png')
playerX = 350
playerY = 480

def player():
    SCREEN.blit(playerImg, (playerX, playerY))


#Game loop
running = True
while running:
    #changing background color-RGB
    SCREEN.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()
