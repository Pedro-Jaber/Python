"""
PEDRO HENRIQUE JABER CAVALCANTE
22107003
14/03/2022
"""


class Pessoa:

    ctt = 0
    lista = []

    def __init__(self,nome):
        self.nome = nome
        Pessoa.ctt += 1
        Pessoa.lista.append(self.nome)
        print("[Objeto Criado]")

    def __str__(self):
        return f"[{self.__class__.__name__:10s}]---------------------------\n" \
               f"NOME:    {self.get_nome():30s}\n" \
               f"---------------------------------------"

    def get_nome(self):
        return self.nome

    def set_nome(self,n_nome):
        if type(n_nome) == str:
            self.nome = n_nome
        else:
            print("ERRO: [Nome Invalido]")

    @classmethod
    def get_qtd(cls):
        return Pessoa.ctt

    @classmethod
    def get_lista(cls):
        return Pessoa.lista


class Professor(Pessoa):

    def __init__(self,nome,qtd_turma=0):
        super().__init__(nome)

        self.qtd_turma = qtd_turma

    def __str__(self):
        return f"[{self.__class__.__name__:10s}]---------------------------\n" \
               f"NOME:    {self.get_nome():30s}\n" \
               f"TURMAS:  {self.get_qtd_turma():02d}\n" \
               f"---------------------------------------"

    def get_qtd_turma(self):
        return self.qtd_turma

    def set_qtd_turma(self,qtd):
        if isinstance(qtd,int) and qtd > 0:
            self.qtd_turma = qtd
        else:
            print("ERRO: [Quantidade Invalida]")

    def rendimento(self,valor):
        qtd_turmas = self.qtd_turma

        rendimento = valor * qtd_turmas
        return rendimento

class Funcionario(Pessoa):

    def __init__(self,nome,salario=1200.0):
        super(Funcionario, self).__init__(nome)

        self.salario = float(salario)

    def __str__(self):
        return f"[{self.__class__.__name__:10s}]--------------------------\n" \
               f"NOME:    {self.get_nome():30s}\n" \
               f"SALARIO: {self.get_salario():6.2f}\n" \
               f"---------------------------------------"

    def get_salario(self):
        return self.salario

    def set_salario(self,n_salario):
        if isinstance(n_salario,float) and n_salario > 0:
            self.salario = n_salario
        else:
            print("ERRO: [Salario Invalido]")


if __name__ == '__main__':
    pessoa01 = Pessoa("Jerfesson")
    professor = Professor("Jorisclado",5)
    professor2 = Professor("Borisvaldo")
    funcionario = Funcionario("Fulano",10000)

    print("\n////////////////////////////////////////\n")
    print(pessoa01)
    print("\n////////////////////////////////////////\n")
    print(professor)

    print(professor.rendimento(150))
    print("\n////////////////////////////////////////\n")
    print(funcionario)
    print("\n////////////////////////////////////////\n")
    print(Pessoa.get_qtd())
    print(Pessoa.lista)
