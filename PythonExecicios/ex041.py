from datetime import date
nasc = int(input('Digite o seu ano de nascimento: '))
anoatual =  date.today()
idade = anoatual.year - nasc

print(f'A idade do atelta é: {idade} anos')
if idade <= 9:
    print('a classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25:
    print('classificação: SENIOR')
else:
    print('classificação: MASTER')