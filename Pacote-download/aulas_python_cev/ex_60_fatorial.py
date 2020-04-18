'''n = int(input('Digite um número para calcular seu fatorial: '))
c = n
culm = 1
while n > 0:
    culm = culm * n
    n = n-1
print('{}! é igual a {}'.format(c, culm))'''
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
cuml = 1
if n == 0:
    print('0! é igual a 1')
else:
    for i in range(n, 0, -1):
        cuml = cuml*i
    print('{}! é igual a {}'.format(c, cuml))