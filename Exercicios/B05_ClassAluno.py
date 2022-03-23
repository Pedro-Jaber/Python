





class Aluno(object):

    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_mensalidade(self):
        return self.mensalidade

    def set_mensalidade(self, n_valor):
        self.mensalidade = n_valor

    def get_idade(self):
        return self.idade

    def set_idade(self, n_idade):
        self.idade = n_idade

    def mostra_dados(self):
        print(f"Nome:      {self.get_nome()}")
        print(f"Mensalida: {self.get_mensalidade()}")
        print(f"Idade:     {self.get_idade()}")

    def aumento_mensalidade(self, aumento):
        self.set_mensalidade(self.get_mensalidade() + aumento)

    def aumento_mensalidade_porc(self, porc):
        self.mensalidade += self.mensalidade * porc/100