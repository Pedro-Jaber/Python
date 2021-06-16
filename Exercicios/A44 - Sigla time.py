





def sgl(nome):
    sigla = ''
    for letra in nome:
        if letra.isupper():
            sigla += letra
    return sigla


if __name__ == '__main__':
    nome = input("Nome do time: ")
    print(f"O time {nome} é {sgl(nome)}")