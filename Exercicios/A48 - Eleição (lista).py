#
#
#
#
#
#
votos = []
while True:
    print("\n")
    print("Escolha seu candidato:\n"
          "Azul     [1]\n"
          "Amarelo  [2]\n"
          "Vermelho [3]\n"
          "---\n"
          "Nulo        [5]\n"
          "Em Branco   [6]")
    voto = int(input(": "))
    if voto == 99:
        break
    elif voto == 1 or voto == 2 or voto == 3 or voto == 5 or voto == 6:
        votos.append(voto)
    else: print("Digite Novamente", end="")


if len(votos) >= 1:
    print(f"Total [{len(votos):03d}]----------------------")
    print(f"Azul      [{votos.count(1):02d}] [{votos.count(1)*100/len(votos):2.1f}]")
    print(f"Amarelo   [{votos.count(2):02d}] [{votos.count(2)*100/len(votos):2.1f}%]")
    print(f"Vermelho  [{votos.count(3):02d}] [{votos.count(3)*100/len(votos):2.1f}%]")
    print(f"Nulo      [{votos.count(5):02d}] [{votos.count(5)*100/len(votos):2.1f}%]")
    print(f"Em Branco [{votos.count(6):02d}] [{votos.count(6)*100/len(votos):2.1f}%]")
    print("----------------------")
elif len(votos) == 0:
    print("Ninguem Votou")