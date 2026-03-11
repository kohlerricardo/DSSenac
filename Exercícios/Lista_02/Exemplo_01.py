# Classificação de Idade: Peça a idade de uma pessoa 
# e diga se ela é criança (0-12),
#  adolescente (13-17) ou adulta (18+) ou idosa (65+)
idade = int(input("Informe a idade do vivente: "))

if idade < 0:
    print("Entrada inválida")
elif idade <= 12 : 
    print("O vivente é uma criança")
elif (idade >= 13) and (idade <= 17):
    print("O vivente é um adolescente")
elif (idade >=18) and (idade<=65):
    print("O vivente é um adulto")
else:
    print("O vivente é um idoso")