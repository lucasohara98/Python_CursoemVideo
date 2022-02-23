'''from math import hypot
op = float(input('Qual o comprimento do cateto oposto: '))
ad = float(input('Qual o comprimento do cateto adjacente: '))
print(f'A hipotenusa é: {hypot(op,ad):.2f}')'''

#sem importação
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float (input('Qual o compriemento do cateto adjacente: '))
hi = (co**2 + ca**2)**(1/2)
print(f'a hipotenusa é: {hi:.2f}')

