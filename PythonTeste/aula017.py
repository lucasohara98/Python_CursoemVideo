lanche =('hamburger','suco','pizza','pudim','batata')
print(lanche[2:])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-2:])
print(lanche)

#TUPLAS SAO IMUTAVEIS
#lanche[1] = 'Refrigerante'
#print(lanche[1])

#FORMAS DE PUXAR AS TUPLAS:

for cont in range(0, len(lanche)):
    print(f' eu vou comer pra caramba {lanche[cont]}')

for comida in lanche:
    print(f'eu vou comer {comida}')
print('comi pra caramba')

for cont in range(0, len(lanche)):
    print(f' eu vou comer pra caramba {lanche[cont]} na posicao {cont}')

for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posicao {pos}')
print('comi pra caramba')

print(sorted(lanche)) #em oredem (alfabetica e numerica)

#junta as tuplas nao soma
a = (3, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

#mostra a quantidade de elementos
a = (3, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(len(c))

#mostra a quantidade que o elemento especifico apereceu no ex o 5
a = (3, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))

#mostra em que posicao esta o elemento na tupla (apenas a primeira ocorrencia)
a = (3, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.index(5))
#para apresentar o outro 5 na posicao, devemos começar do 2 pois a primiera ocorrencia do 5 esta na posicao 0
print(c.index(5, 2))

pessoa = ('lucas', 23, 'M', 1,75)
print(pessoa)
del(pessoa) #apaga a tupla inteira