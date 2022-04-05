nome = str(input('Qaul é o seu nome? ')).lower()
if nome == 'lucas':
    print('Que nome bonito!')
elif nome =='pedro' or nome =='maria' or nome == 'joão':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal')
print (f'Tenha um bom dia, {nome}')