import pygame
import random
from os import path
from main import PLAYING

IMG_DIR = path.join(path.dirname(__file__),'img')
BLACK = (0,0,0)
FPS = 30
INIT = 0
GAME = 1
QUIT = 2

def init_screen(screen):
    clock = pygame.time.Clock()
    background = pygame.image.load(path.join(IMG_DIR,'ciadade-init-2.png'))
    background_rect = background.get_rect()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    state = PLAYING
        screen.fill(BLACK)
        screen.blit(background,background_rect)
        pygame.display.flip()
    return state