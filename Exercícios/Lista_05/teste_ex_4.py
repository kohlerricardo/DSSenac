from Ex_04 import quadrante


def testar_quadrante():
    resultado = quadrante(1,1)
    assert resultado == 1, f"Resultado: {resultado}, esperado 1"
    resultado = quadrante(-1,1)
    assert resultado == 2, f"Resultado: {resultado}, esperado 2"
    resultado = quadrante(-1,-1)
    assert resultado == 3, f"Resultado: {resultado}, esperado 3"
    resultado = quadrante(1,-1)
    assert resultado == 4, f"Resultado: {resultado}, esperado 4"
    resultado = quadrante(0,1)
    assert resultado == 'x', f"Resultado: {resultado}, esperado x"
    resultado = quadrante(1,0)
    assert resultado == 'y', f"Resultado: {resultado}, esperado y"

testar_quadrante()