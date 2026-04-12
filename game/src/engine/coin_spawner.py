import pygame
import settings
import random
from src.entities.coin import Coin
class CoinSpawner:
    def __init__(self, coins_group, all_sprites):
        self.coins_group = coins_group
        self.all_sprites = all_sprites
        self.spawn_timer = 0.0


    def update(self, dt):
        self.coins_group.update(dt) # Atualiza as moedas (mesmo que sejam estáticas, para manter a lógica do grupo).    

    def spawn_coins(self):
        # Gerar coordenadas aleatórias dentro da tela
        for i in range(settings.COIN_COUNT):
            x = random.randint(0, settings.WIDTH - 16) # 16 é o tamanho da moeda, para evitar spawn fora da tela.
            y = random.randint(0, settings.HEIGHT - 16)
            coin = Coin(x, y, i+1) # Cria uma nova moeda com um valor incremental (i+1).
            self.coins_group.add(coin) # Adiciona a moeda ao grupo de gerenciamento.
            self.all_sprites.add(coin) # Adiciona a moeda ao grupo de todos os sprites para ser desenhada e atualizada junto com o player.
    def check_spawn(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer >= settings.COIN_SPAWN_INTERVAL:
            self.spawn_coins()
            self.spawn_timer = 0.0 # Reseta o timer após o spawn.