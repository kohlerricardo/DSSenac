import pygame
import settings

class GameOver:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 50)
        self.msg = self.font.render("GAME OVER - 'R' para Reiniciar", True, (200, 0, 0))
        self.rect = self.msg.get_rect(center=(settings.WIDTH//2, settings.HEIGHT//2))

    def update(self):
        # Lógica de animação do game over, se houver
        pass

    def draw(self, screen):
        screen.fill((30, 0, 0))
        screen.blit(self.msg, self.rect)