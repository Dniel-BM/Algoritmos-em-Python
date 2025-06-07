"""
08valide-username.py

crie um algoritmo que valide a entrada de dados para criação de usuario e ,
de forma a cumprir a condição de receber apanas letras no usuario,
sem espaços ou numeros adicionais, e na senha a condição de não conter apenas letras
crie um laço de repetição para que o programa volte ao inicio se houver erro.

nivel: elementar
"""

while True:
    username = input("!! Crie um username (apenas com letras) !!\nUSERNAME: ")
    if username.isalpha():
        print("Username aceito!")
        break
    else:
        print("Username deve conter apenas letras, sem números ou símbolos")

while True:
    print("\n!! Crie uma senha com letras e outros caracteres !!\n")
    senha = input("Crie uma senha: ")
    if senha.isalpha():
        print("\nSenha fraca! Use outros caracteres além de letras.")
    else:
        print("Senha aceita")
        break

print(f"\nUSER: {username}")
print(f"SENHA: {senha}")
