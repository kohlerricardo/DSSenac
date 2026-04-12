import pygame
import settings

class Menu:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 40)
        self.msg = self.font.render("Pressione ENTER para Jogar", True, (255, 255, 255))
        self.rect = self.msg.get_rect(center=(settings.WIDTH//2, settings.HEIGHT//2))

    def update(self,dt):
        # Lógica de animação do menu, se houver
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0)) # Fundo do menu
        screen.blit(self.msg, self.rect)


