#
#
#
#
#
#
class Conta:

    def __init__(self, numero, senha, titular, saldo = 0.0, limite = -1000.0, ):
        saldo  = float(saldo)
        limite = float(limite)
        self.__nconta  = numero
        self.__titular = titular
        self.__saldo   = saldo
        self.__limite  = limite
        self.__senha   = senha

    def __str__(self):
        return f"@{self.__nconta}({self.__senha})'{self.__titular}'S{self.__saldo})L{self.__limite}*)"

    def formatar(self):
        return f"@{self.__nconta}({self.__senha})'{self.__titular}'${self.__saldo})#{self.__limite}*)"

    def extato(self):
        print(f"Titular: {self.__titular} \n"
              f"Conta:   {self.__nconta:05d} \n"
              f"Saldo:   {self.__saldo:.2f} \n"
              f"Limite:  {self.__limite:.2f}")

    def depositar(self, valor):
        valorf = float(valor)
        while True:
            if valorf > 5000:
                print("Deposito maior do que o permitido")
                break
            elif 0 < valorf <= 5000:
                self.__saldo += valorf
                print("Operação concluida")
                break
            elif valorf <= 0:
                print("Tente fazer um saque")
                break

    def __saque_permitido(self, valor):
        # print(self.__saldo)
        # print(self.__limite)
        saque_disponivel = self.__saldo + (self.__limite*-1)
        # print(saque_disponivel)
        # print(valor)
        return valor <= saque_disponivel

    def sacar(self, valor):
        valor = float(valor)
        while True:
            if valor > 5000:
                print("Saque maior do que o permitido")
                saque = 'não ok'
                return saque
                break
            elif (self.__saque_permitido(valor)):
                self.__saldo -= valor
                print("Operação concluida")
                saque = 'ok'
                return saque
                break
            elif (self.__saque_permitido(valor) == False):
                print("Você não possui limite para essa operação")
                saque = 'não ok'
                return saque
                break
            elif valor <= 0:
                print("Tente fazer um deposito")
                saque = 'não ok'
                return saque
                break

    def transferencia(self,valor,destino):
        saque = self.sacar(valor)
        if saque == 'ok':
            destino.depositar(valor)
            print("Operação concluida")

    @property
    def conta(self):
        return self.__nconta

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        limite = self.__limite
        return limite

    @limite.setter
    def limite(self, novo_limite):
        novo_limite = abs(novo_limite)
        novo_limite *= -1
        self.__limite = novo_limite

    @staticmethod           #idependente de Objs
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos():
        codigos = {'BB':'001', 'Caixa': '104', 'Bradesco':'237'}
        return codigos









