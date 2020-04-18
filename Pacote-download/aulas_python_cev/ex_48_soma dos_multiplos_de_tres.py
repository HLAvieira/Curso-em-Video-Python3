c = 0
soma = 0
for i in range(1, 500+1):
    if i % 3 == 0 and i % 2 != 0:
        c = c + 1
        soma = soma + i
print('A soma dos {} termos solicitados é igual a {}'.format(c, soma))
