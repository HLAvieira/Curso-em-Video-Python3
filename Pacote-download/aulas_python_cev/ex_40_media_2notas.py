n1 = (float(input('Digite a primeira nota: ')))
n2 = (float(input('Digite a segunda nota: ')))
media = (n1+n2)/2
if media < 5:
    print('\033[1;31mREPROVADO\033[m')
elif 5 <= media < 7:
    print('Recuperação')
elif 7 <= media < 10:
    print('APROVADO')
else:
    print('Notas inválidas')