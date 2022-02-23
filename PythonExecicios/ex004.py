n = input('digite algo: ') # função input sempre retorna uma variavel do tipo str
print('o tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaço? {}'.format(n.isspace()))
print('É um número? {}'.format(n.isnumeric()))
print('É um alfábetico? {}'.format(n.isalpha()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('Está em maíusculo? {}'.format(n.isupper()))
print('esta em minusculo? {}'.format(n.islower()))
print('Está captalizada? {}'.format(n.istitle()))
