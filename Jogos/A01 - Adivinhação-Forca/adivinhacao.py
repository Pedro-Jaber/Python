import random





def jogar():
    print("\n"
          "--------------------------------\n"
          "Bem vindo ao jogo de Adivinhação\n"
          "--------------------------------\n")

                                                #variaveis indempendentes

    numero_secreto = random.randint(1,100)
    pontuacao = 10000
    n_acertou = True

                                                #Dificuldade

    print("Escolha a Dificuldade")
    print("Difícil  [3]\n"
          "Médio    [2]\n"
          "Fácil    [1]\n")
    DIFICULDADE = int(input(": "))

    facil   = DIFICULDADE == 1
    medio   = DIFICULDADE == 2
    dificil = DIFICULDADE == 3
    dev     = DIFICULDADE == 99

    if facil:
        tentativas = 20
    elif medio:
        tentativas = 10
    elif dificil:
        tentativas = 5
    elif dev:
        tentativas = 20
        print(f"Numero Secreto [{numero_secreto}]")
    else: print("Erro 1")

                                                #Game loop


    print("Digite um numero entre 1 e 100!")
    #print(numero_secreto)

    for rodada in range(1,tentativas + 1) :                                    #{
        print(f"\nTentativa {rodada} de {tentativas}")
        chute = int(input("Digite o seu numero: "))
        #print("Seu chute foi", chute)

        acertou = chute == numero_secreto
        errou = chute != numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        errado = chute < 1 or chute > 100


        if errado:
            print("Digite um numero entre 1 e 100!")
            continue
        elif acertou:
            # numero_secreto += 1
            # print("[", chute, "é menor que o numero secreto]")
            print("[!Acertou!]")
            n_acertou = False
            break
        elif errou:
            pontos_perdidos = abs(numero_secreto - chute)
            pontuacao -= pontos_perdidos

            if maior:
                print("[", chute, "é maior que o numero secreto]")
            elif menor:
                print("[", chute, "é menor que o numero secreto]")



        else: print("Erro 2")
                                                                #}

                                                #fim de jogo

    print("\n")

    if n_acertou == True:
        print(f"[Você tentou d+] [Numero secreto era {numero_secreto}]\n")

    print("----Fim de jogo----\n"
         f"Pontuação:    {pontuacao:05d} \n"
          "-------------------")

if __name__ == '__main__':
   jogar()