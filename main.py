# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Variáveis
LENGTH = 840
WIDTH = 650
CAR_LENGTH = 140
CAR_WIDTH = 105
# ----- Gera tela principal
window = pygame.display.set_mode((840, 650))
pygame.display.set_caption('Need For Speed 2D')

# ----- Inicia Assets 
background = pygame.image.load('img/background.png').convert()
img = pygame.image.load('img/carro.png').convert_alpha()
img_transform = pygame.transform.scale(img ,(CAR_LENGTH,CAR_WIDTH))

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

#assets = load_assets()
all_sprites = pygame.sprite.Group()
carro = Car(img_transform)
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
                carro.speedx -= 8
            if event.key == pygame.K_RIGHT:
                carro.speedx += 8
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                carro.speedx += 8
            if event.key == pygame.K_RIGHT:
                carro.speedx -= 8
        

    all_sprites.update()
    # ----- Gera saídas
    window.fill((0, 0, 255))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    all_sprites.draw(window)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

