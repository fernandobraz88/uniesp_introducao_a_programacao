# Ler dois valores (considere que não serão lidos valores iguais)
# escrever o maior deles.

from cgitb import reset


valor1=float(input('Digite um valor qualquer:'))
valor2=float(input('Digite outro (diferente do anterior):'))

while valor1 != valor2:

    if valor1 > valor2:
        print(f'{valor1} é maior')

    else:
        print(f'{valor2} é maior')


