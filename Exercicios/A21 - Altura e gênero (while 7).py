




'''
alturaM = 3
alturam = 0
ctM = 0
ctF = 0
soma = 0

print("Ditie ( 0 ) para sair")
while True:
    altura = float(input("Digite sua altura: "))
    if altura == 0:
        break
    soma += altura
    genero = input("Para Homem Digite M \nPara Mulher Digite F\nGenero:")
    if genero == "m":
        ctM += 1
    elif genero == "f":
        ctF += 1
    else: print("genero invalido")

    if altura > alturam:
        alturam = altura
    elif altura < alturaM:
        alturaM = altura

media = soma/(ctM + ctF)
print(f"maior altura: {alturaM}")
print(f"menor altura: {alturam}")
print(f"foram {ctM} homens e {ctF} mulheres")
print(f"a média é: {media:.2f}")
'''


alturamM = 0
alturamm = 3
alturafM = 0
alturafm = 3
ctM = 0
ctF = 0
soma = 0

print("Ditie ( 0 ) para sair")
while True:

    genero = input("\nPara Homem Digite M \nPara Mulher Digite F\n\nGenero:")
    if genero == "b":
        break
    elif genero == "m":
        ctM += 1
        alturam = float(input("Digite sua altura: "))
        soma += alturam

        if alturam < alturamm:
            alturamm = alturam
        if alturam > alturamM:
            alturamM = alturam

    elif genero == "f":
        ctF += 1
        alturaf = float(input("Digite sua altura: "))
        soma += alturaf

        if alturaf < alturafm:
            alturafm = alturaf
        if alturaf > alturafM:
            alturafM = alturaf

    else: print("genero invalido")



media = soma/(ctM + ctF)
print(f"\nmaior altura Masc.: {alturamM}")
print(f"menor altura Masc.: {alturamm}")
print(f"\nmaior altura Femi.: {alturafM}")
print(f"menor altura Femi.: {alturafm}")
print(f"\nforam {ctM} homens e {ctF} mulheres")
print(f"a média é: {media:.2f}")
























