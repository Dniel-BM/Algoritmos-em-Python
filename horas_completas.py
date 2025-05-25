import math
#calcule as horas completas e o valor a pagar total a partir do valor inserido por hora

horas_trabalhadas = float(input("Horas trabalhadas: "))
horas_completas = math.floor(horas_trabalhadas)
print(f"{horas_trabalhadas} horas trabalhadas = {horas_completas} horas completas")

valorPorHora = float(input("Valor da hora: "))
valorTotal = valorPorHora * horas_completas
print(f"Total a pagar: {valorTotal}")
