#Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos (ok)
#Calcular a média da turma (ok)
#Contar quantos alunos obtiveram nota acima desta média calculada. (ok)
#Escrever a média da turma e o resultado da contagem. (ok)

#=================Concluido=====================

notas=[]

while len(notas)<20:
    nota=float(input("Digite a nota do aluno:"))
    notas.append(nota)



soma=sum(notas)



media=soma/len(notas)

print(f'a media da turma foi {media}')

alunos=[]
for aluno in notas:
    if aluno > media:
        alunos.append(aluno)

        
print(f'{len(alunos)} tiraram a nota acima da media')
