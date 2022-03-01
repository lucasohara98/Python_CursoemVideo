n = str(input('Digite uma frase: ')).strip()
n1 = n.lower().count('a')
n2 = n.find('a')+1
n3 = n.rfind('a')+1
print(f'A Letra A aparece {n1} vezes na frase.')
print(f'A primeira letra A aparece na posição {n2}')
print(f'A ultima letra A aparece na posição {n3}')
