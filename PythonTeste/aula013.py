for c in range(0, 6):
    print('oi')

for b in range (0, 6):
    print(b)
print('fim')

for b in range (6, 0, -1):
    print(b)
print('fim')

n= int(input('Digite um numero: '))
for c in range(0, n):
    print(c)
print('fim')
i = int(input('Inicio: '))
f = int(input('fim: '))
p = int(input('passos: '))
for c in range(i, f+1, p):
    print(c)