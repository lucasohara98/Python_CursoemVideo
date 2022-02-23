nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {:20}!'.format(nome))
print('Prazer em te conhecer, {:>20}!'.format(nome))
print('Prazer em te conhecer, {:<20}!'.format(nome))
print('Prazer em te conhecer, {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {},\n a multiplicção é {},\n a divisão é {}'.format(s, m, d), end=' ') #end cacnela quebra de linha e o \n quebra exatamente onde ele está
print ('A divisão inteira é {}, e a potencia é {}'.format(di, e))
