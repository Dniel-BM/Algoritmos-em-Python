"""
08valide-username.py
crie um algoritmo que valide a entrada de dados para criação de usuario,
de forma a cumprir a condição de receber apanas letras,
sem espaços ou numeros,
crie um laço de repetição para que o programa
volte ao inicio se houver erro
nivel: elementar
"""

while True:
    username = input("!! Crie um username (apenas com letras) !!\nUSERNAME: ")
    if username.isalpha():
        print("Username aceito!")
        break
    else:
        print("Username deve conter apenas letras, sem números ou símbolos")
