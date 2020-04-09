print('\033[1;31;40mBem vindo ao avaliador de empréstimo\033[m')
sal = float(input('Digite o valor da sua renda mensal: R$ '))
preco = float(input('Digite o valor do empréstimo desejado: R$ '))
num_parcelas = float(input('Digite o número de parcelas mensais que você deseja obter: '))
val_parcela = preco/num_parcelas
if val_parcela > 0.3*sal:
    print('Infelizmente essas condições não são possíveis, entre em contato com nossos atendentes')
else:
    print('Seu empréstimo de {:.2f} foi provado, você paragará {:.0f} parcelas de R${:.2f}'.format(preco, num_parcelas, val_parcela))
print('Obrigado por negociar conosco')