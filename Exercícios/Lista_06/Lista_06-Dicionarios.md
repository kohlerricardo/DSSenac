# Exercícios sobre Dicionários

> **Tópico:** Criação · Acesso · Manipulação · Algoritmos com Dicionários
> **15 exercícios progressivos** — laços e estruturas de decisão permitidos

---

## Regras gerais

- Dicionários são o foco principal — use-os para armazenar e organizar os dados.
- Laços de repetição (`for`, `while`) e estruturas de decisão (`if`, `elif`, `else`, `match`) são permitidos.
- Listas e tuplas podem ser usadas como suporte quando necessário.
- Cada exercício admite múltiplas soluções válidas — explore diferentes abordagens!

## Legenda de dificuldade

| Símbolo | Nível | Foco |
|---------|-------|------|
| ★ | Fácil | Criação, acesso por chave, iteração básica |
| ★★ | Médio | Manipulação, contagem, dicionários aninhados |
| ★★★ | Difícil | Algoritmos, inversão, agrupamento, lógica composta |

---

## Exercício 1 — Criando e Acessando um Dicionário `★ Fácil`

Crie um dicionário com os dados pessoais de uma pessoa: `nome`, `idade`, `cidade` e `profissão`. Os valores devem ser lidos do usuário. Ao final, exiba cada par chave-valor no formato `chave: valor`.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Nome: Marina` |
| | `Idade: 32` |
| | `Cidade: Porto Alegre` |
| | `Profissão: Engenheira` |
| **Saída** | `nome: Marina` |
| | `idade: 32` |
| | `cidade: Porto Alegre` |
| | `profissão: Engenheira` |

---

## Exercício 2 — Contando Frequência de Palavras `★ Fácil`

Leia uma frase do usuário, separe-a em palavras e conte quantas vezes cada palavra aparece, armazenando o resultado em um dicionário. Exiba cada palavra com sua contagem, em ordem alfabética.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Frase: o gato viu o rato e o rato fugiu` |
| **Saída** | `e: 1` |
| | `fugiu: 1` |
| | `gato: 1` |
| | `o: 3` |
| | `rato: 2` |
| | `viu: 1` |

---

## Exercício 3 — Agenda Telefônica Simples `★ Fácil`

Implemente uma agenda telefônica usando um dicionário onde a chave é o nome e o valor é o telefone. Permita ao usuário: adicionar um contato, buscar um contato pelo nome e exibir todos os contatos. Use um menu simples com opções 1, 2 e 3.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Opção: 1` |
| | `Nome: João  Telefone: 99887766` |
| | `Opção: 1` |
| | `Nome: Ana   Telefone: 91234567` |
| | `Opção: 2` |
| | `Buscar: Ana` |
| | `Opção: 3` |
| **Saída** | `Contato adicionado: João` |
| | `Contato adicionado: Ana` |
| | `Ana: 91234567` |
| | `--- Todos os contatos ---` |
| | `Ana: 91234567` |
| | `João: 99887766` |

---

## Exercício 4 — Placar de Jogo `★ Fácil`

Leia o nome de dois jogadores. Em seguida, leia N rodadas: em cada rodada, leia os pontos de cada jogador e acumule-os em um dicionário. Ao final, exiba o placar e o vencedor (ou empate).

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Jogador 1: Alice   Jogador 2: Bruno` |
| | `Rodadas: 3` |
| | `Alice: 10  Bruno: 8` |
| | `Alice: 6   Bruno: 12` |
| | `Alice: 9   Bruno: 7` |
| **Saída** | `Alice: 25 pontos` |
| | `Bruno: 27 pontos` |
| | `Vencedor: Bruno` |

---

## Exercício 5 — Tradutor de Palavras `★ Fácil`

Defina no código um dicionário português→inglês com pelo menos 8 palavras. Leia uma palavra do usuário e exiba sua tradução. Se a palavra não estiver no dicionário, exiba `Palavra não encontrada.` A busca deve ser case-insensitive.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Palavra: Gato` |
| **Saída** | `Gato → Cat` |

| | |
|---|---|
| **Entrada** | `Palavra: elefante` |
| **Saída** | `Palavra não encontrada.` |

---

## Exercício 6 — Estoque de Produtos `★★ Médio`

Gerencie um estoque usando um dicionário onde a chave é o nome do produto e o valor é a quantidade. Implemente as operações: entrada de produto (adiciona quantidade), saída de produto (subtrai quantidade, sem deixar negativo) e exibição do estoque completo. Use um menu com opções.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Opção: 1  Produto: Arroz    Qtd: 50` |
| | `Opção: 1  Produto: Feijão  Qtd: 30` |
| | `Opção: 2  Produto: Arroz   Qtd: 12` |
| | `Opção: 3` |
| **Saída** | `Entrada registrada: Arroz (+50)` |
| | `Entrada registrada: Feijão (+30)` |
| | `Saída registrada: Arroz (-12)` |
| | `--- Estoque atual ---` |
| | `Arroz: 38 unidades` |
| | `Feijão: 30 unidades` |

---

## Exercício 7 — Média das Notas por Disciplina `★★ Médio`

Leia N disciplinas e, para cada uma, leia 3 notas. Armazene em um dicionário onde a chave é o nome da disciplina e o valor é a média das notas. Ao final, exiba todas as médias, a disciplina com maior média e a com menor média.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Disciplinas: 3` |
| | `Disciplina: Matemática  Notas: 7.0  8.5  9.0` |
| | `Disciplina: Português   Notas: 6.0  7.0  6.5` |
| | `Disciplina: História    Notas: 8.0  9.0  8.5` |
| **Saída** | `Matemática: 8.17` |
| | `Português: 6.50` |
| | `História: 8.50` |
| | `Maior média: História (8.50)` |
| | `Menor média: Português (6.50)` |

---

## Exercício 8 — Inversão de Dicionário `★★ Médio`

Dado um dicionário definido no código onde todas as chaves e valores são únicos, crie um novo dicionário com chaves e valores invertidos (o que era valor vira chave e vice-versa). Exiba o dicionário original e o invertido.

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(dados no código: `{'a': 1, 'b': 2, 'c': 3, 'd': 4}`)* |
| **Saída** | `Original: {'a': 1, 'b': 2, 'c': 3, 'd': 4}` |
| | `Invertido: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}` |

---

## Exercício 9 — Classificação de Alunos por Conceito `★★ Médio`

Leia N alunos com nome e nota. Armazene em um dicionário e classifique cada aluno com um conceito: `A` (≥ 9), `B` (≥ 7), `C` (≥ 5), `D` (< 5). Ao final, exiba todos os alunos com seus conceitos e conte quantos alunos há em cada conceito.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Alunos: 5` |
| | `Pedro: 9.5  Laura: 6.8  Marcos: 4.2  Sofia: 7.5  Igor: 8.9` |
| **Saída** | `Pedro: 9.5 → A` |
| | `Laura: 6.8 → C` |
| | `Marcos: 4.2 → D` |
| | `Sofia: 7.5 → B` |
| | `Igor: 8.9 → B` |
| | `--- Resumo ---` |
| | `A: 1  B: 2  C: 1  D: 1` |

---

## Exercício 10 — Histograma de Caracteres `★★ Médio`

Leia uma string do usuário e construa um dicionário com a frequência de cada caractere (ignorando espaços). Exiba cada caractere seguido de barras `|` proporcionais à sua frequência e o número de ocorrências.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Texto: banana` |
| **Saída** | `b: |  (1)` |
| | `a: |||  (3)` |
| | `n: ||  (2)` |

---

## Exercício 11 — Dicionário Aninhado — Cadastro de Funcionários `★★★ Difícil`

Implemente um cadastro de funcionários usando um dicionário aninhado: a chave externa é o ID (inteiro), e o valor é um dicionário com `nome`, `departamento` e `salário`. Permita: cadastrar, buscar por ID e listar todos. Ao listar, exiba também a folha salarial total.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Opção: 1  ID: 101  Nome: Clara  Depto: TI        Salário: 5200` |
| | `Opção: 1  ID: 102  Nome: Rafa   Depto: RH        Salário: 4100` |
| | `Opção: 2  ID: 101` |
| | `Opção: 3` |
| **Saída** | `Funcionário 101 cadastrado.` |
| | `Funcionário 102 cadastrado.` |
| | `ID 101 — Clara | TI | R$5200.00` |
| | `--- Todos os funcionários ---` |
| | `101: Clara | TI | R$5200.00` |
| | `102: Rafa | RH | R$4100.00` |
| | `Folha salarial total: R$9300.00` |

---

## Exercício 12 — Mesclando Dois Dicionários `★★★ Difícil`

Dados dois dicionários definidos no código com chaves do tipo string e valores inteiros, mescle-os em um terceiro dicionário. Se uma chave existir nos dois, some os valores. Exiba os dois dicionários originais e o resultado da mesclagem.

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(dados no código)* |
| | `d1 = {'maçã': 5, 'banana': 3, 'uva': 8}` |
| | `d2 = {'banana': 2, 'uva': 4, 'manga': 6}` |
| **Saída** | `d1: {'maçã': 5, 'banana': 3, 'uva': 8}` |
| | `d2: {'banana': 2, 'uva': 4, 'manga': 6}` |
| | `Mesclado: {'maçã': 5, 'banana': 5, 'uva': 12, 'manga': 6}` |

---

## Exercício 13 — Índice Invertido de Palavras `★★★ Difícil`

Dadas três frases definidas no código (identificadas como frase 1, 2 e 3), construa um índice invertido: um dicionário onde cada palavra é uma chave e o valor é um conjunto (representado como string formatada) com os números das frases em que ela aparece. Ignore maiúsculas e palavras com menos de 3 letras. Exiba o índice em ordem alfabética.

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(dados no código)* |
| | `Frase 1: "O gato dorme no telhado"` |
| | `Frase 2: "O cachorro late no jardim"` |
| | `Frase 3: "O gato late muito"` |
| **Saída** | `cachorro → frases: [2]` |
| | `dorme → frases: [1]` |
| | `gato → frases: [1, 3]` |
| | `jardim → frases: [2]` |
| | `late → frases: [2, 3]` |
| | `muito → frases: [3]` |
| | `telhado → frases: [1]` |

---

## Exercício 14 — Agrupamento por Categoria `★★★ Difícil`

Leia N produtos, cada um com nome e categoria. Armazene em um dicionário onde a chave é a categoria e o valor é uma lista com os nomes dos produtos daquela categoria. Ao final, exiba os grupos ordenados pela categoria e, dentro de cada grupo, os produtos em ordem alfabética. Exiba também a categoria com mais produtos.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Produtos: 7` |
| | `Notebook → Eletrônicos` |
| | `Maçã → Alimentos` |
| | `Smartphone → Eletrônicos` |
| | `Arroz → Alimentos` |
| | `Tablet → Eletrônicos` |
| | `Feijão → Alimentos` |
| | `Fone → Eletrônicos` |
| **Saída** | `Alimentos: Arroz, Feijão, Maçã` |
| | `Eletrônicos: Fone, Notebook, Smartphone, Tablet` |
| | `Categoria com mais produtos: Eletrônicos (4)` |

---

## Exercício 15 — Cifra de Substituição `★★★ Difícil`

Implemente uma cifra de substituição usando um dicionário como tabela de codificação. Crie um dicionário que mapeia cada letra do alfabeto para outra letra (deslocamento de 3 posições — cifra de César). Leia uma mensagem do usuário, codifique-a letra a letra (preservando espaços e pontuação) e exiba a mensagem cifrada. Em seguida, decodifique-a usando o dicionário inverso e confirme que a mensagem original foi recuperada.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Mensagem: Python e legal` |
| **Saída** | `Cifrada:  Sbwkrq h ohjdo` |
| | `Decifrada: Python e legal` |

---

*Bons estudos! Dicionários são uma das estruturas mais poderosas do Python — dominá-los abre portas para resolver problemas do mundo real com elegância.*
