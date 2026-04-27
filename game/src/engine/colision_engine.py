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
    
    def check_box_colision(self):
        # 1. Busca todas as caixas que colidiram com o player
        colided_boxes = pygame.sprite.spritecollide(self.player, self.box_group, False)
        
        if colided_boxes:
            for box in colided_boxes:
                # Pegamos a sobreposição (overlap) para saber por onde o player entrou
                # Isso evita que o player se "teletransporte" para o lado errado
                
                # --- COLISÃO VERTICAL (Subir em caixas) ---
                # Se o player está caindo (vel_y > 0) e seus pés estão acima do meio da caixa
                if self.player.vel_y > 0 and self.player.rect.bottom >= box.rect.top:
                    self.player.rect.bottom = box.rect.top
                    self.player.vel_y = 0
                    self.player.no_chao = True
                
                # --- COLISÃO HORIZONTAL (Paredes da caixa) ---
                else:
                    # Se o centro do player está à esquerda do centro da caixa, ele bateu na esquerda
                    if self.player.rect.centerx < box.rect.centerx:
                        self.player.rect.right = box.rect.left
                    # Caso contrário, ele bateu na direita da caixa
                    else:
                        self.player.rect.left = box.rect.right

    