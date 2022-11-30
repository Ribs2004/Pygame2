import pygame
import random
import sys
from os import path

IMG_DIR = path.join(path.dirname(__file__),'img')
BLACK = (0,0,0)
FPS = 30
INIT = 0
GAME = 1
QUIT = 2

DONE = 0
PLAYING = 1
EXPLODING = 2

state = PLAYING

def init_screen(screen):
    clock = pygame.time.Clock()
    background = pygame.image.load(path.join(IMG_DIR,'ciadade-init-2.png'))
    background = pygame.transform.scale(background, (840, 650))
    background_rect = background.get_rect()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                state = PLAYING
                running = False
                break
        screen.fill(BLACK)
        screen.blit(background,background_rect)
        pygame.display.flip()
