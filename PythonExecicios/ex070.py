print('-='*15)
print('MERCADINHO PYTHON')
print('-='*15)
total = 0
cont = 0
menor = 0
cont2 = 0
while True:
    prod = str(input('Nome do produto: '))
    price = float(input('Preço: R$ '))
    msg = ' '
    total += price
    if price >= 1000:
        cont += 1
    if cont2 == 1:
        menor = price
    else:
        if price < menor:
            menor = price
            
    while msg not in 'SN':
        msg = str(input('Quer continuar? [S/N] '))
    if msg == 'N':
        break
print(f'O total da compra foi de R$ {total:.2f}')
print(f'temos {cont} produtos custando mais de R$ 1000,00')
print(menor)