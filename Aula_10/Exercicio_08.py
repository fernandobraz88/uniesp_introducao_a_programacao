#Faça um algoritmo para ler um vetor de 30 números. (ok)
#Após isto, ler mais um número qualquer (ok)
#Calcular e escrever quantas vezes esse número aparece no vetor. (ok)

#=========================Concluido=================================

from random import randint

vetor=[]
Q=[]

for i in range(30):
    vetor.append(randint(0,5))

print(vetor)

nq=int(input('Digite um numero de 0 a 5 e veja quantas vezes ele aparece na lista: '))

for x in vetor:
    if (x==nq):
        Q.append(x)

print(f'{nq} aparece no vetor {len(Q)} vezes')