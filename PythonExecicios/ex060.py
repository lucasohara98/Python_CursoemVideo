num = int(input('Digite um numero para calcular seu fatorial: '))
c = num
f = 1
print(f'calculado {num}!', end=' ')
while c > 0:
    print(f'{c}',end=' ')
    print(' X ' if c > 1 else ' = ',end=' ')
    f*= c
    c-= 1
print(f'O fatorial de {num} é {f}')

