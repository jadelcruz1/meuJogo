import pygame as pg
import random
import sys

pg.init()

# Configurações da janela
LARGURA = 800
ALTURA = 600
TELA = pg.display.set_mode((LARGURA, ALTURA))
pg.display.set_caption("Space Escape - Demo")

# Carregar imagens
player_img = pg.image.load("assets/player.png")
player_img = pg.transform.scale(player_img, (60, 60))

enemy_img = pg.image.load("assets/enemy.png")
enemy_img = pg.transform.scale(enemy_img, (50, 50))

background_img = pg.image.load("assets/background.png")
background_img = pg.transform.scale(background_img, (LARGURA, ALTURA))

menu_img = pg.image.load("assets/menu.png")
menu_img = pg.transform.scale(menu_img, (LARGURA, ALTURA))

# Sons (opcional)
# pygame.mixer.Sound("assets/som_exemplo.wav").play()

# Jogador
player_x = LARGURA // 2
player_y = ALTURA - 80
player_vel = 7

# Lista de inimigos
enemigos = []
enemy_vel = 5

fonte = pg.font.SysFont("Arial", 30)

def criar_inimigo():
    x = random.randint(0, LARGURA - 40)
    y = -50
    enemigos.append([x, y])

def menu():
    while True:
        TELA.blit(menu_img, (0, 0))

        titulo = fonte.render("SPACE ESCAPE - DEMO", True, (255, 255, 255))
        comandos = fonte.render("Controles: ← → para mover | ENTER para iniciar", True, (255, 255, 0))

        TELA.blit(titulo, (220, 100))
        TELA.blit(comandos, (120, 150))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    return

        pg.display.update()

def jogo():
    global player_x, player_y, enemigos

    clock = pg.time.Clock()
    running = True

    while running:
        clock.tick(60)
        TELA.blit(background_img, (0, 0))

        # Eventos
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        # Movimentação
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and player_x > 0:
            player_x -= player_vel
        if keys[pg.K_RIGHT] and player_x < LARGURA - 60:
            player_x += player_vel

        # Criar inimigos
        if random.randint(1, 20) == 1:
            criar_inimigo()

        # Atualizar inimigos
        for enemy in enemigos:
            enemy[1] += enemy_vel

            # Colisão
            if enemy[1] > player_y - 40 and player_x < enemy[0] < player_x + 60:
                running = False

            # Remover inimigos fora da tela
            if enemy[1] > ALTURA:
                enemigos.remove(enemy)

            TELA.blit(enemy_img, (enemy[0], enemy[1]))

        # Desenhar jogador
        TELA.blit(player_img, (player_x, player_y))

        pg.display.update()

while True:
    menu()
    juego_reset = []
    enemigos = []
    player_x = LARGURA // 2
    jogo()
