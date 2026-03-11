# Peça ao usuário para inserir um número positivo N.
# O programa deve exibir todos 
# os números de 1 até N utilizando um loop while.​
numero = int(input("Informe um número positivo"))
while numero <=0:
    print("Número Inválido")
    numero = int(input("Informe um número positivo"))
indice = 1
while indice <= numero:
    print(indice)
    indice +=1
