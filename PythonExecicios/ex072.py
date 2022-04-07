ext = ('zero', 'um', 'dois', 'tres', 'quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    num = int(input('Digite um numero de 1 a 10:'))
    if 0 <= num <= 10:
        break
    print('tente novamente.', end='')
print(f'voce digitou o numero {ext[num]}')