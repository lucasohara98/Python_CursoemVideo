lim = int(input('Digite um valor limite para calcular todos os números primos até ele: '))
c = 0
for n in range(1, lim + 1):
    divisores = []
    for d in range(1, n + 1):
        if n % d == 0:
            divisores += [d]
    if len(divisores) == 2:
        c += 1
        print(n)
print(f'Existem {c} números primos até o número {lim}.')