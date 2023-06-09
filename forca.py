import random


def jogar():

    text_open_game()
    palavra_secreta = load_secret_word()
    letras_acertadas = start_words_rights(palavra_secreta)

    # for letra in palavra_secreta:
    #     letras_acertadas.append("_")

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = not "_" in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do Jogo")


# ********* Texto Abertura *********
def text_open_game():
    print("******************************")
    print("Bem vindo ao jogo da Forca!")
    print("******************************")

# ********* Função Carregar Palavra Secreta *********
def load_secret_word():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

# ********* Função Inicializar Palavra Secreta *********
def start_words_rights(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()
