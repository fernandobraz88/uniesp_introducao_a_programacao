from email.policy import default

#testando exercicio 05 com if/elif/else


lista1=[]
lista2=[]
lista3=[]
lista4=[]

numeros=1000

while numeros >=0:

    numeros=float(input('Digite numeros aleatorios (positivos e negativos):'))
    
    if numeros >=0 and numeros <=25:
        lista1.append(numeros)
        
    elif numeros >=26 and numeros <=50:
        lista2.append(numeros)
        
    elif numeros >=51 and numeros <=75:
        lista3.append(numeros)
        
    elif numeros >=76 and numeros <=100:
        lista4.append(numeros)

    elif numeros > 100:
        numeros

    else:
        print('a quantidade de numeros entre:')
        print(f'0-25 = {len(lista1)}')
        print(f'26-50 = {len(lista2)}')
        print(f'51-75 = {len(lista3)}')
        print(f'76-100 = {len(lista4)}')
