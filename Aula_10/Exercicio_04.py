# Ler um vetor A de 10 números. 
# Após, ler mais um número e guardar em uma variável X. 
# Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. 
# Logo após, imprimir o vetor M.


A=[]
M=[]
while len(A)<10:
    Number=int(input("Digite um numero até juntar 10 em uma lista:"))
    A.append(Number)

X=int(input("Agora digite um multiplicador:"))

for n in A:
    resultado=n*X
    M.append(resultado)
   
print(M)

