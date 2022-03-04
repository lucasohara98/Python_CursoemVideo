km = float(input('Qual a distancia da sua viagem?'))
print(f'Voce esta prestes a começar uma viagem de {km}Km.')
if km <= 200:
    print(f'E o preço de sua passagem é de R${km * 0.50:.2f}')
else:
    print(f'E o preço de sua passagem é de R${km * 0.45:.2f}')
