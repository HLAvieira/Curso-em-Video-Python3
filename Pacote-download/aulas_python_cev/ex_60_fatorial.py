n = int(input('Digite um número para calcular seu fatorial: '))
c = n
culm = 1
print(f'{n} ! = ', end='')
while c > 0:
    culm = culm * c
    print(f'{c} ', end='')
    print(' X ' if c > 1 else ' = ', end='')
    c -= 1
print((culm))
'''n = int(input('Digite um número para calcular seu fatorial: '))
c = n
cuml = 1
if n == 0:
    print('0! é igual a 1')
else:
    for i in range(n, 0, -1):
        cuml = cuml*i
    print('{}! é igual a {}'.format(c, cuml))'''
