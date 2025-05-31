"""
07ver-idadeMin-P-CNH
Algoritmo que verifica idade mínima para tira CNH e corrige usuário caso insira dados
incompativeis
"""

print("\nVerificar se possível tirar CNH")

while True:
    try:
        idade_str = input("Digite sua idade: ")
        if '.' in idade_str:
            print("Erro: a idade não pode ser um número decimal, retire o '.'")
            continue
        if ',' in idade_str:
            print("Erro: a idade não pode ser um número decimal, retire a ','")
            continue
        idade = int(idade_str)

        if idade <= 0:
            print("Erro: a idade não pode ser um valor negativo ou '0'")
            continue

        pode_dirigir = idade >= 18
        print(f"Idade: {idade} anos")
        print(f"Pode dirigir? {pode_dirigir}")

        if pode_dirigir == False:
            print("\nNão pode tirar CNH")
        else:
            print("\nPode tirar CNH")
        break

    except ValueError:
        print("Erro: informe a sua idade com números inteiros")
        continue