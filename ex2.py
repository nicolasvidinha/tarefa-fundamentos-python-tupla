import random

while True:

    numero = random.randint(1, 100)
    tentativas = 0
    historico = ()

    print("\n=== JOGO DE ADIVINHAÇÃO ===")
    print("Adivinhe um número entre 1 e 100.")
    print("Você tem no máximo 7 tentativas.\n")

    while tentativas < 7:

        try:
            chute = int(input("Digite seu palpite: "))

            if chute < 1 or chute > 100:
                print("Digite um número entre 1 e 100.\n")
                continue

            tentativas += 1
            historico += (chute,)

            if chute == numero:
                print("\nParabéns! Você acertou!")
                print(f"Número sorteado: {numero}")
                print(f"Tentativas utilizadas: {tentativas}")
                print(f"Histórico de tentativas: {historico}")
                break

            elif chute > numero:
                print("Muito alto!")

            else:
                print("Muito baixo!")

            print(f"Tentativas restantes: {7 - tentativas}\n")

        except ValueError:
            print("Entrada inválida! Digite apenas números.\n")

    else:
        print("\nVocê perdeu!")
        print(f"O número correto era: {numero}")
        print(f"Histórico de tentativas: {historico}")

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()

    if jogar_novamente != "s":
        print("Obrigado por jogar!")
        break