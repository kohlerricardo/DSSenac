
numero = -1
while numero < 0:
    numero = int(input("Informe um número: "))
if numero == 0 or numero == 1:
    print(f"{numero}! = 1")
fatorial = 1
numero_fatorial = numero
#opcao 1
while numero > 1:
    fatorial = fatorial*numero
    numero = numero -1
#opcao 2
indice = 1
fatorial_2 = 1
numero = numero_fatorial
while indice <=numero:
    fatorial_2 = fatorial_2 * indice
    indice = indice + 1  
print(f"Opção 1 = {numero_fatorial}! = {fatorial}")
print(f"Opção 2 = {numero_fatorial}! = {fatorial_2}")