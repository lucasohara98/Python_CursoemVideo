from random import randint
from time import sleep
comp = randint(0, 5)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
num = int(input('Em que numero eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if num == comp:
    print(f'O Numero que eu pensei é {num}, parabens voce venceu!!')
else:
    print(f'O numero que eu pensei é {comp} e não {num}, eu venci!!')