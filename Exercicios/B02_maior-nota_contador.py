





if __name__ == '__main__':

    """
    maior_nota = -1
    ctt_maior  = 0

    while True:
        nota = float(input("Nota: "))
        if nota == -1:
            break
        if nota > maior_nota:
            maior_nota = nota
            ctt_maior = 1
        elif nota == maior_nota:
            ctt_maior += 1

    print(f"Maior nota: {maior_nota}\n"
          f"Quantidade: {ctt_maior} \n")
    """

    #Com Lista

    nota_list = []

    print("Digite [-1] para sair")
    while True:
        nota = float(input("Nota: "))
        if nota == -1:
            break

        nota_list.append(nota)

    maior = max(nota_list)
    menor = min(nota_list)

    print(f"Maior nota {maior} Qtd[{nota_list.count(maior)}]\n"
          f"Menor nota {menor} Qtd[{nota_list.count(menor)}]\n")














