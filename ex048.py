soma = 0
count = 0
for num in range (1, 501, 2):
    if num % 3 == 0:
        soma = soma + num
        count = count + 1
print(f'A soma de todos os {count} valores é {soma}')