txt = str(input('Digite uma frase: ')).upper()
txt1 = txt.split()
txt2 = ''.join(txt1)
inver = txt[::-1].split()
junt = ''.join(inver)

if txt2 == junt:
   print(f'{txt2} e {junt}  é um palindromo')
else:
    print (f'{txt2} e {junt} NÃO é um palindromo')

