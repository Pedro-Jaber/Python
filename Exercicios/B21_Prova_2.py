"""
Pedro Henrique Jaber Cavalcante
22107003
11/11/2021
"""
"""
class Empregado():

    def __init__(self, nome, idade=18, salario=1100):
        self.nome    = nome
        self.idade   = idade
        self.salario = salario

    def __str__(self):
        return f"Empregado\n" \
               f"Nome:    {self.get_nome()}\n" \
               f"Idade:   {self.get_idade()}\n" \
               f"Salario: {self.get_salario():.2f}\n"

    def set_nome(self,nome_n):
        if type(nome_n) == str:
            self.nome = nome_n
        elif type(nome_n) != str:
            print("[Nome Invalido]")

    def get_nome(self):
        return self.nome

    def set_idade(self, idade_n):
        if idade_n > 18:
            self.idade = idade_n
        elif idade_n < 18:
            print("Idade Invalida")

    def get_idade(self):
        return self.idade

    def set_salario(self, salario_n):
        self.salario = salario_n

    def get_salario(self):
        return self.salario

    def aumenta_salario(self, pct):
        pct /= 100
        salario = self.get_salario()
        n_salario = salario + (salario * pct)
        print(f"Salario: {self.salario} >>[+ %{pct*100:.1f}]>> {n_salario}")

        self.set_salario(n_salario)

    def salario_anual(self): ###############################
        anual = self.get_salario() * 13
        return anual

    # Elabora uma função bonus_venda ela receba a quantidade de vendas que o funcionario fez
    # e da um bonus de 50 reais para cada venda
    
    def bonus_venda(self, qtd_vendas):
        bonus = qtd_vendas * 50
        self.salario += bonus


if __name__ == '__main__':

    emp1 = Empregado("Carlos")
    emp2 = Empregado("Peter", 30)
    emp3 = Empregado("Ana", salario=1500)

    print(emp1)
    print(emp2)
    print(emp3)

    print("(1)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    emp2.bonus_venda(5)

    print(emp2)

    print("(2)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # pct = int(input("Em quanto deseja aumentar em %?"))
    # emp1.aumenta_salario(pct)

    emp2.set_nome(110)
    emp1.set_nome("Aderbal")

    print(emp1)
    print(emp2)

    print("(3)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print(emp1.salario_anual())

    print("(4)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    emp3.aumenta_salario(10)

    print(emp3)

    print("(5)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print(emp1)
    print(emp2)
    print(emp3)

"""

"""
class Pessoa:
    qtd_pessoas = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.qtd_pessoas += 1

    def __str__(self):
        return f"Nome {self.nome}\n"

    @classmethod
    def get_qtd_pessoa(cls):
        return Pessoa.qtd_pessoas

    def set_nome(self,nome_n):
        if type(nome_n) == str:
            self.nome = nome_n
        elif type(nome_n) != str:
            print("[Nome Invalido]")

    def get_nome(self):
        return self.nome


class Professor(Pessoa):

    def __init__(self, nome, qtd_turmas=2):  # Turmas por semana
        super().__init__(nome)
        self.qtd_turmas = qtd_turmas

    def set_qtd_turmas(self, qtd):
        if qtd < 2:
            print("[Numero Invalido] O seu numero minimo de turmas é 2")
        elif qtd > 10:
            print("[Numero Invalido] Número máximo de turmas excedido [Max = 10]")
        else:
            print(f"[Numero de turmas definida com sucesso para {qtd}]")

    def get_qtd_turmas(self):
        return self.qtd_turmas

    def rendimento(self, valor_turmar):
        rendimento = (valor_turmar * self.qtd_turmas) * 4
        return rendimento


class Funcionario(Pessoa):
    
    def __init__(self, nome, salario=1100):
        super().__init__(nome)
        self.salario = float(salario)

    def set_salario(self, salario_n):
        if salario_n > 1100:
            self.salario = salario_n
        elif salario_n < 1100:
            print("[Salario Invalido]")


if __name__ == '__main__':

    pessoa1 = Professor("Carlos", 5)
    pessoa2 = Professor("Clara", 10)
    pessoa3 = Professor("Bruno", 7)
    pessoa4 = Professor("Ivan", 4)
    pessoa5 = Professor("Ana", 8)

    pessoa6 = Funcionario("Roberto")
    pessoa7 = Funcionario("Carla")
    pessoa8 = Funcionario("Marcos")
    pessoa9 = Funcionario("Marilia")
    pessoa10 = Funcionario("Ivandro")

    print(Pessoa.qtd_pessoas)

    pessoa1.set_qtd_turmas(7)
    pessoa4.set_qtd_turmas(11)

    print(pessoa4.rendimento(125))
    print(pessoa5.get_qtd_turmas())

    pessoa7.set_salario(1500)
    pessoa8.set_salario(1000)
"""



















