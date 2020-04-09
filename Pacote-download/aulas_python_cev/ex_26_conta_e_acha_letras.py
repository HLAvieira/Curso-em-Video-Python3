frase = input(str('Digite uma frase: ')).lower().strip()
print(''' a frase possui {} caracteres,
a primeira aparição da da letra "a" é na posição {}
a última aparição da letra "a" é na posição {}'''.format(len(frase), frase.find('a'), frase.rfind('a')))

print('a frase pussui {} caracteres'.format(len(frase)))
frase = input(str('Digite uma frase: ')).lower().strip()
culm = 0
aux = 0
while (frase.count('a')) > 0:
    if aux == 0:
        print('"a" aparece na posição', frase.find('a'))
        culm = culm + frase.find('a')
        frase = frase[frase.find('a')+1:]
        aux = aux+1
    else:
        culm = culm + frase.find('a')+aux
        print('"a" aparece na posição', culm)
        frase = frase[frase.find('a') + 1:]


