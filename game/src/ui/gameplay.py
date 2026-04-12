import pygame
from src.engine.coin_spawner import CoinSpawner
from src.engine.colision_engine import CollisionEngine
from src.ui.hud import HUD
from settings import BG_COLOR
from src.entities.box import Box    
class Gameplay:
    def __init__(self,player_name):
        # Inicialização de elementos do jogo, como player, moedas, etc.
        self.coins_group = pygame.sprite.Group() # Grupo para gerenciar as moedas.
        # self.box_group = pygame.sprite.Group() # Placeholder para futuras caixas ou obstáculos.
        self.all_sprites = pygame.sprite.Group() # Grupo para gerenciar todos os sprites do jogo (player, moedas, etc).
        self.hud = HUD() # Gerenciador de interface (pontuação, etc).
        #   2. Entidades
        from src.entities.player import Player # Import local para evitar circularidade
        self.player = Player(player_name)
        self.all_sprites.add(self.player)
        # 3. Engines (Os Especialistas)
        self.coin_spawner = CoinSpawner(self.coins_group,self.all_sprites) # Gerenciador de spawn de moedas.
        self.collision_manager = CollisionEngine(self.player, self.coins_group)
        
        # Spawn inicial
        self.coin_spawner.spawn_coins()
        

    def update(self, dt):

        self.collision_manager.check_coin_colision() # Verifica colisões entre o player e as moedas.
        # self.collision_manager.check_box_colision() # Verifica colisões entre o player e as caixas.
        self.all_sprites.update(dt) # Atualiza todos os sprites do jogo (player, moedas, etc).
        self.coin_spawner.check_spawn(dt) # Verifica se é hora de spawnar novas moedas.
    
    def draw(self, screen):
        screen.fill(BG_COLOR) # Limpa a tela com a cor de fundo.
        self.all_sprites.draw(screen)
        self.hud.draw(screen, self.player)