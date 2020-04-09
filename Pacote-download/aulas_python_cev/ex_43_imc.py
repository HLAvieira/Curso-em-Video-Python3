massa = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua alturam em metros: '))
imc = massa/(altura**2)
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc <= 25:
    print('peso ideal')
elif 25 < imc <= 30:
    print('sobrepeso')
elif 30 < imc <= 40:
    print('Obesidade')
else:
    print('obesidade mórbida')