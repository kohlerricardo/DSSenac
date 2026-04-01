import settings
import pygame
from src.entities.player import Player
from src.entities.coin import Coin
from src.ui.hud import HUD
import random

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
    
    # Grupos de Sprites: Essenciais para desenho e colisão em massa.
    players_group = pygame.sprite.Group()
    coins_group = pygame.sprite.Group()
    
    player = Player("Player1")
    players_group.add(player)
    spawn_coin(coins_group) # Gera as moedas iniciais.

    # Configuração de Texto (Interface/UI).
    hud = HUD() # Cria o objeto HUD para gerenciar a interface de pontuação.

    # fonte = pygame.font.SysFont("Monospace", 15, True, True) # Fonte negrito e itálico.
    # formatacao_texto = fonte.render("Score: 0", False, (255, 255, 255)) # Renderiza o texto inicial do Score.
    running = True
    while running:
        # Calcula quanto tempo passou desde o último frame (em segundos).
        dt = clock.tick(settings.FPS) / 1000  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(settings.BG_COLOR) # Limpa a tela com a cor de fundo.
        
        # DETECÇÃO DE COLISÃO:
        # Verifica se o 'player' tocou em algo do grupo 'coins'. 
        # O 'True' indica que a moeda deve ser excluída (kill) se houver toque.
        colision = pygame.sprite.spritecollide(player, coins_group, True)
        
        if colision:
            for coin in colision:
                player.increase_score(coin.points) # Aumenta o score no objeto player.
            
            # Atualiza o texto visual do Score após a coleta.
            # mensagem = f"Score: {player.score}"
            # formatacao_texto = fonte.render(mensagem, False, (255, 255, 255))
            
        # screen.blit(formatacao_texto, (10, 10)) # Desenha o texto na tela.

        # Se todas as moedas acabarem, gera uma nova "onda".
        if len(coins_group) == 0:
            spawn_coin(coins_group)
            
        # Atualização de lógica e desenho via GRUPOS.
        players_group.update(dt)    # Move o player.
        players_group.draw(screen)  # Desenha o player.
        coins_group.update(dt)      # (Moedas são estáticas, mas o grupo exige).
        coins_group.draw(screen)    # Desenha as moedas restantes.
        hud.draw(screen,player)              # Desenha o HUD (pontuação) na tela.

        pygame.display.flip() # Atualiza o monitor com o que foi desenhado.

    pygame.quit()

if __name__ == "__main__":
    main()