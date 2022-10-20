#Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir: (ok)
#   a. o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
#   b. o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;


Q=[]

while len(Q) <20:
    Num=int(input("Digite Numeros Inteiros para adiciona-los na lista:"))
    if Num >=0:
        Q.append(Num)
    else:
        print("Digite apenas Numeros Positivos")