
# Dada a tupla (4, 15, 8, 22, 3, 18, 7, 11, 25, 6) definida no código,
# construa duas novas tuplas: uma com os valores acima da média e 
# outra com os abaixo ou iguais. 
# Calcule a média manualmente. Exiba as duas tuplas resultantes.

def separa_tuplas(tupla):
    media = 0
    itens = 0
    soma = 0
    for item in tupla:
        soma+=item
        itens+=1
    #######################
    # media = sum(tupla)/len(tupla)
    #######################
    media = soma/itens
    acima_media = ()
    abaixo_igual_media = ()
    for elemento in tupla:
        if elemento > media:
            acima_media = (*acima_media,elemento) # desempacotar 
        else:
            abaixo_igual_media = abaixo_igual_media + (elemento,) # concatenação
    return acima_media,abaixo_igual_media