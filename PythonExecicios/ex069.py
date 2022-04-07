tot18 = 0
totM = 0
tot20 = 0
while True:
    idade = int(input('idade: '))
    sexo =' '
    while sexo not in 'MF':
        sexo = str(input('Escolha o sexo:[M/F]: '))
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totM += 1
    if sexo == 'F':
        tot20 += 1

    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] '))  
    if r == 'N':
        break
print(f'o total de pessoas maior de 18 são {tot18}')
print(f'O total de homens cadastrados foi {totM}')
print(f'O total de mulheres com menos de 20 anos foi {tot20}')
    