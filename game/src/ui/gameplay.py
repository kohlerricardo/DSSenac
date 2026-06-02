import pygame
import os
from src.engine.coin_spawner import CoinSpawner
from src.engine.colision_engine import CollisionEngine
from src.ui.hud import HUD
from settings import DESLOCAMENTO,BG_COLOR
from src.engine.box_spawner import BoxSpawner
class Gameplay:
    def __init__(self,player_name):
        # Inicialização de elementos do jogo, como player, moedas, etc.
        self.coins_group = pygame.sprite.Group() # Grupo para gerenciar as moedas.
        self.box_group = pygame.sprite.Group() # Placeholder para futuras caixas ou obstáculos.
        self.all_sprites = pygame.sprite.Group() # Grupo para gerenciar todos os sprites do jogo (player, moedas, etc).
        self.hud = HUD() # Gerenciador de interface (pontuação, etc).
        #   2. Entidades
        from src.entities.persona import Persona # Import local para evitar circularidade
        self.player = Persona(player_name)
        self.all_sprites.add(self.player)
        # 3. Engines (Os Especialistas)
        # self.coin_spawner = CoinSpawner(self.coins_group,self.all_sprites) # Gerenciador de spawn de moedas.
        self.collision_manager = CollisionEngine(self.player, self.coins_group,self.box_group)
        self.box_spawner = BoxSpawner(self.box_group, self.all_sprites) # Gerenciador de spawn de caixas.
        # Carregar fundo 
        self._load_fundo()
        ##
        # self.box_spawner.generate_random_layout(1) # Verifica se é hora de spawnar novas caixas.
    def _load_fundo(self):
        try:
            self.fundo1 = pygame.image.load(os.path.join("assets","images","persona","fundo_1.png")).convert_alpha()
            self.fundo2 = pygame.image.load(os.path.join("assets","images","persona","fundo_2.png")).convert_alpha()
            self.fundo1_pos = 0
            self.fundo2_pos = self.fundo1.get_width()
        except pygame.error as e:
            print(f"Erro ao carregar fundo: {e}")

    def update(self, dt):

        # self.collision_manager.check_coin_colision() # Verifica colisões entre o player e as moedas.
        # self.collision_manager.check_box_colision() # Verifica colisões entre o player e as caixas.
        self.all_sprites.update(dt) # Atualiza todos os sprites do jogo (player, moedas, etc).
        ##########################################
        # self.coin_spawner.check_spawn(dt) # Verifica se é hora de spawnar novas moedas.
        
        ##########################################
        # Atualiza a posição do fundo para criar o efeito de movimento contínuo.
        #####################################################################################


        self.fundo1_pos -= DESLOCAMENTO*dt #atualiza posição do fundo para criar efeito de movimento
        self.fundo2_pos -= DESLOCAMENTO*dt #atualiza posição do fundo para criar efeito de movimento
        if self.fundo1_pos <= -self.fundo1.get_width(): #reseta posição de fundo 1 para criar loop
            self.fundo1_pos = self.fundo2_pos+self.fundo1.get_width()
        if self.fundo2_pos <= -self.fundo2.get_width(): #reseta posição de fundo 2 para criar loop
            self.fundo2_pos = self.fundo1_pos+self.fundo2.get_width()
        #######################################################################################

    def draw(self, screen):
        screen.fill(BG_COLOR) # Limpa a tela com a cor de fundo.
        #desenhar duas vezes o fundo, cria impressão de continuidade
        screen.blit(self.fundo1, (self.fundo1_pos, 0)) # Desenha o fundo na tela.
        screen.blit(self.fundo2, (self.fundo2_pos, 0)) # Desenha o fundo na tela.
        
        self.all_sprites.draw(screen)
        
        #draw rect on player
        # pygame.draw.rect(screen,(255,0,0),self.player.rect,2)
        self.hud.draw(screen, self.player)