print("******************************")
print("Bem vindo ao jogo Adivinhação!")
print("******************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa", rodada, "de ", total_de_tentativas)
    chute_str = input("Digite o seu número: ")
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print("Você digitou ", chute)

    if(acertou):
      print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto!")


    rodada += 1

print("Fim de jogo")
