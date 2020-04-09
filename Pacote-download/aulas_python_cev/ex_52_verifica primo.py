num = int(input('Digite um número: '))
div = 0
for i in range (1, num+1):
    if num % i == 0:
        div = div+1
print('{} é um número primo'.format(num) if (div == 2) else '{} não é um número primo'.format(num))
