print('=='*20)
print('10 TERMOS DE UMA PROGRESSAO ARITIMETICA')
print('=='*20)
num = int(input('Digite o primeiro termo: '))
raz = int(input('Razão: '))
dec = num + (11 - 1) * raz
for c in range(num, dec , raz):
    print (f'{c} ->',end=' ')