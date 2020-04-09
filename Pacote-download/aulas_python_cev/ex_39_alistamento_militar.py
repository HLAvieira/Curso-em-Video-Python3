print('\033[1;32mBem vindno ao programa de alistamento militar brasileiro\033[m')
nasc = int(input('Digite seu ano de nascimento: '))
from datetime import date
idade = (date.today().year - nasc)
if idade == 18:
    print('Você deve se alistar este ano')
elif idade > 18:
    print('Você está atrasado {} ano(s) para seu alistamento'.format(idade - 18))
else:
    print('Você deverá se alistar em {} ano(s)'.format(18 - idade))