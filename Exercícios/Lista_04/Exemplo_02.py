# Peça ao usuário para inserir um número e exiba a tabuada 
# desse número de 1 a 10 utilizando um loop while

numero = int(input("INforme o número da tabuada: "))
indice = 1
while indice <=10:
    print(f"{indice} x {numero} = {indice*numero}")
    indice+=1