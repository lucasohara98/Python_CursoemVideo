p = float(input('Qual é o preço do produto? R$'))
d = (p * 95)/100
print('O Produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(p, d))