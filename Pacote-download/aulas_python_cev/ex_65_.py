q_num = 0
soma_num = 0
maior = menor =0
menu = 'S'
while menu in 'Ss':
    num = int(input('digite um número: '))
    q_num += 1
    soma_num += num
    if q_num == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    menu = str(input('Deseja continuar? S/N ')).strip().upper()[0]
print('a soma dos {} termos é igual a {} e sua média é igual a {}'.format(q_num, soma_num, soma_num/q_num))
print('O maior número é {} e o menor número é {}'.format(maior, menor))
print('Obrigado')
