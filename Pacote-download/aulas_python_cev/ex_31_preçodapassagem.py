km = float(input('Insira a distância da viagem em Km: '))
if km <= 200:
    print('o preço da passagem é R$ {:.2f}'.format(0.50*km))
else:
    print('o preço da passagem é R$ {:.2f}'.format(0.45*km))