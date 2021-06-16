





def potencia(base, expo):
    c = 1
    if expo >= 0:
        for i in range(1, expo+1):
            c *= base
        return c
    elif expo < 0:
        expo *= -1
        for i in range(1, expo+1):
            c *= 1/base
        return c


if __name__ == '__main__':
    base = int(input("Base: "))
    expo = int(input("Expoente: "))
    print(potencia(base,expo))


