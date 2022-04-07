from random import randint
from time import sleep
print('-='*10,end=' ')
print(' JOKENPO!!',end=' ')
print('-='*10)
print('suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
num = int(input('Qual é a sUa jogada? '))

print('JO')
sleep(1)

print('KEN')
sleep(1)

print('PO!!!')

print('-='*10)

comp = randint (0,2)
print('O computador jogou',end=' ')
if comp == 0:
    print('PEDRA')
elif comp == 1:
    print('PAPEL')
elif comp == 2:
    print('TESOURA')

print(f'O jogador jogou',end=' ')
if num == 0:
    print('PEDRA')
elif num == 1:
    print('PAPEL')
elif num == 2:
    print('TESOURA')

print('-='*10)

if comp == num:
    print('Deu empate')
elif comp == 0 and num == 1:
    print('JOGADOR VENCEU')
elif comp == 1 and num == 2:
    print('JOGADOR VENCEU')
elif comp == 2 and num == 0:
    print('JOGADOR VENCEU')
else:
    print('COMPUTADOR VENCEU!')