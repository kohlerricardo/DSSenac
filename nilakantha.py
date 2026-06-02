#série de nilakantha
import time
PI=3.14159265358979323846
#PI=3.141592
print("Calculando o PI")
pi_calculado = 3
n=2
pi_string="3"
while PI != float(pi_string[0:8]):
    pi_calculado+= 4/(n*(n+1)*(n+2))
    n+=2
    pi_calculado-= 4/(n*(n+1)*(n+2))
    pi_string = str(pi_calculado)
    # time.sleep(1)
    n+=2




