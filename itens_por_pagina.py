#03itens-por-pagina
#Calcule quantas páginas são necessárias pelo numéro de itens
#nivel elementar

import math

itens_por_paginas = int(input("Quantos itens cabem em uma página?"))
itens_total = int(input("Quantidade de itens?"))
total_paginas= math.ceil(itens_total/itens_por_paginas)
print(f"Para o total de itens{itens_total} são necessarias {total_paginas} páginas")
