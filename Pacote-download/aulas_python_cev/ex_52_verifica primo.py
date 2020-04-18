num = int(input('Digite um número: '))
div = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[33m', end='')
        div = div+1
    else:
        print('\033[31m', end='')
    print(i)
print('{} é um número primo'.format(num) if (div == 2) else '{} não é um número primo'.format(num))
