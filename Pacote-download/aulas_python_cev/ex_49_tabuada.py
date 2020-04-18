num = int(input('digite um número: '))
for i in range(1, 11):
    print('''{} X {} = {}
{}'''.format(num, i, num*i, ('=-='*5)))