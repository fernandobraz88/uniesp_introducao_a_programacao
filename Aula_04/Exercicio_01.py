#Solicite ao usuário um valor numérico, inteiro ou real.
#verifique se ele é maior ou menor que 10. 
#O programa deve escrever a mensagem correspondente (maior ou menor)
#informar o valor digitado pelo usuário.

number=float(input('Digite um numero inteiro ou real:'))

if number > 10:
    print(f'{number} é maior que 10')

elif number == 10:
    print('você digitou o numero 10')

else:
    print(f'{number} é menor que 10')
