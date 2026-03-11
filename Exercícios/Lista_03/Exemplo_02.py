# Dado um número de 1 a 12(janeiro-dezembro),
# informe se o mês possui 28, 30 ou 31 dias.

mes = int(input("Informe o mês em formato 1-12: "))
# opção 1
    # if mes == 1:
    #     print("31 dias")
    # elif mes == 2:
    #     print("28 dias")
    # elif mes == 3:
    #     print("31 dias")
    # elif mes == 4:
    #     print("30 dias")
    # elif mes == 5:
    #     print("31 dias")
    # elif mes == 6:
    #     print("30 dias")
    # elif mes == 7:
    #     print("31 dias")
    # elif mes == 8:
    #     print("31 dias")
    # elif mes == 9:
    #     print("30 dias")
    # elif mes == 10:
    #     print("31 dias")
    # elif mes == 11:
    #     print("30 dias")
    # elif mes == 12:
    #     print("31 dias")
    # else:
    #     print("Entrada inválida")
# opcao2
# if mes == 2:
#     print("28 dias")
# elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
#     print("31 dias")
# elif mes == 4 or mes == 6 or mes == 9 or mes == 11: 
#     print("30 dias")
# else:
#     print("Entrada inválida")
# opção 3

match(mes):
    case 1|3|5|7|8|10|12 : print("31 dias")
    case 4|6|9|11 : print("38 dias")
    case 2 : print("28 dias")
    case _ : print("entrada inválida")




meses={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
print(f"{meses[mes]} dias")