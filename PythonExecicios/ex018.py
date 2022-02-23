import math
ang = float(input("digite o angulo que voce deseja: "))
print(f'o angulo de {ang} tem o SENO de {math.sin(math.radians(ang))} \n o angulo de {ang} tem o COSSENO {math.cos(math.radians(ang))} \n o angulo de {ang} tem o TANGENTE de {math.tan(math.radians(ang))}')
#outra forma
from math import radians, cos, sin, tan
