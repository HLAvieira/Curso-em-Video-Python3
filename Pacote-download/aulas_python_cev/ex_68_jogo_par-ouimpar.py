from random import randint
num_jogador = -1
choice = choice_result = 'a'
win = 0
while True:
        while num_jogador not in range(0, 6):
            num_jogador = int(input('Jogue um número de 0 a 5: '))
        while choice not in 'PpIi':
            choice = str(input('Escolha entre \033[1;34m par \033[m ou \033[1;32mímpar\033[m [P/I]')).upper().strip()
        print(f'Você escolheu o número {num_jogador}')
        comp_num = randint(0, 5)
        print(f'O computador escolheu {comp_num}')
        resultado = comp_num + num_jogador
        if resultado % 2 == 0:
            print(f'O resultado {resultado} é par')
            choice_result = str('P')
        else:
            print(f'O resultado é ímpar')
            choice_result = str('I')
        if choice == choice_result:
            win += 1
            print('Parabéns!!! Você Venceu')
        else:
            print('Que pena, você perdeu...')
            break
        num_jogador = int(input('Jogue um número de 0 a 5: '))
        choice = str(input('Escolha entre \033[1;34m par \033[m ou \033[1;32mímpar\033[m [P/I]')).upper().strip()
print(f'Você obteve {win} vitória(s)')