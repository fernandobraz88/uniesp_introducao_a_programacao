#criar lista: declarar variavel = [ "escrever a lista" ]

frutas=['pera','uva','maçã','kiwi']

print(frutas)

#para acessar o item na lista: variavel[N]
print(f'juliana gosta de {frutas[3]}')



#para inserir itens na lista:  variavel.insert(N, "Item")
frutas.insert(2, 'morango')

print(frutas)

#para trocar itens na lista: variavel[#]="novo item"
frutas[0]="melancia"
print(frutas)

#para deletar iten de determinada posição: del variável [#]
del frutas [0]
print(frutas)

#para saber a posição do iten na lista: variavel.index("nome do item")
indice_fruta=frutas.index('morango')
print(f'o indice da fruta é {indice_fruta}')


lista_mercado=[]
while True:

    op=input(' \
              1- Adicione frutas\n \
              2- Remover frutas\n \
              3- Lista frutas\n \
              0- Sair do Programa\n \
              Digite uma opção: ')


    if op==1:
        #adicionar itens na lista
        item=input('Digite o Item:')
        lista_mercado.append(item)
        

    elif op==2:
        #remover itens da lista
        item=input('Digite o item que será removido:')
        indice_item=lista_mercado.index(item)
        del lista_mercado[indice_item]

    
    elif op==3:
        for item in lista_mercado:
            print(item)

    
    elif op==0:
        break

print(lista_mercado)