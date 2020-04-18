a = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))
c = 1
mais_num = a
while mais_num != 0:
    while c <= 10:
        print('O {}º termo é igual a {}'.format(c, a))
        a = a+r
        c += 1
    mais_num = int(input('Deseja ver mais quantos termos? '))
    for i in range(c, (c + mais_num)):
        print('o {}º termo é igual a {}'.format(c, a))
        a = a + r
        c += 1
print('Obrigado!')
