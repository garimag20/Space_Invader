import pygame

#initialize the pygame
pygame.init()

#create the screen
SCREENWIDTH = 600
SCREENHEIGHT = 800
SCREEN = pygame.display.set_mode((SCREENHEIGHT, SCREENWIDTH))

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
