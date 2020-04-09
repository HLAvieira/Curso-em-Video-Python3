nome = input(str('digite seu nome completo: '))
print("""seu nome em maísculas é: {}
seu nome em mínusculas é: {}
seu nome possui {} letras
seu primeiro nome é {}""".format(nome.upper(), nome.lower(), len(''.join(nome.split())), nome.split()[0]))
