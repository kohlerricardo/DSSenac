import pygame
import settings

class Pause:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 30)
        self.msg = self.font.render("PAUSADO - Pressione P para Continuar", True, (255, 255, 0))
        self.rect = self.msg.get_rect(center=(settings.WIDTH//2, settings.HEIGHT//2))

    def update(self, dt):
        # Lógica de animação da tela de pausa, se houver
        pass

    def draw(self, screen):
        screen.fill((0, 0, 50)) # Fundo da tela de pausa
        screen.blit(self.msg, self.rect)