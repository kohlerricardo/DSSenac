# Faça um algoritmo que receba um número de dois dígitos e exiba a soma dos
# dígitos (ex: 45 → 4 + 5 = 9)

# termo = int(input("Informe um número inteiro de dois dígitos: "))

# dezena = termo // 10 #opcao 1
# dezena = int(termo /10) #opcao 2
# unidade = termo % 10
# print(f"A soma dos digitos {dezena} e {unidade} é: {dezena+unidade}")
#opcao com strings 
termo = input("Informe um número inteiro de dois dígitos: ")
if len(termo)!=2:
    print("Informe somente dois digitos")
    exit(1)
dezena = int(termo[0]) 
unidade = int(termo[1])
print(f"A soma dos digitos {dezena} e {unidade} é: {dezena+unidade}")
