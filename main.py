import pygame
import random

pygame.init()

running = True
screen = pygame.display.set_mode((256, 512))

ENEMY_SPACE = pygame.image.load('data/enemy_space_shuttle.png')
ENEMY_SPACE = pygame.transform.scale(ENEMY_SPACE, (30, 30))

SPACE = pygame.image.load('data/space shuttle.png')
SPACE = pygame.transform.scale(SPACE, (40, 40))
SPACEX = 220
SPACEY = 450

BACKGROUND = pygame.image.load('data/space_background.png')

x_val = random.randint(1, 230)
y_val = 0

green = (0, 255, 0)
blue = (0, 0, 128)

increasing = 1

sc = 0
font = pygame.font.Font('freesansbold.ttf', 16)
text = font.render(f'Score:{sc}', True, green, blue)
textrect = text.get_rect()

clock = pygame.time.Clock()

ammo = pygame.image.load('data/space_shuttle_ammo_01.png')
ammo = pygame.transform.scale(ammo, (7, 7))

ammo_x = 800
ammo_y = 800

ammo_state = True

while running:
    y_val += increasing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if SPACEX > -10:
            SPACEX -= increasing + 1

    if keys[pygame.K_d]:
        if SPACEX < 230:
            SPACEX += increasing + 1

    if y_val > 475:
        x_val = random.randint(1, 230)
        y_val = 0
        increasing = 1
        sc = 0
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render(f'Score:{sc}', True, green, blue)
        textrect = text.get_rect()

    if keys[pygame.K_w]:
        if ammo_state:
            ammo_y = SPACEY + 10
            ammo_x = SPACEX + 13
            ammo_state = False

    if y_val - ammo_y >= 1 and -5 < (ammo_x - x_val) < 25:
        ammo_state = True
        ammo_x = 800
        ammo_y = 800
        increasing += 0.5
        x_val = random.randint(1, 230)
        y_val = 0
        sc += 1
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render(f'Score:{sc}', True, green, blue)
        textrect = text.get_rect()

    if ammo_y <= 0:
        ammo_state = True

    ammo_y -= increasing
    pygame.display.flip()
    screen.blit(BACKGROUND, (0,0))
    screen.blit(ammo, (ammo_x, ammo_y))
    screen.blit(SPACE, (SPACEX, SPACEY))
    screen.blit(ENEMY_SPACE, (x_val, y_val))
    screen.blit(text, textrect)
    clock.tick(60)