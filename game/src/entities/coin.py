import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.points = 10              # Valor fixo de cada moeda.
        self.name = f"Coin {name}"    # Nome único (ex: Coin 1).
        self.image = pygame.Surface((16, 16)) # Tamanho da moeda.
        self.image.fill((255, 215, 0)) # Cor dourada (Gold).
        self.rect = self.image.get_rect() # Retângulo para colisão.
        self.rect.topleft = (x, y)    # Posiciona nos eixos X e Y sorteados.