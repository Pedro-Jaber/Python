





if __name__ == '__main__':

    #Sem Lista
    """
    maior = 0
    menor = 9
    ctt_f = 0
    ctt_m = 0
    print("Digite [0] para sair")
    while True:
        altura = float(input("Altura: "))
        if altura == 0:
            break

        sexo   = input("Genero [M][F]: ")
        sexo = sexo.upper()

        if   sexo == 'M':
            ctt_m += 1
        elif sexo == 'F':
            ctt_f += 1
        else: print("Opção Invalida")

        if altura > maior:
            maior = altura
        elif altura < menor:
            menor = altura

    print(f"Maior Altura: {maior}\n"
          f"Menor Altura: {menor}\n"
          f"Mulheres:     {ctt_f}\n"
          f"Homens:       {ctt_m}")
    """


    #Com lista

    alturas = []
    generos = []

    print("Digite [0] para sair")
    while True:
        altura = float(input("Altura: "))
        if altura == 0:
            break
        else:
            alturas.append(altura)

        genero = input("Genero [M][F]: ")
        genero = genero.upper()

        if genero == 'M' or genero == 'F':
            generos.append(genero)
        else: print("Opção Invalida")

    print(f"Maior Altura: {max(alturas)}\n"
          f"Menor Altura: {min(alturas)}\n"
          f"Mulheres:     {generos.count('F')}\n"
          f"Homens:       {generos.count('M')}")


















