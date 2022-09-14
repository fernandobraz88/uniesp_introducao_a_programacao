from ast import For
from html.entities import name2codepoint


Nume1=int(input("Digite um Numero: "))

for Nume2 in range(1,11):
    resultado=Nume1*Nume2
    print(f'{Nume1} x {Nume2} = {resultado}')