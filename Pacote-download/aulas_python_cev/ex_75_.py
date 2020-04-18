
nums = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
for i in nums:
    if i%2 == 0:
        print(f'{i} é par ')
if 9 in nums:
    print(f'O número 9 foi digitado {nums.count(9)} vez(es)')
if 3 in nums:
    print(f'O primeiro 3 digitado foi na {nums.index(3)+1}ª posição')

