from datetime import date
valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o salario do comprador? R$'))
ano = int(input('em quantos anos voce quer pagar' ))
parcela = valor/(12 * ano)
porcetagem = (salario*30)/100
print(f'Para pagar uma casa no valor de R${valor:.2f} em {ano} anos,a prestação sera de R${parcela:.2f} ao mes')
if parcela >= porcetagem:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo pode ser APROVADO!')