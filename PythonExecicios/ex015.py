dia = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
custo = dia * 60
custokm = km * 0.15
total = custo + custokm
print(f'O total a pagar é de R${total:.2f}!')
#outra forma
d = float(input('Quantos dias alugados? '))
k = float(input('Quantos km rodados? '))
print(f'O total a pagar é R${(d * 60) + (k * 0.15):.2f}')