from datetime import date
ano = int(input('''Digite um ano para conferir se ele é bissextou ou não
Aperte 0 para selecionar o ano atual
Ano desejado: '''))
if ano == 0:
    ano = date.today().year

if (ano % 4) == (0) and ((ano % 100) != (0) or ((ano % 100) == (0)and (ano % 400) == (0))):
    print('{} é ano bissexto'.format(ano))
else:
    print('{} não é ano bissexto'.format(ano))