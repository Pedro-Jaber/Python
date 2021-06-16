#
#
#
#
#
#
def conta (a, b, s):
    if s == "+":
        return a + b
    elif s == "-":
        return a - b
    elif s == "x" or s == "X":
        return a*b
    else: print("[operação n encontrada]")


def rebvalor (a):
    if a == 1:
        valor = int(input("Digite o primeiro valor: "))
    elif a == 2:
        valor = int(input("Digite o segundo valor: "))
    elif a == 3:
        valor = int(input("Digite o terceiro valor: "))
    elif a == 4:
        valor = int(input("Digite o quarto valor: "))
    return valor


def menu():
    while True:
        op = input("Somar [+], Subtrair [-] ou Multiplicar [x]? ")
        if op == ("+" or "-" or "x"):
            break
        else: print("operação invalida")
    return op


if __name__ == '__main__':
    valor1 = rebvalor(1)
    valor2 = rebvalor(2)
    #valor3 = rebvalor(3)
    #valor4 = rebvalor(4)
    operacao = menu()
    print(f"O resultado foi: {conta(valor1,valor2,operacao)}")