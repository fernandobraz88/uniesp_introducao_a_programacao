
print('Para resolver uma equação do segundo grau do tipo Ax²+Bx+C=0 digite os valores de A, B e C:  ')
A=float(input('Valor de A: '))
B=float(input('Valor de B: '))
C=float(input('Valor de C: '))

Delta=(B**2)-4*A*C

print(f'Delta = {Delta}')

X1= (-B+(Delta**0.5))/(2*A)
print(f'X1 = {X1}')

X2= (-B-(Delta**0.5))/(2*A)
print(f'X2 = {X2}')