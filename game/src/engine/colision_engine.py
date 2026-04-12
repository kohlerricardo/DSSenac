import pygame 

class CollisionEngine:
    def __init__(self, player, coins_group,box_group=None):
        self.player = player
        self.coins_group = coins_group
        self.box_group = box_group # Placeholder para futuras colisões com caixas ou outros objetos. Pode ser implementado depois.
        

    def check_coin_colision(self):
        # Verifica colisões entre o jogador e as moedas.
        collided_coins = pygame.sprite.spritecollide(self.player, self.coins_group, True) # True para remover a moeda do grupo ao colidir.
        for coin in collided_coins:
          self.player.increase_score(coin.points) # Incrementa a pontuação com o valor da moeda.
    # def check_box_colision(self):
        # colided = pygame.sprite.spritecollide(self.player, self.box_group, False) # False para não remover a caixa ao colidir.
        # if colided:
        #     if self.player.rect.colliderect(colided[0].rect): # Verifica a colisão real entre os retângulos (pode ser expandida para múltiplas caixas depois).
        #         print(f"Colisão com caixa detectada!{self.player.rect}") # Placeholder para lógica de colisão com caixas (pode ser expandida depois).
        #         self.player.rect.update(colided[0].rect)