"""
05ver-se-menor-de-idade.py
Algoritmo que verifica se usuário é maior de idade ou menor de idade, considerando os
erros que o usuario pode cometer ao utilizar valores incompatíveis

"""

import math

while True:
    try:
        idade_str = input('Digite sua idade: ')
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


        if idade >= 18:
            print("Voce é maior de idade")
        else:
            print("Voce é menor de idade")

        break

    except ValueError:
        print("Erro: informe a sua idade com valores inteiros")
        continue
