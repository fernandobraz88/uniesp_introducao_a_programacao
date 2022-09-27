# O Programa deve:
# Ler o ano atual e o ano de nascimento de uma pessoa. 
# Escrever uma mensagem que diga se ela poderá ou não votar este ano 
# (não é necessário considerar o mês em que a pessoa nasceu).

nasc=int(input('Digite o ano que você nasceu: '))
idade=2022-nasc

if idade < 16:
    print('Infelizmente você não está apto a votar ainda')

elif idade >= 16 and idade < 18:
    print('Você já pode votar caso deseje.')

else:
    print('Você é obrigado a votar')