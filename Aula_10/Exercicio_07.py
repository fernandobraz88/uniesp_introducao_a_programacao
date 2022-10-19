from random import randint

V1=[]
V2=[]

for n in range(10):
    V1.append(randint(0,5))
    V2.append(randint(0,5))

print(V1)
print(V2)

#Criar a lógica para comparar se um número é igual e está na mesma posição em V1 e V2

for N in range (len(V1)):
    if V1[N]==V2[N]:
        print(f'o valor {V1[N]} foi encontrado nas 2 matrizes na posição {N}')