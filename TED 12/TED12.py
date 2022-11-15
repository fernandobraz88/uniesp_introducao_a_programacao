#Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos.
# Depois:Imprima o resultado da soma de todos os valores da matriz no terminal;
# E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

#---------------------------Concluído-----------------------------------------

import random

matrizA=[]
matrizB=[]

for l in range (10): 
    linha=[]
    for c in range (10):
        num=random.randint(1,10)
        linha.append(num)
    matrizA.append(linha)

print(matrizA)

for i in matrizA:
    linha2=[]
    for j in i:
        num2=j*3
        linha2.append(num2)
    matrizB.append(linha2)

print('a partir daqui é Matriz B')

print(matrizB)