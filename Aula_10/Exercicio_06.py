#Faça um algoritmo para ler um vetor de 20 números. (ok)
#Após isto, deverá ser lido mais um número qualquer (ok)
#Verificar se esse número existe no vetor ou não.  (ok)
#Se existir, o algoritmo deve gerar um novo vetor sem esse número. (ok)(Considere que não haverão números repetidos no vetor).

#=======================Concluido==========================


from random import sample


matriz=sample(range(99),20)

print(matriz)

x=int(input('Digite o numero que você deseja procurar na lista:'))

for i in matriz:
    if (i==x):
        print(f'{x} está na lista')
        matriz.pop(matriz.index(x))
        print(f'Agora a lista é: {matriz}')
    

      