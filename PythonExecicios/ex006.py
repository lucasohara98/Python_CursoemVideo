# minha resolução
n = int(input('Digite um número: '))
print('o dobro de {} é {}'.format((n), (n*2)))
print('O triplo de {} é {}.'.format((n), (n*3)))
print('A raiz Quadrada de {} é igual a {}.'.format((n), (n**(1/2))))

#da para fazer assim:
n = int(input('Digite um número: '))
print('O dobro de {} vale {}, \n o triplo de {} vale {}, \n e a raiz quadrada de {} vale {:.2f}'.format(n, n*2, n, n*3, n, n**(1/2)))
#obs: {:.2f} indica para o print puxar apenas 2 casas apos o ponto do resultado, e podemos fazer potencia usando o: pow(n,(1/2))

#outra maneira
n = int(input('Digite um número: '))
print(f'O dobro de {n} é {n*2}.\nO triplo é {n*3}\nA raiz quadrada é {n**(1/2):.2f}.')
#colocar o "print(f" faz com que ele concatene a string sem precisar usar o {}.formart (valido para python 3.6 ou +