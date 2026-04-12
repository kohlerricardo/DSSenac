import settings
import pygame
from src.entities.player import Player
from src.entities.coin import Coin
from src.ui.hud import HUD
from src.ui.menu import Menu
from src.ui.pause import Pause
from src.ui.gameplay import Gameplay
import random
from src.engine.coin_spawner import CoinSpawner

# Função auxiliar para criar moedas em locais aleatórios.
def spawn_coin(coins_group):
    for i in range(settings.COIN_COUNT):
        # Utiliza a função random para gerar coordenadas aleatórias 
        #dentro dos limites da tela, considerando o tamanho da moeda.
        x = random.randint(0, settings.WIDTH - 16) # 16 é o tamanho da moeda, para evitar spawn fora da tela.
        y = random.randint(0, settings.HEIGHT - 16)
        coin = Coin(x, y, i+1)
        coins_group.add(coin) # Adiciona a moeda ao grupo de gerenciamento.

def main():
    pygame.init() # Inicializa todos os módulos do Pygame.
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption(settings.TITLE)
    clock = pygame.time.Clock() # Objeto para controlar o tempo/FPS.
    status = "MENU" # Estado inicial do jogo (pode ser "MENU", "PLAYING", "GAME_OVER", etc).
    estados = {
        "MENU": Menu(),
        "PAUSED": Pause(),
        "PLAYING": Gameplay("Player1")
    }

    running = True
    
    while running:
        # Calcula quanto tempo passou desde o último frame (em segundos).
        dt = clock.tick(settings.FPS) / 1000  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if event.type == pygame.KEYDOWN:
            if status == "MENU" and event.key == pygame.K_RETURN:
                status = "PLAYING" # Inicia o jogo ao pressionar ENTER no menu.
            elif status == "PLAYING" and event.key == pygame.K_ESCAPE:
                status = "PAUSED" # Permite pausar o jogo com ESC.
                print("Jogo pausado. Pressione 'P' para continuar.")
            elif status == "PAUSED" and event.key == pygame.K_ESCAPE:
                status = "PLAYING" # Permite pausar o jogo com ESC.
                print("Continuando o jogo.")
        cena = estados.get(status)
        cena.update(dt) # Atualiza a lógica da cena atual (menu, pausa, etc).
        cena.draw(screen) # Desenha a cena atual na tela.
        pygame.display.flip() # Atualiza o monitor com o que foi desenhado.

    pygame.quit()

if __name__ == "__main__":
    main()