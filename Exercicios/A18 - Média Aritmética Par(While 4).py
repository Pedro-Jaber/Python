





soma = 0
ct = 0
ctT = 0


print("Ditie ( 0 ) para sair")
while True:
    valor = float(input("Digite o numero: "))
    ctT += 1
    if valor == 0:
        break
    resto = valor % 2
    if resto == 0:
        soma += valor
        ct += 1

if ctT == 0:
    print("Não pode se dividir por zero")
else:
    media = soma / ct
    if ctT == 1: print(f"A média de {ct} numero Par é: {media:.4f}")
    elif ctT > 1:
        print(f"A média de {ct} numeros Pares é: {media:.4f}")
        print(f"a soma desses numeros é {soma}")
    print("a quantidade de numero digitados foi ", ctT)