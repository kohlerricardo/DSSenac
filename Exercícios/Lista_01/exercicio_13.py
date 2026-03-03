# Faça um algoritmo que receba uma temperatura em Celsius e exiba o valor
# em Fahrenheit (F = C × 9/5 + 32).
temp_celsius = float(input("Informe a temperatura em graus celsius: "))

farenheit = temp_celsius *9/5+32
print(f"{temp_celsius} equivale a {farenheit} graus farenheit")