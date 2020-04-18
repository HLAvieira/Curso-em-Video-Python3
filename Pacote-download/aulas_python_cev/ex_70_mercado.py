prod_over1000 = total_cost = 0
min_price = 10**10000
menu = min_prod = ' '
while True:
    product_name = str(input('Digite o nome do produto: '))
    product_price = float(input('Digite o preço do produto R$ '))
    total_cost += product_price
    if product_price > 1000:
        prod_over1000 += 1
    if product_price < min_price:
        min_price = product_price
        min_prod = product_name
    while menu not in 'NS':
        menu = str(input('Deseja adicionar mais um produto? [S/N]')).upper().strip()
    if menu == 'N':
        break
    else:
        menu = ' '
print(f'''Obrigado por Comprar, o valor final é de R${total_cost:.2f}, 
o produto mais barato foi {min_prod}, no valor de RS{min_price:.2f} e
{prod_over1000} produtos foi (foram) acima de R$1000.00''')