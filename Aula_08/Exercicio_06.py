#Esse codigo consiste em que o usuario faça uma entrada de dados (um numero)
#e o programa calcule o fatorial desse numero e imprima a conta EX:
# 6!  =>  6 x 5 x 4 x 3 x 2 x 1 = 720

from math import factorial

n=int(input('Informe um número inteiro para calcular o seu fatorial: '))

f=factorial(n)

v=n

while v > 0:
    print(f'{v}', end ='')
    print(' x ' if v>1 else ' = ', end ='')
    v-=1
print(f'{f}')
