n = int(input('Qual a velocidade atual do carro: '))
ex = n - 80
multa = float(ex * 7)
if n > 80:
    print(f'MULTADO! Voce execedeu o limite de 80 km/h e deve pagar uma multa de R$ {multa}')
print('Tenha um bom dia! Dirija com segurança!')

