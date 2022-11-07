# Use um dicionário para armazenar informações sobre uma pessoa que você conheça.
# Armazene seu primeiro nome. 
# O sobrenome.
# A idade
# e a cidade em que ela vive. 
# Você deverá ter chaves como primeiro_nome, sobrenome, idade, e cidade. 
# Por fim, mostre cada informação armazenada em seu dicionário.


dicionario={
    'Primeiro_nome': 'João',
    'Sobrenome': 'Oliveira',
    'Idade': '33',
    'Cidade':'João Pessoa'
}

for info in dicionario.items():
    print(info)

