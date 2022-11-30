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

def end_screen(screen):
    clock = pygame.time.Clock()
    tela_over = pygame.image.load(path.join(IMG_DIR,'game_over.png'))
    tela_over = pygame.transform.scale(tela_over, (840, 650))
    tela_over_rect = tela_over.get_rect()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = PLAYING
                    running = False
                    break
        screen.fill(BLACK)
        screen.blit(tela_over,tela_over_rect)
        pygame.display.flip()
