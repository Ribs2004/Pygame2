# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from random import *
from init_screen import init_screen, state, DONE, PLAYING
from end_screen import end_screen


pygame.init()

# ----- Variáveis
HEIGHT = 840
WIDTH = 650
CAR_LENGTH = 50
CAR_WIDTH = 100
# ----- Ge ra tela principal
window = pygame.display.set_mode((840, 650))
pygame.display.set_caption('Need For Speed 2D')

# ----- Inicia Assets 
background = pygame.image.load('img/background.png').convert()
player_car = pygame.image.load('img/carro.png').convert_alpha()
player_car = pygame.transform.scale(player_car ,(CAR_LENGTH,CAR_WIDTH))
obstacle_car = pygame.image.load('img/car_obstacle.png').convert_alpha()
obstacle_car = pygame.transform.scale(obstacle_car, (CAR_LENGTH, CAR_WIDTH))
score_font = pygame.font.Font('font/PressStart2P.ttf',28)

explosion_anim = []

for i in range(9):
    filename = 'img/regularExplosion{:02d}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img,(40,40))
    explosion_anim.append(img)

#Carrega os sons do jogo
pygame.mixer.music.set_volume(0.5)
crash_sound = pygame.mixer.Sound('snd/car_crash.wav')
corrida_musica = pygame.mixer.Sound('snd/musica_corrida.wav')

# ----- Inicia estruturas de dados
game = True
score = 0
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
            if self.rect.right > WIDTH+40:
                self.rect.right = WIDTH+40
            if self.rect.left < 150:
                self.rect.left = 150

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image =img
        self.rect = self.image.get_rect()
        self.rect.x = randint(105, 630)
        self.rect.y = -1500 + randint(0, 1400)
        self.speedy = randint(16, 22)
    
    def update(self):
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:
            self.rect.x = randint(105, 630)
            self.rect.y = -100

class Crash(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        #Armazena a animação de acidente
        self.explosion_anim = explosion_anim
        #Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0
        self.image = self.explosion_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        self.frame_ticks = 50
    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image  = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

#assets = load_assets()

while True:

    all_sprites = pygame.sprite.Group()
    all_obstacles = pygame.sprite.Group()
    carro = Car(player_car)
    all_sprites.add(carro)
    for c in range (0, 4):
        carro_obstaculo = Obstacles(obstacle_car)
        all_sprites.add(carro_obstaculo)
        all_obstacles.add(carro_obstaculo)
    all_sprites.add(carro)
    state = PLAYING

    init_screen(window)
    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)
        score += 0.033333

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
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

        if state == PLAYING:
            corrida_musica.play()
            hits = pygame.sprite.spritecollide(carro , all_obstacles, True)
            if len(hits) > 0:
                carro.kill()
                explosao = Crash(carro.rect.center)
                all_sprites.add(explosao)
                all_sprites.update()
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
                crash_sound.play()
                state = DONE
                

            if state == DONE:
                score = 0

            
            
        

        all_sprites.update()
        window.blit(background, (0, 0))
        text_surface = score_font.render("{}".format(int(score)),True,(255,255,0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH/2,10)
        all_sprites.draw(window)
        window.blit(text_surface,(60,60))
        pygame.display.update()  # Mostra o novo frame para o jogador
    end_screen(window)
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

