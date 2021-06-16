import random
#
#
#


def jogar():

    bem_vindo()

    """Gerar Palavra Secreta"""

    palavra_secreta = gerar_palavra_se()
    letras_ocultas = letras_ocultar(palavra_secreta)
    letras_erradas = []

    """Game loop"""

    print(letras_ocultas, f"São [{len(letras_ocultas)}] Letras")

    enforcado = False
    acertou = False
    erros = 0

    while not enforcado and not acertou:
        print("\n\n")
        desenha_forca(erros)
        infor(letras_ocultas, erros, letras_erradas)
        chute = chutando()

        if chute in palavra_secreta:
            chute_certo(palavra_secreta,chute,letras_ocultas)
        elif chute not in palavra_secreta:
            erros +=1
            letras_erradas.append(chute)

        enforcado = erros == 6
        acertou = "_" not in letras_ocultas

    """fim de jogo"""

    print("\n")

    if enforcado:
        desenha_forca(erros)
        print(f"[{palavra_secreta}]")
        print("----Fim de jogo-----\n"
             f"[Você foi Enforcado]\n"
              "--------------------")
    elif not enforcado:
        print ("----Fim de jogo----\n"
              f"       top         \n"
               "-------------------")


def bem_vindo():
    print("\n"
          "--------------------------\n"
          "Bem vindo ao jogo de Forca\n"
          "--------------------------\n")


def gerar_palavra_se():
    palavras = []
    # arquivo = open("palavras.txt", "r")

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.upper().strip())
    # arquivo.close()

    indexP = random.randint(0, len(palavras) - 1)
    palavra_secreta = palavras[indexP]

    return palavra_secreta


def letras_ocultar(palavra):
    return ["_" for letras in palavra]
                    # for i in palavra_secreta:         #for i in range (0,len(palavra_secreta)):
                    #     letras_certas.append("_")     #    letras_certas += "_"
                    # print(letras_certas)


def chutando():
    chute = input("Uma letra: ")
    chute = chute.upper().strip()
    return chute


def infor(letras_ocultas, erros, letras_erradas):
    gerarletras(letras_ocultas)
    print(f"Erros [{erros}/6] {letras_erradas}")
    # print(f"Falta [{letras_certas.count('_')}] letra(s)")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      /|    ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def gerarletras(letras_ocultas):
    print("[",end="")
    for letra in letras_ocultas:
        print(letra, end="")
    print("]")


def chute_certo(palavra_secreta,chute,letras_ocultas):
    index = 0  # posição da letra
    for letra in palavra_secreta:
        if chute == letra:
            letras_ocultas[index] = letra
            #
            # motrar o numero de letras
            # print(f"Entrada letra [{(letra.upper())}] em [{index}]")
            #
        index += 1


if __name__ == '__main__':
    jogar()
