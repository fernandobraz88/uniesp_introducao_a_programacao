#Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir: (ok)
#   a. o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor; (ok)
#   b. o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor; (ok)

#======================Concluido=====================================

Q=[]

while len(Q) <20:
    Num=int(input("Digite Numeros Inteiros para adiciona-los na lista:"))
    if Num in Q:
       print('Numero repetido, digite outro')
    
    elif Num < 0:
        print("Digite apenas Numeros Positivos")
        
    else:
        Q.append(Num)
        


menorvalor=99999999
maiorvalor=0

for valor in Q:
    if valor > maiorvalor:
        maiorvalor=valor
        
print(f'O valor do maior elemento de Q é {maiorvalor}')

for valor in Q:
    if valor < menorvalor:
        menorvalor=valor

print(f'O valor do menor elemento de Q é {menorvalor}')
