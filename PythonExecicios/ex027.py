n = str(input('Digite seu nome completo:')).strip()
n1 = n.split()
print(f'Seu primeiro nome é {n1[0]}')
print(f'Seu segundo nome é {n1[len(n1)-1]}')
