





ct = 0
soma = 0



ini = int(input("valor inicial: "))
fim = int(input("valor final: "))

if ini == fim:
    print("valores iguais")

elif ini < fim:
    for i in range(ini, fim + 1):
        print(i)
        ct += 1
        soma += i

elif ini > fim:
    for i in range(ini, fim - 1, -1):
        print(i)
        ct += 1
        soma += i


print("soma: ",soma)
print("cont: ",ct)
print("media", soma/ct)