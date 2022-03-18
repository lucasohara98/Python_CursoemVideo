peso = float(input('Qual é o seu peso? (kg): '))
altura = float(input('Qual é a sua altura? (m): '))

imc = (peso)/altura**2

print(f'Seu IMC é de:{imc:.2f}')
if imc < 18.5:
    print('CUIDADO! voce esta ABAIXO do peso NORMAL')
elif imc >= 18.5 and imc < 25:
    print('PARABENS! Voce esta com o peso NORMAL')
elif imc >= 25 and imc < 30:
    print('CUIDADO! Voce esta com o SOBREPESO')
elif imc >= 30 and imc < 40:
    print('CUIDADO! Voce esta com o OBESIDADE')
elif imc > 40:
    print('CUIDADO! Voce esta com o OBESIDADE MORBIDA')

