"""
Pedro Henrique Jaber Cavalcante
22107003
4/11/2021
"""


class Conta:

    qtd_contas = 0

    def __init__(self,nome,saldo):
        self.nome = nome
        self.saldo = float(saldo)
        Conta.qtd_contas += 1

    def __str__(self):
        return f"Conta\n" \
               f"Nome: {self.nome}\n" \
               f"Slado {self.saldo:.2f}\n"

    @classmethod
    def get_qtd_contas(cls):
        return Conta.qtd_contas

    @staticmethod
    def top_foda():
        print("!TOP!")

    def get_nome(self):
        return self.nome

    def set_nome(self,nome_n):
        if type(nome_n) == str:
            self.nome = nome_n
        else:
            print("[Coloque um Nome Valido]")

    def get_saldo(self):
        return self.saldo

    def deposito(self,valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("[Valor Invalido]")

    def saque(self,valor):
        if valor > 0:
            if self.__class__ == ContaPF and self.get_saldo() >= valor + 2:
                self.saldo -= 2
            elif self.__class__ == ContaPJ and self.get_saldo() >= valor + 5:
                self.saldo -= 5

            self.saldo -= valor
        else:
            print("[Valor Invalido]")


class ContaPF(Conta):

    def __init__(self,nome,saldo,genero,cpf):
        super().__init__(nome,saldo)
        self.genero = genero
        self.cpf = cpf

    def get_genero(self):
        return self.genero

    def set_genero(self,genero_n):
        if type(genero_n) == str:
            self.genero = genero_n
        else:
            print("Genero Invalido")

    def get_cpf(self):
        return self.cpf

    def set_cpf(self,cpf_n):
        self.cpf = cpf_n


class ContaPJ(Conta):

    def __init__(self,nome,saldo,tipo_org,cnpj):
        super().__init__(nome,saldo)
        self.tipo_org = tipo_org
        self.cnpj = cnpj

    def get_tipo_org(self):
        return self.tipo_org

    def set_tipo_org(self,tipo_org_n):
        self.tipo_org = tipo_org_n

    def get_cnpj(self):
        return self.cnpj

    def set_cnpj(self,cnpj_n):
        self.cnpj = cnpj_n


if __name__ == '__main__':
    conta1 = Conta("Carlos", 1200)
    conta2 = ContaPF("Clara", 1500, "F", "123.123.123-12")
    conta3 = ContaPJ("Beto", 10000,"MEI","Sla")

    print(Conta.qtd_contas)

    print(conta1)
    print(conta2)
    print(conta3)

    #print(vars(conta1))
    #print(conta1.__dict__)

    conta2.deposito(100)


    print(conta2)

    conta2.saque(10)

    print(conta2)

