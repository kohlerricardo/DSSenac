# 🎮 Guia de Estrutura de Projeto: Game Dev Python (SRP)

Este documento serve como guia para a organização profissional do seu projeto de jogo. Utilizamos o princípio de **Responsabilidade Única (Single Responsibility Principle - SRP)** para garantir que o código seja modular, fácil de depurar e organizado.

---

##  1. Preparação do Ambiente
Certifique-se de que seu ambiente virtual está configurado e ativo antes de iniciar.

* **Nome da Venv:** `game`
* **Ativação (Windows):** `.\game\Scripts\activate`
* **Ativação (Linux/macOS):** `source game/bin/activate`

---

## 2. Arquitetura de Pastas
Abaixo está a representação da árvore de diretórios que você deve seguir:

```text
├── game/                   # Projeto/Raiz do Ambiente Virtual (VENV)
|
├── main.py                 # Ponto de entrada e Game Loop principal
├── settings.py             # Constantes (Cores, FPS, Velocidade, Resolução)
├── requirements.txt        # Dependências do projeto (ex: pygame-ce)
│
├── assets/                 # Pasta de RECURSOS EXTERNOS (Não-Python)
│   ├── images/             # Sprites (.png com transparência), Tiles e ícones
│   ├── sounds/             # Efeitos sonoros curtos (SFX)
│   └── music/              # Trilhas sonoras de fundo (BGM)
│
└── src/                    # Pasta de CÓDIGO FONTE (Lógica do Jogo)
    ├── __init__.py         # Inicializador de pacote
    ├── entities/           # Classes de objetos do jogo (Sprites)
    │   ├── __init__.py
    │   ├── player.py       # Lógica exclusiva do Jogador
    │   └── coin.py         # Lógica exclusiva das Moedas
    │
    ├── engine/             # Sistemas de suporte (O "Motor")
    │   ├── __init__.py
    │   ├── spawner.py      # Lógica de geração aleatória de objetos
    │   └── collisions.py   # Gerenciamento de impactos e física
    │
    └── ui/                 # Interface do Usuário
        ├── __init__.py
        └── hud.py          # Exibição de Score, Vida e Menus
``` 

--- 

## 3. Por que organizar assim? (Política SRP)
A Política de Responsabilidade Única (Single Responsibility Principle) dita que cada arquivo deve ter apenas um "motivo para mudar":

Isolamento: Se você quiser trocar a arte do herói, mexe apenas na pasta assets/images. O código não muda.

Organização: Se o herói pular alto demais, você sabe que o problema está em src/entities/player.py. Você não precisa ler o código das moedas ou do menu.

---

## 4. Exemplo de Importação no main.py

Para importar os aquivos de código dentro do main, especifica-se o caminho de pastas, separadas por ponto **.** e importa-se a classe ou valor necessário. 
```text
from src.entities.player import Player
from src.entities.coin import Coin
from src.engine.spawner import spawn_coin
```