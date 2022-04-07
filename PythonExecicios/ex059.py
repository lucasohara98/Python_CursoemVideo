n1 = (int(input('Digite o primeiro valor: ')))
n2 = (int(input('Digite o segundo valor: ')))
op = 0
while op != 5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair')
    op = int(input('Qual a sua opção? '))
    if op == 1:
        soma = n1 + n2
        print(f'A soma entre os dois numero é {soma}')
    elif op == 2:
        mult = n1 * n2
        print(f'A multiplicação entre os dois numero é {mult}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n1 < n2:
            print(f'{n2} é maior que {n1}')

    elif op == 4:
        n1 = (int(input('Digite o primeiro valor: ')))
        n2 = (int(input('Digite o segundo valor: ')))


print('fim do programa. Volte sempre')

