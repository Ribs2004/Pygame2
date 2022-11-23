# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from random import *

pygame.init()

# ----- Variáveis
HEIGHT = 840
WIDTH = 650
CAR_LENGTH = 140
CAR_WIDTH = 105
# ----- Gera tela principal
window = pygame.display.set_mode((840, 650))
pygame.display.set_caption('Need For Speed 2D')

# ----- Inicia Assets 
background = pygame.image.load('img/background.png').convert()
player_car = pygame.image.load('img/carro.png').convert_alpha()
player_car = pygame.transform.scale(player_car ,(CAR_LENGTH,CAR_WIDTH))

# ----- Inicia estruturas de dados
game = True

# ----- Variável para ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30
# ----- Definindo os novos tipos
class Car(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 378
        self.rect.y = 500
        self.speedx = 0

    def update(self):
            self.rect.x += self.speedx

            # Mantem dentro da tela
            if self.rect.right > WIDTH+75:
                self.rect.right = WIDTH+75
            if self.rect.left < 120:
                self.rect.left = 120

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image =img
        self.rect = self.image.get_rect()
        self.rect.x = randint(105, 630)
        self.rect.y = -100
        self.speedy = randint(10, 22)
    
    def update(self):
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:
            self.rect.x = randint(105, 630)
            self.rect.y = -100

#assets = load_assets()
all_sprites = pygame.sprite.Group()
all_obstacles = pygame.sprite.Group()
carro = Car(player_car)
all_sprites.add(carro)
for c in range (0, 4):
    carro_obstaculo = Obstacles(player_car)
    all_sprites.add(carro_obstaculo)
    all_obstacles.add(carro_obstaculo)
all_sprites.add(carro)


# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                carro.speedx -= 14
            if event.key == pygame.K_RIGHT:
                carro.speedx += 14
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                carro.speedx += 14
            if event.key == pygame.K_RIGHT:
                carro.speedx -= 14
        

    all_sprites.update()
    window.blit(background, (0, 0))
    all_sprites.draw(window)
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

