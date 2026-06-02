# Exercício 3 — Contando Ocorrências em Tupla
# Dada a tupla (3, 7, 2, 7, 5, 7, 1, 4, 7, 2)
#  definida no código, peça ao usuário um número e conte quantas 
#  vezes ele aparece na tupla, sem usar o método .count(). Exiba o resultado.

def contar_em_tupla(tupla,elemento):
    num=0
    for item in tupla:
        if item == elemento:
            num+=1
    return num