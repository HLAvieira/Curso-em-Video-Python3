import random
from time import sleep
seu_num = int(input('Digite um número de 0 a 10: '))
pc_num = random.randint(0, 10)
print('PROCESSANDO')
sleep(1)
print('=-='*20)
sleep(1)
print('PROCESSO FINALIZADO')
sleep(1)
print('=-='*20)
sleep(1)
chances = 1
acertou = False
while not acertou:
    if pc_num == seu_num:
        acertou = True
    else:
        if pc_num > seu_num:
            print('O valor deve ser mais alto')
            print('=-=' * 20)
        else:
            print('O valor deve ser mais baixo')
            print('=-=' * 20)
        chances += 1
        print('Tente mais uma vez')
        print('=-=' * 20)
        seu_num = int(input('Digite um número de 0 a 5: '))
print('Parabéns, você acertou na {}ª chance!'.format(chances))
