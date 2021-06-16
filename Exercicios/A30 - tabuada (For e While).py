






while True:
    print("\nDigite [0] para sair")
    num = int(input("escolha o numero para a tabuada: "))
    if num == 0: break

    tab = input("soma [+] ou multiplicação [x]")

    for mult in range(1,11,1):
        if tab == "x":
            print(f"{mult} x {num} = {mult*num}")
        if tab == "+":
            print(f"{mult} + {num} = {mult+num}")