import pygame

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.points = 10              # Valor fixo de cada moeda.
        self.name = f"Box {name}"    # Nome único (ex: Box 1).
        self.image = pygame.Surface((32, 32)) # Tamanho da caixa.
        self.image.fill((139, 69, 19)) # Cor marrom (Brown).
        self.rect = self.image.get_rect() # Retângulo para colisão.
        self.rect.topleft = (x, y)    # Posiciona nos eixos X e Y sorteados.