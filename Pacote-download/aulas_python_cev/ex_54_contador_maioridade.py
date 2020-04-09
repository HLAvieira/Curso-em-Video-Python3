n_maior = 0
n_menor = 0
for i in range (0,7):
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i+1)))
    if idade < 21:
        n_menor = n_menor + 1
    else:
        n_maior = n_maior + 1
print('Há {} pessoas menores de idade e {} pessoas maiores de idade'.format(n_menor, n_maior))