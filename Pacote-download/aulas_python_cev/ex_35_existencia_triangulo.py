a = float(input('Comprimeto do primeiro lado: '))
b = float(input('Comprimeto do segundo lado: '))
c = float(input('Comprimeto do terceiro lado: '))
if a < b+c and b < a+c and c < b+a:
    print('Esse triânulo existe')
else:
    print('Esse triângulo não existe')
