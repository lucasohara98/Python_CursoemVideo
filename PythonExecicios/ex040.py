n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2
print(f'Sua media foi {media}')
if media < 5:
    print('voce esta REPROVADO!')
elif media >= 5 and media <= 6.9:
    print('voce esta de RECUPERAÇÃO!')
else:
    print('voce esta APROVADO!')