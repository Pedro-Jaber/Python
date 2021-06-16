











saMenor = 0
saMedia = 0
saMaior = 0
folhaP = 0

salarioM = int(input("Digite o salario minimo:"))
print("Digite [0] para finalizar")
while True:
    salario = int(input("Digite o salaraio: "))
    if salario == 0:
        print("\n[fim da conta]\n")
        break
    elif salario > salarioM:
        folhaP = folhaP + salario
        if salarioM< salario < salarioM*5:
            saMenor += 1
        elif salarioM*5 <= salario < salarioM*10:
            saMedia += 1
        elif salario >= salarioM*10:
            saMaior += 1

    elif salario < salarioM:
        print("Salario invalido")

    else: print("Erro1")
if folhaP > 0:
    print(f"A folha de pagamento é de: R$ {folhaP}")
    print(f"Salarios < {salarioM*5} : {saMenor}")
    print(f"Salarios >= {salarioM*5} e < {salarioM*10} : {saMenor}")
    print(f"Salarios >= {salarioM*10} : {saMaior}")
elif folhaP == 0:
    print("Nenhum falor digitado")
else: print("Erro2")