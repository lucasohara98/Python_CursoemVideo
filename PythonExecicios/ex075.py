nums = (int(input('Digite o 1º numero: ')), int(input('Digite o 2º numero: ')), int(input('Digite o 3º numero: ')), int(input('Digite o 4º numero: ')))

print(f'Voce digitou os valores:{nums} ')
print(f'o numero 9 foi digitado {nums.count(9)} vezes')
print(f'o numero 3 apareceu na posição {nums.index(3)+1}')