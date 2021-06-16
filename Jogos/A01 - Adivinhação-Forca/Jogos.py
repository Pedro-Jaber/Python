import adivinhacao
import forca




def escolher_jogo():
                                                #Escolhendo jogo
    print("\n"
        "----------------\n"
        "Escolha seu jogo\n"
        "----------------\n")

    print("[1] Adivinhação\n"
        "[2] Forca")

    jogo = int(input(": "))

                                                #Executando jogo

    if(jogo == 1):
        print("Carregando jogo da Adivinhação")
        print("\n")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Carregando jogo da Forca")
        print("\n")
        forca.jogar()


if __name__ == '__main__':
    escolher_jogo()