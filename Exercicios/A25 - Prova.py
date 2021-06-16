
#Pedro Henrique Jaber Cavalcante


"""
1. Projete o programa que faça manutenção em uma conta bancária de um correntista. O correntista
fornecerá o número da conta, o saldo atual, o tipo da operação a ser realizada (depósito ou retirada) e o valor da
operação. Gere a tela de saída com os seguintes dados deste correntista: o número da conta bancária e o novo saldo
após a operação. Faça críticas.             """


"""
saldoC = 0.00

conta = int(input("Digite o numero da conta:"))
saldoC = float(input("Qual é o saldo da conta: "))
while True:
    op = input("\nDigite: " 
               "\nDeposito [d]" 
               "\nretirada [r]"
               "\nDigite [-1] para sair"
               "\n: ")

    if op == "d":
        print("Digite o valor a ser Depositado")
        valorD = float(input(": "))
        print("Transação aprovada")
        saldoC += valorD

    elif op == "r":
        while True:
            print(f"Digite o valor a ser Retirada (menor que 2000)")
            valorR = float(input(": "))
            if valorR > 2000.00:
                print("Valor Invalidao")
            elif valorR <= saldoC:
                print("Transação aprovada")
                saldoC -= valorR
                break

    elif op == "-1":
        break
    else:
        print("Erro1")

    print(f"Conta: {conta}")
    print(f"Saldo Atual: {saldoC}")
"""



"""
2. Desenvolva o programa que calcule a média aritmética de uma turma, onde cada aluno realizou uma
avaliação. Mas, não sabemos a quantidade de alunos da turma. Na tela de saída, mostre também a quantidade de
alunos da turma e a menor nota da turma. Sempre que tivermos uma divisão, temos que verificar se o divisor é
diferente de zero.              """

"""
alunosT = 0
notaT = 0
notam = 99999

print("Digite (-1) para sair")
while True:
    nota = float(input("Digite a nota do aluno: "))
    if nota == -1:
        print("Fim da contagem")
        break
    if notam > nota:
        notam = nota
    alunosT += 1
    notaT += nota

if alunosT == 0:
    print("Não é possivel dividir por zero")
else:
    media = notaT / alunosT
    if alunosT == 1: print(f"A média da turma de {alunosT} aluno é {media:.2f}")
    elif alunosT > 1:
        print(f"A média da turma de {alunosT} alunos é {media:.2f}")
        print(f"A menor nota foi {notam}")
    else: print("erro")
"""




"""
3. Elabore o programa que recebe a idade e o peso de várias pessoas. Analise e processe esses dados com o
objetivo de gerar o seguinte relatório estatístico de saída: a quantidade de pessoas analisadas, a soma de peso das
pessoas e a idade da pessoa mais velha.             """

"""
idadeV = 0
pesoT = 0
ct = 0
print("Digite idade [-1] para sair")
while True:
    idade = int(input("Digite sua idade: "))
    if idade == -1:
        print("fim da contagem")
        break

    peso = float(input("Dgite seu peso:"))

    if idade >= -1:
        ct += 1
        pesoT += peso
        if idade > idadeV:
            idadeV = idade

print(f"O peso total {pesoT}")
print(f"A pessas mais velha é {idadeV}")
print(f"A quantidade foi {ct}")
"""


































































