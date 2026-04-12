# Exercícios sobre Tuplas

> **Tópico:** Criação · Acesso · Desempacotamento · Algoritmos  
> **15 exercícios progressivos** — laços e estruturas de decisão permitidos

---

## Regras gerais

- Tuplas são o foco principal — use-as para armazenar e organizar os dados.
- Laços de repetição (`for`, `while`) e estruturas de decisão (`if`, `elif`, `else`, `match`) são permitidos.
- Quando o enunciado proibir uma função built-in (ex.: `max`, `min`, `count`), implemente o equivalente manualmente.
- Cada exercício admite múltiplas soluções válidas — explore diferentes abordagens!

## Legenda de dificuldade

| Símbolo | Nível | Foco |
|---------|-------|------|
| ★ | Fácil | Criação, acesso por índice, desempacotamento |
| ★★ | Médio | Iteração, filtragem, tuplas aninhadas |
| ★★★ | Difícil | Algoritmos clássicos, matrizes, codificação |

---

## Exercício 1 — Criando e Acessando uma Tupla `★ Fácil`

Crie uma tupla com os nomes dos 7 dias da semana. Exiba o primeiro, o último e o elemento do meio, acessando-os pelo índice. Exiba também o total de elementos usando `len()`.

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(nenhuma entrada — dados definidos no código)* |
| **Saída** | `Primeiro: Segunda-feira` |
| | `Último: Domingo` |
| | `Meio: Quinta-feira` |
| | `Total de dias: 7` |

---

## Exercício 2 — Desempacotamento de Tupla `★ Fácil`

Defina no código uma tupla com três valores representando o nome, a idade e a cidade de uma pessoa. Use desempacotamento (*unpacking*) para atribuir cada valor a uma variável e exiba uma frase formatada com os dados.

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(nenhuma entrada — dados definidos no código)* |
| **Saída** | `Nome: Alice | Idade: 28 | Cidade: Curitiba` |

---

## Exercício 3 — Contando Ocorrências em Tupla `★ Fácil`

Dada a tupla `(3, 7, 2, 7, 5, 7, 1, 4, 7, 2)` definida no código, peça ao usuário um número e conte quantas vezes ele aparece na tupla, sem usar o método `.count()`. Exiba o resultado.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Número a buscar: 7` |
| **Saída** | `O número 7 aparece 4 vez(es) na tupla.` |

---

## Exercício 4 — Tupla de Coordenadas `★ Fácil`

Leia do usuário os valores `x` e `y` de um ponto no plano cartesiano e armazene-os em uma tupla. Determine e exiba em qual quadrante o ponto se encontra (1°, 2°, 3° ou 4° quadrante) ou se está sobre um dos eixos.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `x: -3` |
| | `y: 5` |
| **Saída** | `Ponto: (-3, 5)` |
| | `Localização: 2° Quadrante` |

---

## Exercício 5 — Maior e Menor sem `max()`/`min()` `★ Fácil`

Defina no código a tupla `(14, 3, 52, 8, 27, 1, 39, 6)`. Percorra-a com um laço e encontre o maior e o menor valor sem usar as funções `max()` e `min()`. Exiba os resultados e os índices onde foram encontrados.

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(nenhuma entrada — tupla: `(14, 3, 52, 8, 27, 1, 39, 6)`)* |
| **Saída** | `Maior: 52 (índice 2)` |
| | `Menor: 1 (índice 5)` |

---

## Exercício 6 — Filtrando Elementos de uma Tupla `★★ Médio`

Dada a tupla `(4, 15, 8, 22, 3, 18, 7, 11, 25, 6)` definida no código, construa duas novas tuplas: uma com os valores acima da média e outra com os abaixo ou iguais. Calcule a média manualmente. Exiba as duas tuplas resultantes.

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(nenhuma entrada — dados definidos no código)* |
| **Saída** | `Média: 11.9` |
| | `Acima da média: (15, 22, 18, 25)` |
| | `Abaixo ou igual: (4, 8, 3, 7, 11, 6)` |

---

## Exercício 7 — Tuplas como Registros de Alunos `★★ Médio`

Defina no código uma tupla de tuplas onde cada tupla interna representa um aluno com `(nome, nota)`. Percorra os registros e exiba o nome de cada aluno com sua situação: `Aprovado` (nota ≥ 7), `Recuperação` (nota ≥ 5) ou `Reprovado` (nota < 5). Ao final, exiba a média geral da turma.

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(dados no código: `('Ana',8.5), ('Bruno',4.0), ('Carla',6.5), ('Diego',9.0), ('Eva',5.0)`)* |
| **Saída** | `Ana: 8.5 → Aprovado` |
| | `Bruno: 4.0 → Reprovado` |
| | `Carla: 6.5 → Recuperação` |
| | `Diego: 9.0 → Aprovado` |
| | `Eva: 5.0 → Recuperação` |
| | `Média da turma: 6.60` |

---

## Exercício 8 — Concatenação e Fatiamento `★★ Médio`

Crie duas tuplas com 4 inteiros cada, lidas do usuário. Concatene-as em uma terceira tupla. Exiba: a tupla concatenada, os 3 primeiros elementos, os 3 últimos e os elementos de índice par.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Tupla 1: 1 2 3 4` |
| | `Tupla 2: 5 6 7 8` |
| **Saída** | `Concatenada: (1, 2, 3, 4, 5, 6, 7, 8)` |
| | `Primeiros 3: (1, 2, 3)` |
| | `Últimos 3: (6, 7, 8)` |
| | `Índices pares: (1, 3, 5, 7)` |

---

## Exercício 9 — Busca Linear em Tupla `★★ Médio`

Defina no código uma tupla com 10 strings (nomes de cidades). Peça ao usuário uma cidade e realize uma busca linear, exibindo se foi encontrada e em qual posição. A busca deve ser *case-insensitive*.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `Cidade: florianópolis` |
| **Saída** | `Cidade encontrada: Florianópolis (posição 3)` |

---

## Exercício 10 — Tupla de Tuplas — Tabela de Produtos `★★ Médio`

Defina no código uma tupla de tuplas representando produtos: `(nome, preço, quantidade)`. Exiba todos os produtos formatados em colunas. Calcule e exiba o produto mais caro, o mais barato e o valor total do estoque (preço × quantidade de cada item).

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(dados no código: `('Caneta',2.50,100), ('Caderno',15.90,50), ('Mochila',89.90,20), ('Borracha',1.20,200)`)* |
| **Saída** | `Produto          Preço    Qtd` |
| | `Caneta           R$2.50   100` |
| | `Caderno          R$15.90  50` |
| | `Mochila          R$89.90  20` |
| | `Borracha         R$1.20   200` |
| | `Mais caro: Mochila (R$89.90)` |
| | `Mais barato: Borracha (R$1.20)` |
| | `Valor total do estoque: R$2441.00` |

---

## Exercício 11 — Ordenando Tupla de Tuplas `★★★ Difícil`

Defina uma tupla de tuplas com dados de funcionários: `(nome, salário)`. Ordene manualmente por salário em ordem decrescente usando *bubble sort* sobre uma lista auxiliar, sem usar `sorted()` ou `sort()`. Exiba o ranking final.

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(dados no código: `('Carlos',4200), ('Ana',6800), ('Bruno',3500), ('Diana',7100), ('Eva',5300)`)* |
| **Saída** | `1° Diana: R$7100.00` |
| | `2° Ana: R$6800.00` |
| | `3° Eva: R$5300.00` |
| | `4° Carlos: R$4200.00` |
| | `5° Bruno: R$3500.00` |

---

## Exercício 12 — Distância entre Pontos `★★★ Difícil`

Defina no código uma tupla com N pontos no plano, cada um representado como uma tupla `(x, y)`. Leia do usuário as coordenadas de um ponto de referência P. Calcule a distância euclidiana de P a cada ponto da tupla e exiba o ponto mais próximo e o mais distante, com suas distâncias.

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(pontos no código: `((1,2),(4,6),(7,1),(3,9),(5,5))`)* |
| | `Ponto de referência — x: 4  y: 4` |
| **Saída** | `Mais próximo: (4, 6) — distância: 2.00` |
| | `Mais distante: (3, 9) — distância: 5.10` |

---

## Exercício 13 — Frequência de Elementos `★★★ Difícil`

Dada a tupla `(1,3,2,1,5,3,3,2,1,4,5,3)` definida no código, calcule a frequência de cada valor único usando apenas tuplas auxiliares (sem dicionários ou listas). Exiba cada valor com sua frequência e percentual, em ordem crescente de valor.

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(nenhuma entrada — dados definidos no código)* |
| **Saída** | `Valor 1: 3x (25.0%)` |
| | `Valor 2: 2x (16.7%)` |
| | `Valor 3: 4x (33.3%)` |
| | `Valor 4: 1x (8.3%)` |
| | `Valor 5: 2x (16.7%)` |

---

## Exercício 14 — Transposta de Matriz com Tuplas `★★★ Difícil`

Defina no código uma matriz 3×4 como uma tupla de tuplas (cada linha é uma tupla). Calcule e exiba a matriz transposta (4×3), também como tupla de tuplas, sem usar `zip()`. Exiba ambas as matrizes formatadas.

**Caso de teste**

| | |
|---|---|
| **Entrada** | *(dados no código: `((1,2,3,4),(5,6,7,8),(9,10,11,12))`)* |
| **Saída** | `Original (3x4):` |
| | `1  2  3  4` |
| | `5  6  7  8` |
| | `9  10 11 12` |
| | `Transposta (4x3):` |
| | `1  5  9` |
| | `2  6  10` |
| | `3  7  11` |
| | `4  8  12` |

---

## Exercício 15 — Compressão Run-Length `★★★ Difícil`

A compressão Run-Length codifica sequências repetidas: `AAABBBCCDDDDEA` se torna `((A,3),(B,3),(C,2),(D,4),(E,1),(A,1))`. Leia uma string do usuário e aplique o algoritmo, armazenando o resultado como uma tupla de tuplas `(caractere, contagem)`. Exiba a tupla resultante e a string reconstruída a partir dela para verificação.

**Caso de teste**

| | |
|---|---|
| **Entrada** | `String: AAABBBCCDDDDEA` |
| **Saída** | `Comprimida: (('A', 3), ('B', 3), ('C', 2), ('D', 4), ('E', 1), ('A', 1))` |
| | `Reconstruída: AAABBBCCDDDDEA` |

---

*Bons estudos! Compreender a diferença entre tuplas e listas é um marco importante na formação de todo programador Python.*
