# Leia do usuário os valores x e y de um ponto no plano
# cartesiano e armazene-os em uma tupla. Determine e
#  exiba em qual quadrante o ponto se encontra 
# (1°, 2°, 3° ou 4° quadrante) ou se está sobre um dos eixos.

def quadrante(x,y):
    ponto = (x,y)
    if x >0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4
    if x == 0:
        return 'x'
    if y == 0:
        return 'y'
