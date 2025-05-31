"""
06ver-limitVelo
Verifica se velocidade do objeto está dentro do limite de velocidade estabelecido,
corrija erros de entrada como velocidade 0, valor negativo ou tipo de dado incompativel

"""
print("Verificando limite de velocidade:")
while True:
    try:
        velocidade_str = input("Velocidade: ").strip()
        velocidade = float(velocidade_str)

        if velocidade < 0:
            print("ERRO: velocidade não pode ser negativa")
            input("Pressione enter para continuar...")
            print("Verificando limite de velocidade:")
            continue
        if velocidade == 0:
            print("Objeto parado, não é possível analisar")
            input("Pressione enter para continuar...")
            print("Verificando limite de velocidade:")
            continue

    except ValueError:
        print("ERRO: valor inválido")
        input("Pressione enter para continuar...")
        print("Verificando limite de velocidade:")
        continue

    break

limite_velocidade = 60
dentro_limite = velocidade <= limite_velocidade

print(f"Velocidade atual: {velocidade} km/h")
print(f"Limite: {limite_velocidade} km/h")
print(f"Dentro do limite: {dentro_limite}")

if dentro_limite == True:
    print("\nCirculando dentro do limite")
else:
    print("\nCirculando fora do limite")
