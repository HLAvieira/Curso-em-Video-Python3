a = str(input('Digite uma palavra ou frase: ')).lower().strip().split()
b = ''.join(a)
c = b[::-1]
print('o termo é um palíndromo' if b == c else print('o termo não é um palíndromo'))