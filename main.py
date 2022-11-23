# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Variáveis
LENGTH = 840
WIDTH = 650
CAR_LENGTH = 84
CAR_WIDTH = 65
# ----- Gera tela principal
window = pygame.display.set_mode((840, 650))
pygame.display.set_caption('Need For Speed 2D')

# ----- Inicia Assets
def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('img/background.png').convert()
    assets['imagem_carro'] = pygame.image.load('img/carro.png').convert_alpha()
    assets['imagem_carro_transform'] = pygame.transform.scale(assets['imagem_carro'],(CAR_LENGTH,CAR_WIDTH))
    return assets
# ----- Inicia estruturas de dados
game = True
# ----- Definindo os novos tipos
class Car(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['imagem_carro']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = LENGTH - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets

    def update(self):
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
assets = load_assets()
# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYUP:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 255))  # Preenche com a cor branca
    window.blit(assets['background'], (0, 0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

