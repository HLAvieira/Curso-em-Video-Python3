import random
from time import sleep
seu_num = input('Digite um número de 0 a 5: ')
pc_num = random.randint(0, 5)
print('PROCESSANDO')
sleep(1)
print('=-='*20)
sleep(1)
print('PROCESSO FINALIZADO')
sleep(1)
print('=-='*20)
sleep(1)
print('''Seu número escolhido foi {}
O número sorteado foi {}'''.format(seu_num, pc_num))
if int(seu_num) == int(pc_num):
    print('Parabéns, você acertou')
else:
    print('Que pena, boa sorte na próxima')

