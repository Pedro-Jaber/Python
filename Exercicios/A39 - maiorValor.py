#
#
#
#
#
#
#
def maior_valor (a, b):
    if a == b:
        return a
    elif a > b:
        return a
    elif a < b:
        return b


def lerval ():
    valor = int(input("Digite o valor:"))
    return valor


if __name__ == '__main__':
    valor1 = lerval()  #int(input("digite: "))
    valor2 = lerval()  #int(input("digite: "))
    print(f"O maior valor é {maior_valor(valor1,valor2)}")