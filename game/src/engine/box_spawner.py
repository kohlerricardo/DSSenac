import random
import settings
from src.entities.box import Box

class BoxSpawner:
    def __init__(self, box_group, all_sprites):
        self.box_group = box_group
        self.all_sprites = all_sprites
        self.box_size = 32

    def generate_random_layout(self, quantity):
        """Cria 'N' pontos de spawn aleatórios no cenário."""
        for _ in range(quantity):
            # Sorteia uma posição X aleatória
            x = random.randint(0, settings.WIDTH - self.box_size)
            # O chão base onde a pilha começa
            base_y = settings.HEIGHT - settings.CHAO_POS
            self.box_group.add(Box(x, base_y - self.box_size)) # Adiciona a caixa ao grupo de caixas
            self.all_sprites.add(Box(x, base_y - self.box_size)) # Adicion
    def check_spawn(self, dt):
        pass # Implementar lógica de spawn conforme necessário