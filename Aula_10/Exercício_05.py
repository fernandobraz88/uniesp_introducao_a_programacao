#Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B. Exemplo: A[0] + B[0] deverá ser salva em N[0]. (ok)

#======================Concluido=============================

from random import randint

N=[]
A=[]
B=[]

for i in range(5):
    A.append(randint(1,10))
    B.append(randint(1,10))

print(A)
print(B)

for x in range(len(A)):
    N.append(A[x]+B[x])


print(N)