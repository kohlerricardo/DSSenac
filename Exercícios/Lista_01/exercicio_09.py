#9. Faça um algoritmo que receba quatro números (a, b, c, d) e exiba o resultado
#da expressão (a × b) - (c × d).

a = int(input('Informe o valor A'))
b = int(input('Informe o valor B'))
c = int(input('Informe o valor C'))
d = int(input('Informe o valor D'))

resultado = (a*b)-(c*d)
print(f"O resultado da expressão ({a}x{b})-({c}x{d})é {resultado}")