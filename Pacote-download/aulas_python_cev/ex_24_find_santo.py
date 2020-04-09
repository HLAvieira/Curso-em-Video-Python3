cidade = input(str('Digite o nome de uma cidade: '))
cidade_cap = cidade.title()
if cidade.title().find('Santo') == 0:
    print('A cidade começa com santo')
else:
    print('A cidade não começa com santo')
cidade = input(str('Digite o nome de uma cidade: '))
if 'Santo' in cidade.title().split()[0]:
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')
