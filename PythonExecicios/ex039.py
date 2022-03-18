from datetime import date
nasc = int(input('Digite o seu ano de nascimento: '))
anoatual =  date.today()
idade = (anoatual.year - nasc)
falta = 18 - idade
foi = idade - 18

print(f'Quem nasceu em {nasc} tem {idade} anos em {anoatual.year} ')
if idade < 18:
    print(f'Ainda faltam {falta} anos para seu alistamento')
    print(f'seu alistamento sera em {anoatual.year + falta}')
elif idade == 18:
    print('Voce deve se alistar IMEDIATAMENTE')
else:
    print(f'Voce ja deveria ter se alistado há {foi} anos')
    print(f'seu alistamento foi em {anoatual.year - foi} ')


'''

como obeter datas atuais no python

from datetime import datetime
now = datetime.now()
print now.year
print now.month
print now.day
print now.hour
print now.minute
print now.second
'''
''' f=date.today().year'''