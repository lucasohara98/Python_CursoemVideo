import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')

#outra forma:
from math import sqrt, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {ceil(raiz)}')