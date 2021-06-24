from os import system

from conta import Conta
import fun_gerir_banco_dados


"""
================================
Funções de gerenciamento da main
================================
"""


def bem_vindo():
    print("=================================\n"
          "    Bem vindo ao Banco Python    \n"
          "=================================\n"
          "[1] - Entrar na conta\n"
          "[2] - Criar uma conta\n"
          "Oque deseja fazer --->", end ="")
    evento = input("")
    print("")
    return evento.lower().strip()


def criando_validando_senha():
      while True:
            print("A senha deve ter 6 caracteres")
            senha1 = input("Digite uma senha: ")
            senha2 = input("Digite a senha novamente: ")
            iguais = (senha1 == senha2)
            menor = (len(senha1) < 6)
            maior = (len(senha1) > 6)
            ideal = (iguais and len(senha1) == 6)
            if menor:
                  print("\nSenha Curta, Digite novamente")
                  pass
            elif maior:
                  print("\nSenha é muito grande, Digite novamente")
                  pass
            elif not iguais:
                  print("\nSenhas Diferentes, Digite novamente")
                  pass
            elif ideal: return senha1


def tratar_nome(primero_nome, sobrenome):
      nome1 = primero_nome.strip()
      nome2 = sobrenome.strip()
      nome = nome1 + " " + nome2
      nome = nome.lower().title()
      return nome


def criar_conta():
      print("=================================\n"
            "        Criando na Conta         \n"
            "=================================")
      primero_nome = input("Digite seu primeiro nome: ")
      sobrenome = input("Digite seu sobrenome: ")
      nome_completo = tratar_nome(primero_nome, sobrenome)
      senha = criando_validando_senha()
      numero_conta = fun_gerir_banco_dados.gera_numero_conta()
      print(f"O numero da sua conta é {numero_conta}")

      conta = Conta(numero_conta,senha,nome_completo)
      fun_gerir_banco_dados.conta_registrar(conta)


def entrar_conta():
      status = True
      print("=================================\n"
            "        Entrando na Conta        \n"
            "=================================")
      while status:
            conta = input("Conta: ")
            senha = input("Senha: ")
            contaBD = f"@{conta}({senha}"
            verificar = fun_gerir_banco_dados.verificar_conta(contaBD)
            if verificar == '0': print("conta não encontrada, tente novamente")
            else:
                  status = main_conta(verificar)
                  return status


def extrair_numero(conta):
      #@10056(123456)'Pedro Jaber'$0.0)#-1000.0)
      inicio = conta.index("@") + 1
      fim = conta.index("(")
      numero = conta[inicio: fim]
      return int(numero)


def extrair_senha(conta):
      #@10056(123456)'Nome'$0.0)#-1000.0*)
      inicio = conta.index("(") + 1
      fim = conta.index(")")
      senha = conta[inicio: fim]
      return senha


def extrair_titular(conta):
      #@10056(123456)'Nome'$0.0)#-1000.0*)
      inicio = conta.index("'") + 1
      fim = conta.index("$") - 1
      titular = conta[inicio: fim]
      return titular


def extrair_saldo(conta):
      #@10056(123456)'Nome'$0.0)#-1000.0*)
      inicio = conta.index("$") + 1
      fim = conta.index("#") - 1
      saldo = conta[inicio: fim]
      return float(saldo)


def extrair_limite(conta):
            #@10056(123456)'Nome'$0.0)#'-1000'.0*)
      inicio = conta.index("#") + 1
      fim = conta.index("*")
      limite = conta[inicio: fim]
      limite = float(limite)
      return limite


def pri_nome(titular):
      #Nome Sobrenome
      fim = titular.index(" ")
      Pnome = titular[: fim]
      return Pnome


def transferir(valor,destino,conta_remetente):
      destino = f"@{destino}("
      verificar = fun_gerir_banco_dados.verificar_conta(destino)
      if verificar == '0':
            print("conta não encontrada, tente novamente")
            pass
      else:
            numero = extrair_numero(verificar)
            senha = extrair_senha(verificar)
            titular = extrair_titular(verificar)
            saldo = extrair_saldo(verificar)
            limite = extrair_limite(verificar)
            conta_destinatario = Conta(numero, senha, titular, saldo, limite)
            conta_remetente.transferencia(valor, conta_destinatario)
            fun_gerir_banco_dados.salvar_conta(conta_destinatario)


def main_conta(conta):
      numero = extrair_numero(conta)
      senha = extrair_senha(conta)
      titular = extrair_titular(conta)
      saldo = extrair_saldo(conta)
      limite = extrair_limite(conta)

      primeiro_nome = pri_nome(titular)

      conta = Conta(numero,senha,titular,saldo,limite)
      print("")

      while True:
            print("================================\n"
                 f"       Bem vindo {primeiro_nome}\n"
                  "================================\n"
                  "[1] - Sacar\n"
                  "[2] - Depositar\n"
                  "[3] - Transferir\n"
                  "[4] - Extrato\n"
                  "Digite 'parar' para sair\n")
            evento =  input("Oque deseja fazer ---> ")
            evento = evento.lower().strip()
            if evento == "1":
                  valor = float(input("Quanto deseja sacar: "))
                  conta.sacar(valor)
                  print("\n")
            elif evento == "2":
                  valor = float(input("Quanto deseja depositar: "))
                  conta.depositar(valor)
                  print("\n")
            elif evento == "3":
                  valor = float(input("Quanto deseja Tranferir: "))
                  destino = input("Qual o numero da conta do destinatario: ")
                  transferir(valor,destino,conta)
                  print("\n")
            elif evento == "4":
                  print("\n")
                  conta.extato()
            elif evento == "parar":
                  fun_gerir_banco_dados.salvar_conta(conta)
                  status = False
                  return status
            else:
                  print("\n")
                  print("Tente novamente")


















