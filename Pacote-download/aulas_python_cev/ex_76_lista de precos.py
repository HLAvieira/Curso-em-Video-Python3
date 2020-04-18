produtos_e_precos = ('arroz', 11.50, 'feijão', 5.97, 'refrigereante', 6.25, 'papel toalha', 3.70)
print('=-='*17)
print(f'{"LISTAGEM DE PREÇOS":^51}')
print('=-='*17)
for i in range(0, len(produtos_e_precos), 2):
    print(f'{produtos_e_precos[i]:.<40}', end=' ')
    print(f'R${produtos_e_precos[i+1]:>7.2f}')
