





class Pessoa():

    def __init__(self, nome, sobrenome, idade = 25):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def __str__(self):
        return f"Nome Completo: {self.nome} {self.sobrenome} Idade: {self.idade}"

    def get_nome(self):
        return self.nome

    def set_nome(self,novo_nome):
        self.nome = novo_nome

    def get_sobrenome(self):
        return self.sobrenome

    def set_sobrenome(self, novo_sobrenome):
        self.sobrenome = novo_sobrenome

    def get_nome_completo(self):
        print(f"Nome Completo: {self.get_nome()} {self.get_sobrenome()}")

    def get_idade(self):
        return self.idade

    def set_idade(self,nova_idade):
        if 0 <= nova_idade <= 140 and type(nova_idade) == int:
            self.idade = nova_idade
        else:
            print("Idade Invalida")

    def most_dados(self):
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        self.get_nome_completo()
        print("----")
        print(f"Nome:      {self.nome}")
        print(f"Sobrenome: {self.sobrenome}")
        print(f"Idade:     {self.idade}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        return ''

    def mais_velho(self, pessoa2):
        if self.idade == pessoa2.idade:
            print("Idades iguais")
        elif self.idade > pessoa2.idade:
            print(self.__str__())
        elif self.idade < pessoa2.idade:
            print(pessoa2.__str__())


    """
    def compara_valor(self, carro2):
        if self.valor == carro2.valor:
            print("Preços Iguais")
        elif self.valor > carro2.valor:
            print("-----------------------------------------")
            print(f"[O carro '{carro2.modelo}' é mais Barato]")
            print("-----------------------------------------")
            print("[Carro Mais Barato]")
            carro2.mostra_info()
            print("-----------------------------------------")
            print("[Carro Mais Caro]")
            self.mostra_info()
            print("-----------------------------------------")

        elif self.valor < carro2.valor:
            print("-----------------------------------------")
            print(f"[O carro '{self.modelo}' é mais Barato]")
            print("-----------------------------------------")
            print("[Carro Mais Barato]")
            self.mostra_info()
            print("-----------------------------------------")
            print("[Carro Mais Caro]")
            carro2.mostra_info()
            print("-----------------------------------------")

    """