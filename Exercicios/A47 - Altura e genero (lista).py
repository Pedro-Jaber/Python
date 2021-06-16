#
#
#
#
#
#
alturas = []
generos  = []
print("Digite [0] para sair")
while True:
    genero = input("Genero: [M] [F]: ")
    if genero == "0": break
    else:
        generos.append(genero.upper())
    altura = float(input("Digite sua altura: "))
    if 0 < altura < 3:
        alturas.append(altura)
    elif altura < 0 or altura > 3:
        print("Digite novamente")


print(f"Menor Pessoa: {min(alturas)}")
print(f"Maior Pessoa: {max(alturas)}")
print(f"Numero de Homens   : {generos.count('M')}   [{generos.count('M')*100/len(generos)}%]")
print(f"Numero de Mulheres : {generos.count('F')}   [{generos.count('F')*100/len(generos)}%]")
print(f"Media das Alturas: {sum(alturas)/len(alturas)}")