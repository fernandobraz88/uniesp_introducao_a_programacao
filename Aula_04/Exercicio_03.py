# As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia
# E 1,00 se forem compradas pelo menos 12. 
# Escreva um programa que leia o número de maçãs compradas
# calcule e escreva o custo total da compra.


maças=int(input('Quantas maçãs você deseja comprar?:'))

if maças < 12:
    custo=maças*1.3
    print(f'Comprando {maças} maçãs, você irá gastar R${custo}')

else:
    custo=maças
    print(f'Comprando {maças} maçãs, você irá gastar R${custo}')