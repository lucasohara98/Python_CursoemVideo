from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print(f'O computador escolheu {itens[computador]}')
jogador=(int(input('Qual é a sua jogada:')))

print('jogador jogou:')
print(f'o computador jogou:{itens[computador]}')