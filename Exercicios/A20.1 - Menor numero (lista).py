





lista =[]

print("Ditie ( 0 ) para sair")
while True:
    valor = int(input("Digite o numero:"))
    if valor == 0:
         break
    if valor < numeroMenor:
         numeroMenor = valor
    elif numeroMaior > valor:
         numeroMaior = valor

print(f"O menor valor é: {numeroMenor}")
print(f"O maior valor é: {numeroMaior}")