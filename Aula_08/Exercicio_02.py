#Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano,
# P(x1, y1) e Q(x2, y2), imprima a distância entre eles.

print('Para calcular a distancia entre os pontos P e Q, digite as coordenadas x e y dos mesmos. Vamos lá?')

print('Primeiro vamos aos valores de P:')

xp=float(input('Digite o X do ponto P:'))
yp=float(input('Digite o Y do ponto P:'))

print('Agora vamos aos valores de Q:')

xq=float(input('Digite o X do ponto Q:'))
yq=float(input('Digite o Y do ponto Q:'))

Distancia=(((xq-xp)**2)+((yq-yp)**2))**0.5
print(f'A distancia entre os pontos P e Q é {Distancia:,.2f}')