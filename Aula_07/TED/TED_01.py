# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia,
# e R$ 1,00 se forem compradas pelo menos 12.
# Escreva um programa que leia o número de maçãs compradas, 
# calcule e escreva o custo total da compra.

macas=float(input('Quantas maçãs deseja comprar?: '))

if macas < 12:
    custo=macas*1.30
    print(f'Para {macas} maçãs, você irá gastar R${custo}')
else:
    custo=macas*1
    print(f'Para {macas} maçãs, você irá gastar R${custo}')
