soma = 0
for i in range(0, 6):
    num = float(input('Digite o {}º número: '.format(i+1)))
    if num % 2 ==0:
        soma = soma + num
print('a soma dos número pares digitados é igual a {:.0f}'.format(soma))