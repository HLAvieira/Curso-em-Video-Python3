a = float(input('digite o primeiro número: '))
maior = a
menor = a
b = float(input('digite o segundo número: '))
if b > a:
    maior = b
else:
    menor = b
c = float(input('digite o terceiro número: '))
if c > maior:
    maior = c
elif c < menor:
    menor = c
print('o maior número é {}, o menor número é {}'.format(maior, menor))



