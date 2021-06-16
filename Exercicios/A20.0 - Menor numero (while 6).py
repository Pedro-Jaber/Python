



numeroMenor = 9999999
numeroMaior = -9999999
ct = 0
soma = 0

print("Ditie ( -1 ) para sair")
while True:
    valor = int(input("Digite o numero:"))
    if valor == -1:
        break
    ct += 1
    soma += valor
    if valor < numeroMenor:
        numeroMenor = valor
    elif valor > numeroMaior:
        numeroMaior = valor

media = soma/ct
if ct > 0:
    print(f"\nO menor valor é: {numeroMenor}")
    print(f"O maior valor é: {numeroMaior}")
    print(f"Foram digitados {ct} numeros ")
    print(f"Soma total = {soma}")
    print(f"A media dos numeros digitados é {media}")
elif ct == 0:
    print("Não foi digitado nenhum valor")