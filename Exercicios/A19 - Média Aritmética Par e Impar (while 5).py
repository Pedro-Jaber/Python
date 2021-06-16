





somaP = 0
ctP = 0

somaI = 0
ctI = 0

ctT = 0


print("Ditie ( -1 ) para sair")
while True:
    valor = int(input("Digite o numero: "))
    if valor == -1 :
        break
    resto = valor % 2
    if resto == 0:
        somaP += valor
        ctP += 1
    elif resto != 0:
        somaI += valor
        ctI += 1

    ctT += 1

print("\nPar:")
if ctP == 0:
    print("Não tem numero Par")
else:
    mediaP = somaP / ctP
    if ctP == 1: print(f"A média de {ctP} numero Par é: {mediaP:.4f}")
    elif ctP > 1:
        print(f"A média de {ctP} numeros Pares é: {mediaP:.4f}")
        print(f"a soma desses numeros é {somaP}")

print("\nImpar:")
if ctI == 0:
    print("Não tem numero Par")
else:
    mediaI = somaI / ctI
    if ctI == 1:
        print(f"A média de {ctI} numero Impar é: {mediaI:.4f}")
    elif ctI > 1:
        print(f"A média de {ctI} numeros Impares é: {mediaI:.4f}")
        print(f"a soma desses numeros é {somaI}")

print(f"\nA quantidade de numero digitados foi: {ctT}")