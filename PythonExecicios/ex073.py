brasileirão = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

print('Lista de times do brasileirao:')

print(brasileirão)
print('-='*50)

print('Lista dos 4 primeiros times do brasileirao:')

print(brasileirão[0:4])
print('-='*50)

print('Lista dos 4 ultimos times do brasileirao:')

print(brasileirão[-4])
print('-='*50)

print('Lista dos times do brasileirao em ordem alfabetica:')

print(sorted(brasileirão))
print('-='*50)

print('posicao do chapecoense :')
print(f'O chapeconcse esta na  {brasileirão.index("Chapecoense")+1}ª posição.')
print('-='*50)

