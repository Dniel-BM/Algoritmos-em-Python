"""
10adivinhando-num-1-100.py
Algoritmo que cria um jogo de adivinhação
onde o usuario tenta advinhar um número sorteado entre 1 e 100
com número de tentativas definidos
e dicas ao longo das tentativas revelando se o número é maior ou menor
nível: fácil
"""

import random

numero_sorteado = random.randint(1, 100)
tentativa = 1
limite_tentativas = 11
acertou = False

print("Jogo de Adivinhação")
print(f"Você tem {limite_tentativas} tentativas para adivinhar o número sorteado entre 1 e 100")

while tentativa < limite_tentativas and not acertou:
    palpite = int(input(f"Palpite {tentativa}: "))
    tentativa += 1

    if palpite == numero_sorteado:
        print(f"Parabéns! Você acertou o número {numero_sorteado} na {tentativa-1} tentativa.")
        acertou = True
    elif palpite < numero_sorteado:
        print("O número é maior")
    else:
        print("O número é menor")

if not acertou:
    print(f"Game Over! O número sorteado era {numero_sorteado}")



