import pygame
class HUD:
    def __init__(self):
        """"
        Configurações iniciais do HUD, como fonte e texto.
        """
        self.font_size = 20
        self.font = pygame.font.SysFont("Monospace", self.font_size, True, False) # Fonte negrito.
        self.score_text = self.font.render("Score: 0", False, (255, 255, 255)) # Texto inicial do Score. 
        self.text_color = (255, 255, 255) # Branco
        self.pos = (10, 10) # Posição do texto -  canto superior esquerdo
        # Surface para o HUD
        # tupla (largura, altura) 
        # largura inicial baseada no tamanho do nome do player
        # altura inicial baseada na quantidade de campos
        self.hud_fundo = pygame.Surface((len("Player") * self.font_size, self.font_size*2)) 
        self.hud_fundo.fill((0, 0, 0)) # Fundo preto para melhor contraste
        self.hud_fundo.set_alpha(150) # Transparência do fundo
          


    def draw(self, screen, player):
        """
        Renderiza as informações na tela. 
        Note que o HUD recebe o objeto 'player' para ler o 'score'.
        """
        # 1. Cria a string formatada
        player_name = f"{player.name}" if player.name else "Player"
        score_text = f"Score: {player.score}"
        # 2. Desenha o fundo do HUD antes do texto para garantir que ele fique atrás.
        screen.blit(self.hud_fundo, self.pos)
        
        # 3. Transforma os textos em uma Surface (imagem)
        render_player = self.font.render(player_name, True, self.text_color)
        render_score = self.font.render(score_text, True, self.text_color)

        # 4. Desenha o texto principal
        screen.blit(render_player, self.pos)
        screen.blit(render_score, (self.pos[0], self.pos[1] + self.font_size)) # Desenha o score abaixo do nome do jogador.
