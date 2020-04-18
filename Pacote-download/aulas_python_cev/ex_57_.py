sex = '0'
while sex not in 'FMO':
    sex = str(input('''Bem vindo!
    Selecione seu sexo:
    [ M ] Masculino
    [ F ] Feminino
    [ O ] Prefiro não dizer
    ''')).upper().strip()[0]
print('Obrigado, sexo {} registrado com sucesso'.format(sex))
