from data import Data
#
#
#
#
#

"""
def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta
"""
"""
def depositar(conta, valor):
    valorf = float(valor)
    status = ""
    if valorf > 5000:
        status = "Deposito maior do que o permitido"
    elif 0 < valorf <= 5000:
        status = "Operação concluida"
        conta["saldo"] += valorf
    elif valorf <= 0:
        status = "Tente fazer um saque"

    return status
"""
"""
def sacar(conta, valor):
    valor = float(valor)
    status = ""
    if valor > 5000:
        status = "Saque maior do que o permitido"
    elif 0 <= valor <= 5000:
        status = "Operação concluida"
        conta["saldo"] -= valor
    elif valor <= 0:
        status = "Tente fazer um deposito"

    return status
"""
"""
def extrato(conta):
    print(f"Saldo é {conta['saldo']}")
"""


dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = input("Ano: ")

data = Data(dia, mes, ano)
print(f"{data.formadata()}")
