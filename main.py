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
playerX = 360
playerY = 480
playerX_change = 0

def player(x,y):
    SCREEN.blit(playerImg, (x, y))


#Game loop
running = True
while running:
    #changing background color-RGB
    SCREEN.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke pressed is left or right arrow key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
