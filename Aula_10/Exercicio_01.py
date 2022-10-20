# Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol
# Armazene os nomes lidos em um vetor (lista). 
# Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube
# Depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente
# ou NÃO ACHEI caso contrário.

lista_times=[]

while lista_times in range(0,9):
    lista_times=input("Insira o nome de um Time de futebol:")