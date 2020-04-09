sal = float(input('Digite o Valor do salário: '))
if sal > 1250:
    print('Você receberá 10% de aumento e seu novo salário será de R${:.2f}'.format(sal*1.1))
else:
    print('Você receberá 15% de aumento e seu novo salário será de R${:.2f}'.format(sal*1.15))