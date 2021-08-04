import pygame
import random
# initialize the pygame
pygame.init()

# create the screen
SCREENWIDTH = 800
SCREENHEIGHT = 600
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# Background
background = pygame.image.load('background.png')

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 360
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 3.5
enemyY_change = 40

# Bullet
# Ready - you can't see the bullet on the screen
# Fire - the bullet is moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 3.5
bulletY_change = 10
bullet_state = "ready"


def enemy(x, y):
    SCREEN.blit(enemyImg, (x, y))


def player(x, y):
    SCREEN.blit(playerImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    SCREEN.blit(bulletImg, (x+16, y+10))


# Game loop
running = True
while running:
    # changing background color-RGB
    SCREEN.fill((0, 0, 0))
    # background image
    SCREEN.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke pressed is left or right arrow key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.8
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.8
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # checking for boundaries such that spaceship doesn't go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # 800-64 ->64 - size of spaceship
        playerX = 736

    # enemy
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 3.5
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3.5
        enemyY += enemyY_change

    #Bullet Movement
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
