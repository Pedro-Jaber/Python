#
#
#
#
#
#
notas = []

qnt = int(input("Quantidade: "))

for i in range (1,qnt+1):
    nota = float(input("notas: "))
    notas.append(nota)


print(f"media: {sum(notas)/len(notas)}")
print("")