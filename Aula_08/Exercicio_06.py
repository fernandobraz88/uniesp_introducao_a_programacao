from math import factorial

n=int(input('Informe um número inteiro para calcular o seu fatorial: '))

f=factorial(n)

v=n

while v > 0:
    print(f'{v}', end ='')
    print(' x ' if v>1 else ' = ', end ='')
    v-=1
print(f'{f}')
#print(f'O fatorial de {n} é {f}.')