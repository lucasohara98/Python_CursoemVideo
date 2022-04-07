somaidade = 0
maioridadehomem = 0
nomevelho=''
menor = 0
for c in range(1, 6):
    print(f'<--- {c}ª PESSOA --->')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('sexo [M/F]: ')).upper()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome


print(f'A media de idade do grupo de pessoas é de {somaidade/5} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {menor} mulheres com menos de 20 anos')

