nome = str(input('Digite o seu nome completo: ')).strip()
print('O seu nome em maiúsculas é {}'.format(nome.upper()))
print(f'O seu nome em minúsculas é {nome.lower()}')
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

