"""
02lista-de-frutas

Algoritmo que ordena lista, verifica se certa palavra está na lista e sugera palavras proximas na lista (anterior e seguinte)
nivel: elementar
"""
#Lista
frutas = ["manga", "laranja", "abacaxi", "kiwi", "banana"]

# Ordenando alfabeticamente
frutas_ordenadas = sorted(frutas)
print(frutas_ordenadas)  # ['abacaxi', 'banana', 'kiwi', 'laranja', 'manga']


# Usando em um algoritmo de busca
def esta_no_dicionario(palavras, busca):
    """Verifica se uma palavra está na lista, e se não estiver, sugere a anterior e próxima"""
    palavras_ordenadas = sorted(palavras)

    if busca in palavras_ordenadas:
        return f"'{busca}' foi encontrada!"

    # Procurando posição da palavra
    for i, palavra in enumerate(palavras_ordenadas):
        if busca < palavra:
            anterior = palavras_ordenadas[i - 1] if i > 0 else " "
            return f"'{busca}' não encontrada. Você quis dizer '{anterior}' ou '{palavra}'?"

    return f"'{busca}' não encontrada. Última palavra é '{palavras_ordenadas[-1]}'."

#Solicitando entrada do usuário
busca = input("Digite o nome de uma fruta para buscar no dicionário: ").strip().lower()

"""
.strip(): Remove espaços extras no início e no final da string. 
Isso evita que entradas como " maçã " sejam interpretadas incorretamente devido ao espaço antes ou depois da palavra.

.lower(): Converte todos os caracteres da string para minúsculas, 
garantindo que a comparação não seja afetada por maiúsculas e minúsculas. 
Por exemplo, "KiWi" será transformado em "kiwi" para evitar discrepâncias.
"""


# Execução do algoritmo
print(esta_no_dicionario(frutas, busca))


