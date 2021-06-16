#
#
#
#
#
#
def soma (a, b):
    calc = a + b
    return calc

    #ou


def sub (a, b):
    return a - b


def mult (a, b):
    return a*b


def recbvalor (a):
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
    valor1 = recbvalor(1)
    valor2 = recbvalor(2)
    #valor3 = rebvalor(3)
    #valor4 = rebvalor(4)
    operacao = menu()
    if operacao == "+":
        print(f"O resultado da soma é: {soma(valor1, valor2)}")  #{soma(valor1, valor2) + soma(valor3, valor4)}    {soma(soma(valor1, valor2),soma(valor3, valor4))}
    elif operacao == "-":
        print(f"O resultado da subtração é: {sub(valor1, valor2)}")
    elif operacao == "x":
        print(f"O resultado da multiplicação é: {mult(valor1, valor2)}")
    elif operacao != "+" and operacao != "-" and operacao != "x":
        print("operacão n encontrada")
    else:
        print("Erro01")