#Solicite ao usuário um valor numérico, inteiro ou real
#Escrever se é positivo ou negativo (considere o valor zero como positivo).

number=float(input('Digite um numero inteiro ou real:'))

if number >= 0:
    print(f'{number} é um numero positivo')

else:
    print(f'{number} é um numero negativo')