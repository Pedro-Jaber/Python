#
#
#
#
#
#
#
cnpj_s = []
funci_ = []

print("Digite [0] para sair")
while True:
    cnpj  = input("Digite o CNPJ: ")
    if cnpj == '':
        break
    funci = int(input("Digite o numero de funci: "))
    # funci.l

    cnpj_s.append(cnpj)
    funci_.append(funci)


maiorEmpresa = funci_.index(max(funci_))

print("---------------------- ---------")
print(f"Maior Empresa [CNPJ]:   {cnpj_s[maiorEmpresa]}")
print(f"Numero de Funcionarios: {max(funci_):7d} ")
print("-------------------------------")

print(cnpj_s)
print(funci_)