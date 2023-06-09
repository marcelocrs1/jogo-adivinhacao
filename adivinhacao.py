print("******************************")
print("Bem vindo ao jogo Adivinhação!")
print("******************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print("Você digitou ", chute)

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto!")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto!")



print("Fim de jogo")

# ********** Usando o Loop While inves do for **********

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
