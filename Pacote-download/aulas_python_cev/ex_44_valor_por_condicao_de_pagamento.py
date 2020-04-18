valor = float(input('Digite o valor ddo produto: R$ '))
pag = int(input('''Escolha a forma de pagamento:
1 - À vista no dinheiro
2 - Débito
3 - até 2x sem juros
4 - 3x a 12x
'''))
if pag == 1:
    print('O valor final do produto é R${:.2f}'.format(valor*0.9))
elif pag ==2:
    print('O valor final do produto é R${:.2f}'.format(valor * 0.95))
elif pag == 3:
    print('O valor final do produto é R${:.2f}'.format(valor))
elif pag == 4:
    print('O valor final do produto é R${:.2f}'.format(valor * 1.2))
else:
    print('\033[31mOpção de pagamento inválida\033[m')