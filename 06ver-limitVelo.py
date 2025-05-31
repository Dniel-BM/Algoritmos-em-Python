"""
06ver-limitVelo
Verifica se velocidade do objeto está dentro do limite de velocidade estabelecido

"""


print("Verificando limite de velocidade:")
velocidade_atual = float(input("\nVelocidade atual:"))
limite_velocidade = 60
dentro_limite = velocidade_atual <= limite_velocidade

print(f"Velocidade atual: {velocidade_atual} km/h")
print(f"Limite: {limite_velocidade} km/h")
print(f"Dentro do limite: {dentro_limite}")

if dentro_limite == True:
    print("\nCirculando dentro do limite")
else:
    print("\nCirculando fora do limite")
