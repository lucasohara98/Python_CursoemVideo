'''
from math import trunc
n = float(input('Digite um Valor: '))
print(f'O valor digitado foi {n} e sua porção inteira é {trunc(n)}')

#outra forma:
import math
n = float(input('Digite um Valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, math.trunc(n)))
'''
#outra forma (sem import)
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e sua porção inteira foi {int(n)}')