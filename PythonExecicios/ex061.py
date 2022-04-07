print('=='*20)
print('10 TERMOS DE UMA PROGRESSAO ARITIMETICA 2.0 ')
print('=='*20)
num = int(input('Digite o primeiro termo: '))
raz = int(input('Razão: '))

termo = num
cont = 1

while cont <= 10:
    print(f'{termo} ->', end=' ')
    termo = termo + raz
    cont = cont + 1
print('fim')