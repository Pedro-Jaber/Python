import random





# menorValor = 999999999
valores = []
print("Digite [0] para sair")
while True: #len(valores) < 100:
    valor = random.randint(0,100)   #int(input("Digite o valor: "))
    print(f"{valor:3d}")
    if valor == 0:
        break
    valores.append(valor)


# for num in valores: print(f"{num:3d}")

# print( "---------------------")
# print(f"Maior valor:      {max(valores):3d}")
# print(f"Menor valor:      {min(valores):3d}")
# print(f"total de numeros: {len(valores):3d}" )
# print( "---------------------")


print( "*********************")
print( "---------------------")
print( "*********************")

if len(valores) >= 1:
    valores.sort()
    for num in valores: print(f"{num:3d}")
    menor = valores[0]     #Primeiro valor
    maior = valores[-1]    #Ultimo valor
    media = sum(valores)/len(valores)

    print( "-----------------------")
    print(f"Maior valor:      {maior:5d}")
    print(f"Menor valor:      {menor:5d}")
    print(f"Total de numeros: {len(valores):5d}")
    print(f"Soma dos valores: {sum(valores):5d}")
    print(f"Media valor:      {media:3.2f}")
    print( "-----------------------")

elif len(valores) == 0:
    print("Não foi digitado nenhum valor")