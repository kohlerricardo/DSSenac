import pygame
import settings
import os  
import random
class Player(pygame.sprite.Sprite): # Herança: Player 'é um' Sprite do Pygame.
    def __init__(self, name):
        super().__init__()          # Inicializa a lógica interna de Sprites.
        self.name = name            # Atributo para identificação.
        self.score = 0              # Pontuação individual do jogador.
        self.image = pygame.Surface((64,64)) # Placeholder visual inicial.
        self.chao=True
        self.dict_images = {}
        for image in ['left','right','jump','fall']:
            try:
                # Tenta carregar a imagem inicial (olhando para cima).
                loaded_image = pygame.image.load(os.path.join("assets","images","persona",f"{image}.png")).convert_alpha()
                self.dict_images[image] = loaded_image
            except pygame.error as e:
                # Se a imagem faltar, pinta de rosa choque (padrão de erro).
                self.image.fill((255, 0, 255))
            
        self.image = self.dict_images['left']
        self.rect = self.image.get_rect() # Cria o retângulo de colisão da imagem.
        # Posiciona o jogador no centro exato da tela usando as settings.
        self.rect.center = (settings.WIDTH // 2, settings.HEIGHT // 2)
        # Variáveis para controle de pulo
        self.vel_y = 0
        #Gravidade é a aceleração que fará o player cair mais rápido com o tempo, simulando uma queda realista.
        #oriunda do arquivo settings.py, onde definimos um valor fixo para a gravidade do jogo.
        self.pulo = settings.FORCA_PULO # Velocidade inicial do pulo.
        self.no_chao = True # Flag para verificar se o player está no chão
    # Método para que o movimento de pulo seja aplicado, alterando a velocidade vertical do player e a imagem para a animação de pulo.
    def _jump(self):
        self.vel_y = -self.pulo # Aplica a força de pulo na velocidade vertical (negativa para subir).
        self.image = self.dict_images['jump']
        self.no_chao = False
    # Método para aplicar a gravidade, atualizando a posição vertical do player e simulando a queda.   
    def gravidade(self,dt):
        # 1. Aumenta a velocidade de queda (aceleração)
        self.vel_y += settings.GRAVIDADE * dt
        # 2. Aplica a velocidade na posição Y do rect
        self.rect.y += self.vel_y * dt
        # 3. Simulação de Chão
        # Se o pé do player passar da altura do chão definida:
        chao_y = settings.HEIGHT - settings.CHAO_POS 
        if self.rect.bottom >= chao_y:
            self.rect.bottom = chao_y
            self.vel_y = 0
            self.no_chao = True
            self.image = self.dict_images['left'] 

    def update(self, dt):           # Lógica que roda a cada frame.
        self.gravidade(dt) # Aplica a gravidade a cada frame.
        
        keys = pygame.key.get_pressed() # Checa quais teclas estão pressionadas.
        
        # Movimentação multiplicada pelo Delta Time (dt) para ser independente do FPS.
        if keys[pygame.K_LEFT]:
            self.rect.x -= settings.PLAYER_SPEED * dt
            self.image = self.dict_images['left'] # Troca o visual para a esquerda.
        if keys[pygame.K_RIGHT]:
            self.rect.x += settings.PLAYER_SPEED * dt
            self.image = self.dict_images['right']
        if keys[pygame.K_SPACE] and self.no_chao:
            self._jump() # Inicia o pulo se a barra de espaço for pressionada e o player estiver no chão.

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

