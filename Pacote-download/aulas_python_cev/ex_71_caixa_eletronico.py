bill_50 = bill_20 = bill_10 = bill_1 = 0
rest = 1
cash = int(input('Qual o valor a ser sacado? R$ '))
while cash // 50 >= 1:
    bill_50 += 1
    cash -= 50
while cash // 20 >=1:
    bill_20 += 1
    cash -= 20
while cash // 10 >=1:
    bill_10 += 1
    cash -= 10
while cash // 1 >= 1:
    bill_1 += 1
    cash -= 1
print(f'''Total de {bill_50} nota(s) de R$50.00
Total de {bill_20} nota(s) de R$20.00
Total de {bill_10} nota(s) de R$10.00
Total de {bill_1} nota(s) de R$1.00''')
