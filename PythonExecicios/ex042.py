s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um TRIANGULO ', end='')
    if s1 == s2 == s3:           '''igualdade é inclusiva; a = b = c, porem a diferença nao no caso de difrença deve se comprara o C com o A tambem'''
        print('EQUILATERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('nao podem formar um triangulo')
''