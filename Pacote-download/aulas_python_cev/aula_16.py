lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for pos, comida in enumerate(lanche):
    print(f'{pos+1}º vou comer')

for cont in range(0, len(lanche)):
    print(lanche[cont])
print(sorted(lanche)) #resultado está em uma lista
print(lanche)
a = (1,2,3)
b = (3,4,5)
c = b+a
print(c)
print(c.count(3)) #quantas vez aparece o item 3
print(c.index(3)) #index da primeira ocorrência do item 3
print(c.index(3, 1)) #deslocamento de index: index da primeira ocorrência do item 3 a partir do index 1 (após a vírgula)