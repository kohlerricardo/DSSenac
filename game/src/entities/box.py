import pygame
import os
class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Definimos o tamanho da caixa (ex: 32x32)
        self.image = pygame.Surface((32, 32))
        self.image = pygame.image.load(os.path.join("assets","images" ,"persona","simples.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32)) # Redimensiona a imagem para o tamanho da caixa
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, dt):
        # Caixas são estáticas, mas o método existe para compatibilidade com o Grupo
        pass