




tAlunos = int(input("Quantos alunos: "))
soma = ct = 0

for alu in list(1, tAlunos + 1):
    nota = float(input("Digite a nota do aluno: "))
    soma += nota
    ct += 1

print(f"\nMedia: {(soma/ct):.2f}")
