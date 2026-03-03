# Número Positivo ou Negativo: Peça um número e informe 
# se ele é positivo, negativo ou zero.     

numero = int(input("informe um número: "))

if numero > 0 :
    print(f"{numero} é maior que 0")
elif numero == 0:
    print(f"numero é igual a 0")
else:
    print(f"{numero} é menor que 0")