numero = int(input("valor "))
unidade = numero % 10
dezena = numero // 10
soma = unidade + dezena
print(f"O valor da soma dos termos de {numero} é {soma}")