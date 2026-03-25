import pygame
import settings
import os  

class Player(pygame.sprite.Sprite): # Herança: Player 'é um' Sprite do Pygame.
    def __init__(self, name):
        super().__init__()          # Inicializa a lógica interna de Sprites.
        self.name = name            # Atributo para identificação.
        self.score = 0              # Pontuação individual do jogador.
        self.image = pygame.Surface((48, 48)) # Placeholder visual inicial.
        
        try:
            # Tenta carregar a imagem inicial (olhando para cima).
            loaded_image = pygame.image.load("assets/images/up.png").convert_alpha()
            self.image = loaded_image
        except pygame.error as e:
            # Se a imagem faltar, pinta de rosa choque (padrão de erro).
            self.image.fill((255, 0, 255))
            
        self.rect = self.image.get_rect() # Cria o retângulo de colisão da imagem.
        # Posiciona o jogador no centro exato da tela usando as settings.
        self.rect.center = (settings.WIDTH // 2, settings.HEIGHT // 2)

    def increase_score(self, points):
        self.score += points        # Método para somar pontos ao coletar moedas.

    def update(self, dt):           # Lógica que roda a cada frame.
        keys = pygame.key.get_pressed() # Checa quais teclas estão pressionadas.
        
        # Movimentação multiplicada pelo Delta Time (dt) para ser independente do FPS.
        if keys[pygame.K_LEFT]:
            self.rect.x -= settings.PLAYER_SPEED * dt
            self.load_image("left") # Troca o visual para a esquerda.
        if keys[pygame.K_RIGHT]:
            self.rect.x += settings.PLAYER_SPEED * dt
            self.load_image("right")
        if keys[pygame.K_UP]:
            self.rect.y -= settings.PLAYER_SPEED * dt
            self.load_image("up")
        if keys[pygame.K_DOWN]:
            self.rect.y += settings.PLAYER_SPEED * dt
            self.load_image("down")
            
        # Sistema de "Clamping": impede que o rect saia das bordas da tela.
        self.rect.x = max(0, min(self.rect.x, settings.WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, settings.HEIGHT - self.rect.height))

    def load_image(self, direction):
        # Constrói o caminho da imagem dinamicamente (ex: assets/left.png).
        image_path = os.path.join("assets", "images", f"{direction}.png")
        try:
            # Atualiza self.image para a nova direção.
            self.image = pygame.image.load(image_path).convert_alpha()
        except:
            pass # Mantém a imagem atual se a nova falhar.