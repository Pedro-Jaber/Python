





# alunosT = 0
# notaT = 0
# print("Digite (-1) para sair")
# while True:
#     nota = float(input("Digite a nota do aluno: "))
#     if nota == -1:
#         print("Fim da contagem")
#         break
#     alunosT += 1
#     notaT += nota
# if alunosT == 0:
#     print("Não é possivel dividir por zero")
# else:
#     media = notaT / alunosT
#     if alunosT == 1: print(f"A média da turma de {alunosT} aluno é {media:.2f}")
#     elif alunosT > 1: print(f"A média da turma de {alunosT} alunos é {media:.2f}")
#     else: print("erro")

# listaNota = []
#
# print("Digite [-1] para sair")
# while True:
#     nota = float(input("Digite a nota: "))
#     if nota == -1:
#         print("Fim da soma")
#         break
#     elif 0 <= nota <= 10:
#         listaNota.append(nota)
#     else: print("Digite novamente")
#
# print(f"Numero de alunos: {len(listaNota)}")
# print(f"Media da turma: {(sum(listaNota)/len(listaNota)):.2f}")
# print("\nNotas: ")
# for nota in listaNota: print(nota)
import random

random.seed(20)
listaNota = []
ct = 0

print("Digite [-1] para sair")
while ct <= 20:
    nota = random.randint(1,10) #float(input("Digite a nota: "))
    if nota == -1:
        print("Fim da soma")
        break
    elif 0 <= nota <= 10:
        listaNota.append(nota)
    else: print("Digite novamente")
    ct += 1


print(f"Numero de alunos: {len(listaNota)}")
print(f"Media da turma: {(sum(listaNota)/len(listaNota)):.2f}")
print("\nNotas: ")
for nota in listaNota: print(nota)
