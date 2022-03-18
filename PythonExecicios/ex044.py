print('='*10,end=' ')
print('loja do lucas', end =' ')
print('='*10)

valor = float(input('Qual o valor da compra?R$: '))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] á vista dinheiro/cheque')
print('[ 2 ] a vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x no cartão ou mais')

pag = int(input('digite a opção desejada: '))
juros =(valor * 20)/100
if pag == 1:
    print(f'Sua compra de R${valor} vai custar R${valor - ((valor * 10)/100)} no final')
elif pag == 2:
    print(f'Sua compra de R${valor} vai custar R${valor - ((valor * 5) / 100)} no final')
elif pag == 3:
    print(f'Sua compra de R${valor} vai ser parcelada em 2x de R${valor/2}.')
elif pag == 4:
    parcela = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcela} de R${(valor + juros)/parcela} COM JUROS')
    print(f'Sua compra de R${valor} vai custar R${valor + juros} no final')