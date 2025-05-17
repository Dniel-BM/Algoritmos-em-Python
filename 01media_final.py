#Algoritmos em C
"""
01media_final: script que recebe 4 notas e retorna a media final
Fonte:Lógica de Programação com aplicações em Python. Eberspächer e Forbellone. 4a Edição, Pearson, 2022.
nivel: elementar.
"""

N1 = float(input("Nota 1: "))
N2 = float(input("Nota 2: "))
N3 = float(input("Nota 3: "))
N4 = float(input("Nota 4: "))

nota_final=(N1 + N2 + N3 + N4)/4

print(nota_final)
if nota_final >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
