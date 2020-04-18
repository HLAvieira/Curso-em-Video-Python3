nasc = int(input('Digite seu ano de nascimento: '))
from datetime import date
idade = (date.today().year - nasc)
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('Sênior')
else:
    print('MASTER')