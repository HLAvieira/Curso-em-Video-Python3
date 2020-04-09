velocidade = float(input('Digite a velocidade do carro em Km/h ::::: '))
if velocidade > 80.0:
    print('você foi multado em R${:.2f} '. format((velocidade-80.0)*7))
else:
    print('Velocidade permitida')