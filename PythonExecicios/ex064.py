num = 0
sum = 0
cont = 0
num = int(input('Digite 999 para parar: '))
while num != 999:
    cont += 1
    sum += num
    num = int(input('Digite 999 para parar: '))
print(f'voce digitou {cont} numeros e a soma dele é de {sum}')