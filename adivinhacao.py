import random


def jogar():
    print("******************************")
    print("Bem vindo ao jogo Adivinhação!")
    print("******************************")

    numero_random = random.randrange(1, 101)
    numero_secreto = numero_random
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nivel: "))

    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print("Você digitou ", chute)

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto!")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_random - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo o numero secreto era:", numero_secreto)


if (__name__ == "__main__"):
    jogar()

    # ********** Usando o Loop While inves do for **********

    # rodada = 1

    # while (rodada <= total_de_tentativas):
    #     print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    #     chute_str = input("Digite o seu número: ")
    #     chute = int(chute_str)
    #
    #     acertou = chute == numero_secreto
    #     maior = chute > numero_secreto
    #     menor = chute < numero_secreto
    #
    #     print("Você digitou ", chute)
    #
    #     if (acertou):
    #         print("Você acertou!")
    #     else:
    #         if (maior):
    #             print("Você errou! O seu chute foi maior do que o número secreto!")
    #         elif (menor):
    #             print("Você errou! O seu chute foi menor do que o número secreto!")
    #
    #     rodada += 1

    # "R$ {:7.2f}".format(1.59)  Outra opão de format
