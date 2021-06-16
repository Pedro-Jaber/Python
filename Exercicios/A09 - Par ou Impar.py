
numero = int(input("Numero: "))
cal = numero % 2
if cal == 0:
    print(f"O {numero} é Par", f"Resto = {cal}")
    if numero % 5 == 0:
        print("e também é divisivel por cinto")
else:
    print(f"O {numero} é Impar", f"Resto = {cal}")
    if numero % 5 == 0:
        print("e também é divisivel por cinto")
