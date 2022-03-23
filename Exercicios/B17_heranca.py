"""
Pedro Henrique Jaber Cavalcante
22107003
21/10/2021
"""


class Funci:

    def __init__(self,nome,cpf,salario=0.0):
        self.nome    = str(nome)
        self.cpf     = str(cpf)
        self.salario = float(salario)

    def __str__(self):
        return f"Nome:    {self.get_nome()}\n" \
               f"CPF:     {self.get_cpf()}\n" \
               f"Salario: {self.get_salario()}\n"

    def get_nome(self):
        return self.nome

    def set_nome(self, nome_n):
        self.nome = nome_n

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf_n):
        self.cpf = cpf_n

    def get_salario(self):
        return self.salario

    def set_salario(self, salario_n):
        self.salario = salario_n

    def bonificacao(self):
        bonifi = self.get_salario()/10
        return bonifi

    def salario_total(self):
        return self.get_salario() + self.bonificacao()


class Geren(Funci):

    def __init__(self,nome,cpf,senha,salario=0.0,quant_funci=0):
        #self.nome        = str(nome)
        #self.cpf         = str(cpf)
        #self.salario     = float(salario)

        super().__init__(nome,cpf,salario)
        self.senha       = str(senha)
        self.quant_funci = int(quant_funci)

    def __str__(self):
        str = super().__str__()
        return f"GEN\n" \
               f"{str}" \
               f"Quanti Funci: {self.get_quant_funci()}\n"
        """ 
        f"GEN\n" \
        f"Nome:         {self.get_nome()}\n" \
        f"CPF:          {self.get_cpf()}\n" \
        f"Salario:      {self.get_salario()}\n" \
        f"Quanti Funci: {self.get_quant_funci()}\n"
        """

    def get_senha(self):
        return self.senha

    def set_senha(self, senha_n):
        self.senha = senha_n

    def get_quant_funci(self):
        return self.quant_funci

    def set_quant_funci(self, quant_funci_n):
        self.quant_funci = quant_funci_n

    def autentica(self):
        senha = input("Digite a senha\n > ")
        if str(senha) == self.get_senha():
            print("[Acesso Permitido]")
            return True
        elif str(senha) != self.get_senha():
            print("[Acesso Negado]")
            return False

    def salario_total(self):
        return super().salario_total() + 500


class Vende(Funci):
    def __init__(self,nome,cpf,salario=0.0,valor_venda=0.0,pct_comi=0.0):
        super().__init__(nome,cpf,salario)
        self.valor_venda = valor_venda
        self.pct_comi = pct_comi


if __name__ == '__main__':
    pessoa = Funci("Carlos","123-123-123-12",1200)
    pessoa2 = Geren("Paulo","321-321-321-32",123456,3200,12)
    pessoa3 = Vende("Carla","234-234-234-54",1500)

    print(pessoa)
    print(pessoa2)

    # essoa2.autentica()

    print(pessoa.__dict__)

    print(pessoa2.salario_total())






