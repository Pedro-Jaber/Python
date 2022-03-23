





list = []

print("Digite [0] para sair")

while True:
    num = int(input("Digite um numero: "))
    if num == 0:
        break
    list.append(num)

print(list)
list.sort()
print(f"lista na ordem Crescente: {list}")
list.sort(reverse=True)
print(f"lista na ordem Decrescente: {list}")
print("Quantidade: ", len(list))
print(f"Soma dos valores: {sum(list)}")
print(f"Media do valores: {sum(list)/len(list)}")
print(f"Maior valor: {max(list)}")
print(f"Menor valor: {min(list)}")

##############################
ctt = 0
for num in list:
    if num > 10:
        ctt+=1

porc = (ctt * 100) / len(list)

print(f"A porcentagem de numeros > 10: {porc:.1f}%")
##############################

pesquisar = int(input("Pesquisar valor: "))

if pesquisar in list:
    print(f"O valor {pesquisar} esta na lista, sua primeira aparição ocorre no index {list.index(pesquisar)}")
else:
    print(f"Valor não encontrado")

