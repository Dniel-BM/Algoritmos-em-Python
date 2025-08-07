"""
11Sistema-de-notas
Algoritmo que recebe diversas notas, recebe como lista, confirma entrada do usuario e calcula a media
"""

notas = [float(nota) for nota in input("Digite notas separadas por um espaco: ").split()]
qtdDeNotas = 0
soma = 0

print(f"As notas inseridas sao: {notas}")

confirma = input("Confirmar envio de notas:\nDigite [s] para confirmar ou ["
                 "n] para inserir as notas novamente:\n> _ ").lower().strip()

while confirma != 's':
    print("Retornando para insercao de notas")
    notas = input("Digite notas separadas por um espaco: "
                               "").split()
    confirma = input(
        "Confirmar envio de notas:\nDigite [s] para confirmar ou ["
        "n] para inserir as notas novamente:\n> _ ").lower().split()

print(notas)
print(type(notas))
for nota in notas:
    if nota < 0 and nota > 10:
        print("Nota invalida! Nao sera contabilizada na soma")
        prossiga = input("Deseja prosseguir mesmo assim?\n> _")
        continue
    soma += nota
    qtdDeNotas += 1
if qtdDeNotas > 0:
    media = soma / qtdDeNotas
print(f"Media final {media}")
