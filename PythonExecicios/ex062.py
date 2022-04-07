print('=='*20)
print('10 TERMOS DE UMA PROGRESSAO ARITIMETICA 2.0 ')
print('=='*20)
num = int(input('Digite o primeiro termo: '))
raz = int(input('Razão: '))

termo = num
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ->', end=' ')
        termo = termo + raz
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais?'))
print('FIM')
