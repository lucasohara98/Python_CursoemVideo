num = int(input('Digite um numero inteiro: '))
binario = bin(num)
hexa = hex(num)
octal = oct(num)
print('[1] converter para BÍNARIO:')
print('[2] converter para OCTAL: ')
print('[3] converter para HEXADECIMAL: ')
base = int(input(f'Escolha uma das bases para conversão:'))
print(f'sua opção foi {base}')

if base == 1:
    print(f'{num} convertido em BÍNARIO é igual a {binario}')
elif base == 2:
    print (f'{num} convertido em OCTAL é igual a {octal}')
elif base == 3:
    print(f'{num} convertido em HEXADECIMAL é igual a {hexa}')
