num = int(input('Digite um número inteiro (digite 999 para sair): '))
cont = 0
soma = 0
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input('Digite um número inteiro (digite 999 para sair): '))
print('Você digitou {} números e a soma dees é igual a {}'.format(cont, soma))