#Seja criativo ao desenvolver este programa.
#a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
#b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
#c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.
#d. Modifique sua lista, substitua os desistentes por novos convidados.
#e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

convidados = ['Chaves','Quico','Chiquinha','Nhonho','Popis'] 

for nome in convidados:
    print(f"Querido(a) {nome}, venha a minha casa hoje comer sanduiche de presunto e tomar refresco de procedencia duvidosa")  

print("Popis não poderá ir ao jantar") 

convidados_2 = ['Chaves','Quico','Chiquinha','Nhonho'] 

for nome in convidados_2:
    print(f"Querido(a){nome}, venha a minha casa hoje comer sanduiche de presunto e tomar refresco de procedencia duvidosa")