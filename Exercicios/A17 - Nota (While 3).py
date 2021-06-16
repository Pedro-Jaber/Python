





alunosT = 0
notaT = 0
print("Digite (-1) para sair")
while True:
    nota = float(input("Digite a nota do aluno: "))
    if nota == -1:
        print("Fim da contagem")
        break
    alunosT += 1
    notaT += nota
if alunosT == 0:
    print("Não é possivel dividir por zero")
else:
    media = notaT / alunosT
    if alunosT == 1: print(f"A média da turma de {alunosT} aluno é {media:.2f}")
    elif alunosT > 1: print(f"A média da turma de {alunosT} alunos é {media:.2f}")
    else: print("erro")
