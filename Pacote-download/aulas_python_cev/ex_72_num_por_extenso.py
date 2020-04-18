num = int(input('Digite um número entre 0 e 5: '))
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
while num not in range(0, len(extenso)):
    num = int(input('Digite um número entre 0 e 5: '))
print(f'{num} por extenso é {extenso[num]}')