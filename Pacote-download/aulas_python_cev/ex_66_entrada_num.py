cont = soma = 0
while True:
    num = int(input('Digite um número inteiro (999 encerra o programa): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} números, a soma deles é igual a {soma}')