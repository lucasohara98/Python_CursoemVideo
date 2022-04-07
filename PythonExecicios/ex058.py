from random import randint
print('Sou seu computador...')
print('Acabei de pensar em numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi?')
tent = 1
comp = randint(1, 10)
palp = int(input('Digite seu palpite: '))
if palp > 10:
    print('Valor deve ser menor que 10.')
while palp != comp:
    tent += 1
    if palp > comp:
        palp = int(input('Menos...tente outra vez: '))

    elif palp < comp:
        palp = int(input('Mais...tente outra vez: '))


print(f'Acertou com {tent} tentativas. Parabens!')


