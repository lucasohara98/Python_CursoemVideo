list = ('Lapis', 1.75,
        'Borracha', 2.75,
        'Caderno', 15.90,
        'Estojo', 10.00,
        'Compasso', 10.50,
        'Mochila', 150.00
        )
print('-'*30)
print('Listagem de preços')
print('-'*30)
for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<30}',end = '')
    else:
        print(f'R${list[pos]:>7.2f}')
