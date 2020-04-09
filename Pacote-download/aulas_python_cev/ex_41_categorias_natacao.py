nasc = int(input('Digite seu ano de nascimento: '))
from datetime import date
idade = (date.today().year - nasc)
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 20:
    print('Sênior')
else:
    print('MASTER')