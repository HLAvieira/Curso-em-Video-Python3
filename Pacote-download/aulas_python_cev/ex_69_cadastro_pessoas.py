older = m_total = w_under20 = 0
age = -1
menu = sex = 'a'

while menu not in 'NS':
    menu = str(input('''Deseja adicionar uma pessoa?
[ S ] - Sim
[ N ] - Não
''')).strip().upper()[0]
    if menu == 'S':
        while sex not in 'MFO':
            sex = str(input('''Qual o sexo da pessoa?'
[ M ] - Masculino 
[ F ] - Feminino
[ O ] - Outro
''')).strip().upper()[0]
            if sex == 'M':
                m_total += 1
        while age < 0:
            age = int(input('Qual a idade da pessoa? '))
            if age >= 18:
                older += 1
            if sex == 'F' and age < 20:
                w_under20 += 1
    elif menu == 'N':
        break
    menu = 'a'
    sex = 'a'
    age = -1
print('obrigado')
print(f'Nos registros há {older} pessoas com 18 anos ou mais, {m_total} homens ao todo e {w_under20} mulheres com menos de 20 anos')