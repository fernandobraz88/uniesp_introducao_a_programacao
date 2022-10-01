# Ler as notas da 1a. e 2a. avaliações de um aluno. 
# Calcular a média aritmética simples
# Escrever uma mensagem que diga se o aluno foi ou não aprovado
# (considerar que nota igual ou maior que 6 o aluno é aprovado). 
# Escrever também a média calculada.

nota1=float(input('Digite o Nota da 1ª Avaliação:'))
nota2=float(input('Digite o Nota da 2ª Avaliação:'))

media=(nota1+nota2)/2

if media >=6:
    print(f'Parabens, com a media {media} você está aprovado')

else:
    print(f'Infelizmente com a media {media} você está reprovado. Estude mais da proxima vez')
