r= 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
    soma += n
    cont += 1
    med = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'A media da soma desses numeros é de {med}')
print(f'O maior numero foi {maior} e o menor numero foi {menor}')
