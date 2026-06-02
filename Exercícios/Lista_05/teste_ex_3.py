from Ex_3 import contar_em_tupla
def testar_contar_em_tupla():
    tupla = (0,1,2,0,2,1,3)
    resultado = contar_em_tupla(tupla,3)
    assert resultado == 1,f"Erro: Esperado 1, recebido {resultado}"
    resultado = contar_em_tupla(tupla,2)
    assert resultado == 2,f"Erro: Esperado 1, recebido {resultado}"
    resultado = contar_em_tupla(tupla,5)
    assert resultado == 0, f"Erro: Esperado 0, recebido {resultado}"

##############################################################
# teste exercicio 4 - Quadrante do plano cartesiano
def testar_quadrante():
    pass

testar_contar_em_tupla()