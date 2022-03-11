from conta import Conta


"""
==========================================
Funções de gerenciamento de banco de dados
==========================================
"""


def gera_numero_conta():
    with open("contas.txt", 'r') as arquivo:
        linhas = arquivo.readlines()
        ultima_conta = linhas[-1]
        numero_conta = int(ultima_conta[1:6])
        numero_conta += 2
        return numero_conta


def verificar_conta(contaBD):
    with open("contas.txt", 'r') as arquivo:
        for linha in arquivo:
            if contaBD in linha:
                return linha

        return '0'


def conta_registrar(conta):
    with open("contas.txt", 'a+') as arquivo:
        arquivo.write(f"{conta.formatar()}\n")


def encontrar_conta(str_numero_conta):
    ct = 0
    with open("contas.txt", 'r') as arquivo:
        for linha in arquivo:
            ct+=1
            if str_numero_conta in linha:
                return ct


def sobrescrever_conta(ct_conta,conta):
    with open("contas.txt", 'r') as arquivo_leitura:
        lista_conta = arquivo_leitura.readlines()
    ct_conta-=1
    lista_conta[ct_conta] = conta
    with open("contas.txt", 'w') as arquivo_escrita:
         for linha in lista_conta:
             arquivo_escrita.write(linha)


def salvar_conta(conta):
    #@conta(senha )'Titular'Ssaldo)Llimite)
    conta = conta.formatar()
    conta += "\n"
    inicio = conta.index("@")
    fim = conta.index(")")
    str_numero_conta = conta[inicio: fim]

    ct_conta = encontrar_conta(str_numero_conta)
    sobrescrever_conta(ct_conta,conta)
