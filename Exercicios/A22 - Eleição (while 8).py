






cd1 = 0
cd2 = 0
cd3 = 0
nulo = 0
branco = 0
total = 0

while True:
    print("\n[1] - cand 1\n[2] - cand 2\n[3] - cand 3\n[5] - Nulo\n[6] - Branco")
    voto = int(input("Digite seu voto: "))
    if voto == 137:
        print("votação encerrada")
        break
    elif voto == 1:
        cd1 += 1
        total += 1
    elif voto == 2:
        cd2 += 1
        total += 1
    elif voto == 3:
        cd3 += 1
        total += 1
    elif voto == 5:
        nulo += 1
        total += 1
    elif voto == 6:
        branco += 1
        total += 1
    else: print("voto invalido\n")


print(f"\nO total de votos foi de {total} ")

#impressão dos votos
if cd1 == 0:                                      #sem votos
    print("Não há votos suficientes para o cd1")
    pcd1 = 0
else:                                             #com votos
    pcd1 = (cd1*100)/total
    print(f"Candidatos 1: {cd1} ({pcd1:.2f} %) ")

if cd2 == 0:                                      #sem votos
    print("Não há votos suficientes o cd2")
    pcd2 = 0
else:                                             #com votos
    pcd2 = (cd2*100)/total
    print(f"Candidatos 2: {cd2} ({pcd2:.2f} %)")

if cd3 == 0:                                      #sem votos
    print("Não há votos suficientes o cd3")
    pcd3 = 0
else:
    pcd3 = (cd3*100)/total                        #com votos
    print(f"Candidatos 3: {cd3} ({pcd3:.2f} %)")

if nulo == 0:                                     #sem votos
    print("Não há votos nulos")
    pnulo = 0
else:                                             #com votos
    pnulo = (nulo*100)/total
    print(f"Nulo: {nulo} ({pnulo:.2f} %)")

if branco == 0:                                   #sem votos
    print("Não há votos em branco")
    pbranco = 0
else:                                             #com votos
    pbranco = (branco*100)/total
    print(f"Branco: {branco} ({pbranco:.2f} %)")
