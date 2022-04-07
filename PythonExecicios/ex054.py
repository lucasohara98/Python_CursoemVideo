from datetime import date
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu:'))
    anoatual = date.today()
    idade = anoatual.year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'ao todo tivemos {maior} pessoas maiores de idade')
print(f'e tivemos {menor} pessoas menores de idade')