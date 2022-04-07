maior = 0
menor = 0
for p in range (0, 5):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso lido foi de {maior}')
print(f'o maior peso lido foi de {menor}')

