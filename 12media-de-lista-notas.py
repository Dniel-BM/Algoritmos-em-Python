"""
12media-de-lista-notas
Algoritmo que recebe lista de notas, efetua testes e condicoes (float,
nota > 0) retornando media da lista de notas e quantidade de notas. Criando uma
interface que confirma ou nao a selecao de notas, retornando para corrigir se
o usuario indicar. Robusto contra erros como inserir caracteres inadequados na
entrada de notas, validando os inputs inseridos

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
