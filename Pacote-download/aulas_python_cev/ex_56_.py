soma_idade = 0
maior_idade = -1
h_m_velho = ''
mulh_menr_20 = 0
for i in range(0,4):
    nomes = str(input('Digite o nome da {}ª pessoa: '.format(i+1)))
    idades = int(input('Digite a idade da {}ª pessoa: '.format(i+1)))
    sexo = int(input('''selecione o sexo da {}ª pessoa:
1 - Homem
2 - Mulher
'''.format(i+1)))
    if sexo == 1 and idades > maior_idade:
        maior_idade = idades
        h_m_velho = nomes
    elif sexo == 2:
        if idades > 20:
            mulh_menr_20 = mulh_menr_20 + 1
    soma_idade = soma_idade + idades
print('a média de idadades é de {} ano(s)'.format(soma_idade/4))
print('O homem mais velho é o {} com {} anos'.format(h_m_velho, maior_idade))
print('Há {} mulher(es) com mais de 20 anos'.format(mulh_menr_20))