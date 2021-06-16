






def abso(a):

    """
    if a < 0:
        b = a * -1  #ou b = -a
    else:
        b = a
    return b
    """

    if a < 0:
        a = -a
    return a


if __name__ == '__main__':
    valor1 = float(input("Digite o valor: "))
    print(f"O valor absoluto de {valor1} é {abso(valor1)}")
