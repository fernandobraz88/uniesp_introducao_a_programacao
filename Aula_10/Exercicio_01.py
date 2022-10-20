# Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol (ok)
# Armazene os nomes lidos em um vetor (lista). (ok)
# Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube
# Depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (ok)
# ou NÃO ACHEI caso contrário. (ok)


import re


times=[]

while len(times)<10:
    time=input("Insira o nome de um Time de futebol:").upper()
    
    if time in times:
        print('Você ja inseriu esse Time de Futebol')
    else:
        times.append(time)

print(times)

consulta=input('Qual o time que você deseja procurar na lista?').upper()
ordem=times.index(consulta)

for i in times:
    if (i==consulta):
        print(f'Achei!!, o time {consulta} está na posição {ordem} da lista')
    else:
        print('Não achei!!!')