import pygame

#initialize the pygame
pygame.init()

#create the screen
SCREENWIDTH = 600
SCREENHEIGHT = 800
SCREEN = pygame.display.set_mode((SCREENHEIGHT, SCREENWIDTH))

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #changing background color-RGB
    SCREEN.fill((0,0,0))
    pygame.display.update()
