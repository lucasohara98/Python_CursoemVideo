
nome = str(input('Qual é o seu nome?'))
if nome == 'Lucas':
    print('Que nome lindo voce tem')
else:
    print('Seu nome é tão normal')
print(f'Bom dia. {nome}')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:  '))
m = (n1 + n2)/2
if m >= 6.0:
    print('Sua media foi boa')
else:
    print('Sua media foi ruim! estude mais')    

#simplificado: print('PARABENS' if m>=6 else 'ESTUDE MAIS')