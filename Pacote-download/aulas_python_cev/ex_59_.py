a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
menu = int(input('''Escolha a opção desejda:
[ 1 ] - SOMAR
[ 2 ] - MULTIPLICAR
[ 3 ] - MAIOR
[ 4 ] - NOVOS NÚMEROS
[ 5 ] - SAIR DO PROGRAMA
'''))
while menu != 5:
    if menu == 1:
        print('a soma dos números é igual a {} '.format(a+b))
    elif menu == 2:
        print('O produto dos dois números é igual a {}'.format(a*b))
    elif menu == 3:
        if a > b:
            print('O maior número é igual a {}'.format(a))
        elif b > a:
            print('O maior número é igual a {}'.format(b))
        else:
            print('Os dois números são iguais')
    elif menu == 4:
        print('Você escolherá novos números')
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
    menu = int(input('''Escolha a opção desejda:
[ 1 ] - SOMAR
[ 2 ] - MULTIPLICAR
[ 3 ] - MAIOR
[ 4 ] - NOVOS NÚMEROS
[ 5 ] - SAIR DO PROGRAMA
'''))
print('Obrigado por usar o Programa')
