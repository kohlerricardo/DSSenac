from Ex_06 import separa_tuplas
# 11,9
def teste_separa_tuplas():
    tupla = (4, 15, 8, 22, 3, 18, 7, 11, 25, 6)
    acima,abaixo = separa_tuplas(tupla)
    assert acima == (15,22,18,25),f"Recebido {acima} Esperado = (15,22,18,25)"
    assert abaixo == (4,8,3,7,11,6),f"Recebido {abaixo} Esperado = (4,8,3,7,11,6)"


teste_separa_tuplas()