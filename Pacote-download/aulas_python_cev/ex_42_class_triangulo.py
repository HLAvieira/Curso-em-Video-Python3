a = float(input('Comprimeto do primeiro lado: '))
b = float(input('Comprimeto do segundo lado: '))
c = float(input('Comprimeto do terceiro lado: '))
if a < b+c and b < a+c and c < b+a:
    print('Esse triânulo existe')
    if a == b ==c :
        print('O triângulo é equilátero')
    elif a == b or a == c or b == c:
        print('O triãngulo é isóceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Esse triângulo não existe')
