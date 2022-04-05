num = 0
sum = 0
cont = 0
while True:
    num = int(input('Digite 999 para parar: '))
    if num == 999:
        break
    cont += 1
    sum += num

print(f'voce digitou {cont} numeros e a soma dele é de {sum}')