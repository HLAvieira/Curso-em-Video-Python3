num = int(input('\033[7;30mDigite um número inteiro:\033[m '))
base = int(input('''Escolha uma base de conversão:
1 - Binário
2 - Octal
3 - Hexadecimal
'''))
if base == 1:
    print('o número {} em binário é {}'.format(num, bin(num)))
elif base == 2:
    print('o número {} em octal é {}'.format(num, oct(num)))
elif base == 3:
    print('o número {} em hexadecimal é {}'.format(num, hex(num)))
else:
    print('Opção inválida =-= tente novamente')