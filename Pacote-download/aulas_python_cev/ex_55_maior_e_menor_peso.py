n_maior = 0
n_menor = 10**1000000*10
for i in range(0, 4):
    peso = float(input('Digite o peso, em Kg, da {}ª pessoa: '.format(i+1)))
    if peso < n_menor:
        n_menor = peso
    elif peso > n_maior:
        n_maior = peso
print('o maior peso é {}Kg e o menor peso é {}Kg'.format(n_maior, n_menor))