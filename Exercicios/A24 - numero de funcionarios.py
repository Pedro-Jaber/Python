







cnpjMaior = ""
funciMaior = -1
cnpjMenor = ""
funciMenor = 99999999

ct = 0

print("digite [s] para sair")
while True:
    cnpj = input("Digite o CNPJ:")
    if cnpj == "s":
        break
    ct += 1
    funci = int(input("Digite a quantidade de funcionario:"))
    if funci > funciMaior:
        cnpjMaior = cnpj
        funciMaior = funci
    elif funci < funciMenor:
        cnpjMenor = cnpj
        funciMenor = funci
if ct > 1:
    print(f"\n     Maior empresa     "
      f"\n_______________________\n"
      f"Empresa: {cnpjMaior} "
      f"\nFuncionarios: {funciMaior} "
      f"\n_______________________")

    print(f"\n\n     Menor empresa     "
      f"\n_______________________\n"
      f"Empresa: {cnpjMenor} "
      f"\nFuncionarios: {funciMenor} "
      f"\n_______________________")

    print(f"\n[Total de emepresas: {ct}]")
elif ct <= 1:
    print("quantidade insuficiente")
else: print("Erro1")