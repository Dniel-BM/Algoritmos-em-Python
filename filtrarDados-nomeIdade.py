"""
09filtrarDados-nomeIdade.py
Faça um algoritmo que filtre os dados de uma lista. Separe os dados somente com letras na lista nomes e os dados somente com números na lista idades
nível: elementar
"""
dados = ["Pedro", "25", "Maria", "30", "João", "50"]
nomes = [nome for nome in dados if nome.isalpha()]
idades = [idade for idade in dados if not idade.isalpha()]
print("Nomes", nomes)
print("Idades", idades)

