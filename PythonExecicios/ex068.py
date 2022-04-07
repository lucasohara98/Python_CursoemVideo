from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)
ParImpar=' '
v= 0
while True:
    num = int(input('Digite um valor: '))
    comp = randint(1, 11)
    comp2 = ' '
    soma = num + comp
    while ParImpar not in 'PI':
        ParImpar = str(input('Escolha: PAR OU IMPAR? [P/I]')).upper()
    print(f'Voce jogou {num} e o computador jogou {comp}. O total deu {soma} e ele é...', end='')
    print('DEU PAR' if soma % 2 ==0 else 'DEU IMPAR')
        if ParImpar == 'P':
            if soma % 2 == 0:
                print('Voce Venceu!')
                v += 1
            else:
                print('Voce perdeu!')
                break
        elif ParImpar == 'I':
            if soma % 2 == 1:
                print('Voce Venceu!')
                v += 1
            else:
                print('Voce perdeu!')
                break
        print('Vamos jogar novamente...')
    print(f'voce venceu {v} vezes, parabens')