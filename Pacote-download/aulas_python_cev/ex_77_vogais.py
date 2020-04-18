words = ('Palmeiras - SP', 'Flamengo - RJ', 'Internacional - RS', 'Grêmio - RS', 'São Paulo - SP', 'Atlético - MG', 'Athletico Paranaense - PR', 'Cruzeiro - MG', 'Botafogo - RJ', 'Santos - SP', 'Bahia - BA', 'Fluminense - RJ', 'Corinthians - SP', 'Chapecoense - SC', 'Ceará - CE', 'Vasco da Gama - RJ', 'America Fc - MG', 'Sport - PE', 'Vitória - BA', ' Paraná - PR')
for i in words:
    print(f'\nNo termo "{i.upper()}" há as vogais ', end ='')
    for p in i:
        if p.lower() in 'áéíóúaeiou':
            print(p.lower(), end=' ')

