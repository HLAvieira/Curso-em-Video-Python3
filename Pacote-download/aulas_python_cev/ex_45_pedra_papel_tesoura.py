from random import choice
from time import sleep
jogador = str(input('''Digite a opção que você quer jogar entre as possibilidades abaixo
Pedra
Papel
Tesoura
Escolha: ''')).strip().lower()
print('Você escolheu: {}'.format(jogador))
sleep(1)
comp = choice(['pedra', 'papel', 'tesoura'])
print('O computador escolheu: {}'.format(comp))
sleep(1)
print('''Resultado:
=-=-=-=-=-=-=-=-=-=-=-=-=-''')
sleep(2)
if jogador == comp:
    print('Empate')
elif jogador == 'pedra' and comp =='papel':
    print('Você perdeu')
elif jogador == 'pedra' and comp == 'tesoura':
    print('Você venceu')
elif jogador == 'papel' and comp == 'tesoura':
    print('Você perdeu')
elif jogador == 'papel' and comp == 'pedra':
    print('Você venceu')
elif jogador == 'tesoura' and comp == 'pedra':
    print('Você perdeu')
elif jogador == 'tesoura' and comp == 'papel':
    print('Você venceu')
