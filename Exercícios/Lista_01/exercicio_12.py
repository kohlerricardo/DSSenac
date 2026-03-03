#12. Faça um algoritmo que receba o raio de um círculo e exiba sua área (A = π ×
#r²) e o seu volume (V = (4/3) × π × r³). Considere π = 3.14159.
import math
PI = 3.14159
raio = float(input("Informe o raio do círculo"))
area = PI * (raio*raio)

# volume = 4/3 * PI * raio**3 #forma1
volume = 4/3 * PI * pow(raio,3)#forma2

print(f"A área do círculo é {area:.2f} cm2")
print(f"O volume do círculo é {volume:.2f} cm3")