import random

numero_secreto = random.randint(1,100)
palpite = 0
tentativas = 0
while palpite != numero_secreto:
    palpite = int(input("Tente adivinhar o número secreto: "))
    tentativas = tentativas + 1
    if palpite > numero_secreto:
        print("Muito alto!")
    elif palpite < numero_secreto:
        print("Muito baixo!")
print(f"Parabens!! Você acertou em {tentativas} tentativas")