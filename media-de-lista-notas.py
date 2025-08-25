"""
media-de-lista-notas
Algoritmo que recebe lista de notas, efetua testes e condicoes (float,
nota > 0) retornando media da lista de notas e quantidade de notas. Criando uma
interface que confirma ou nao a selecao de notas, retornando para corrigir se
o usuario indicar. Robusto contra erros como inserir caracteres inadequados na
entrada de notas

"""
def get_notas():
    while True:
        try:
            notas_str = input("Digite notas separadas por um espaco: ")
            notas = [float(nota) for nota in notas_str.split()]
            if all ( 0 <= nota <= 10 for nota in notas):
                return notas
            else:
                print("Erro: as notas devem estar entre 0 e 10.")
        except ValueError:
            print("Erro: Insira apenas numeros.")

def main():
    while True:
        notas = get_notas()
        print(f"Notas: {notas}")
        confirma = input("Confirmar envio de notas: \nDigite[s] para "
                         "confirmar ou [n] para inserir notas novamente:\n> "
                         "_ ").lower().strip()
        if confirma == 's':
            break

    soma = sum(notas)
    qtdnotas = len(notas)

    if qtdnotas > 0:
        media = soma /qtdnotas
        print(f"Media final: {media:.2f}")
    else:
        print("Nenhuma nota foi inserida")
if __name__ == "__main__":
    main()

"""
#DOC-STRING GEMINI
# Define a new function to get and validate grades.
def get_notas():
    # Docstring for the function.
    # Loop indefinitely until valid input is received.
    while True:
        # Try to convert input to floats, handling potential errors.
        try:
            # Prompt user for notes, separated by spaces.
            notas_str = input("Digite notas separadas por um espaco: ")
            # Convert string input to a list of floats.
            notas = [float(nota) for nota in notas_str.split()]
            # Validate if all notes are within the 0-10 range.
            if all(0 <= nota <= 10 for nota in notas):
                # Return valid notes.
                return notas
            # Inform user about invalid note range.
            else:
                print("Erro: As notas devem estar entre 0 e 10.")
        # Handle non-numeric input.
        except ValueError:
            print("Erro: Insira apenas numeros.")
"""

"""
# Define the main function for program execution.
def main():
    # Docstring for the main function.
    # Loop until notes are confirmed.
    while True:
        # Get notes using the helper function.
        notas = get_notas()
        # Display the notes to the user.
        print(f"As notas inseridas sao: {notas}")

        # Ask for confirmation from the user.
        confirma = input(
            "Confirmar envio de notas:\nDigite [s] para confirmar ou [n] para inserir as notas novamente:\n> _ "
        ).lower().strip()

        # If confirmed, break the loop.
        if confirma == 's':
            break
"""
"""
    # Calculate the sum of notes.
    soma = sum(notas)
    # Get the quantity of notes.
    qtdDeNotas = len(notas)

    # Calculate media if there are notes.
    if qtdDeNotas > 0:
        # Calculate and print the final average, formatted to two decimal places.
        media = soma / qtdDeNotas
        print(f"Media final: {media:.2f}")
    # Handle case where no notes were entered.
    else:
        print("Nenhuma nota foi inserida.")
    """

"""
# Standard boilerplate to run the main function.
if __name__ == "__main__":
    main()
"""
