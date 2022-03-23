import datetime





class Pessoa:

    def __init__(self, nome="none", peso=999.9, dnasc=datetime.date(9999, 12, 31)):
        print(f"Criando {nome}...")
        if type(nome) == str:
            self.nome  = nome
            self.peso  = peso
            self.dNasc  = dnasc
            self.idade = self.defi_idade()
            print("[Pessoa criada]")
        else:
            print("[Nome invalido]")
            print("[Pessoa não registrada]")
            self.nome = "none"
            self.peso = 999.9
            self.dNasc = dNasc
            self.idade = datetime.date(9999, 12, 31)

    def __str__(self):
        return f"Nome:       {self.get_nome()}    \n" \
               f"Peso:       {self.get_peso()}    \n" \
               f"Idade:      {self.get_idade()}   \n" \
               f"Nascimento: {self.formt_dNasc()} \n" \

    def get_nome(self):
        return self.nome

    def set_nome(self, n_nome):
        if type(n_nome) == str:
            self.nome = n_nome
        else:
            print("[Nome Invalido]")

    def get_peso(self):
        return self.peso

    def set_peso(self, n_peso):
        self.peso = n_peso

    def get_idade(self):
        return self.idade

    def set_idade(self, n_idade):
        self.idade = n_idade

    def get_dNasc(self):
        return self.dNasc

    def set_dNasc(self, dia, mes, ano):
        self.dNasc = datetime.date(ano, mes, dia)

    def formt_dNasc(self):
        return f"{self.get_dNasc().day}/{self.get_dNasc().month}/{self.get_dNasc().year}"

    def defi_idade(self):
        hoje = datetime.date.today()
        #vetor_data = str(self.dNasc).split('-')
        #self.dNasc = datetime.date(int(vetor_data[0]),int(vetor_data[1]),int(vetor_data[2]))
        idade = hoje.year - self.dNasc.year

        if hoje.month < self.dNasc.month:
            idade -= 1
        elif hoje.day < self.dNasc.day and hoje.month <= self.dNasc.month:
            idade -= 1

        return idade

    def imc(self, altura):
        peso = int(self.get_peso())
        imc = peso / (altura ** 2)

        return imc


if __name__ == '__main__':
    dNasc = datetime.date(2002, 12, 26)

    pessoa1 = Pessoa("Pedro", 75.5, dNasc)
    pessoa2 = Pessoa(1100, 67)
    print("\n")
    print(pessoa1)
    print("")
    print(pessoa2)

    print("------------------------------")

    print("")
    pessoa1.set_nome("Carlos")
    print(pessoa1.get_dNasc())
    pessoa1.set_dNasc(13,12,1985)
    print("")
    print(pessoa1)

    #print("------------------------------")

    #altura = float(input("Digite sua altura: "))
    #print(f"IMC {pessoa1.imc(altura):.2f}")

    print("------------------------------")

    print(pessoa1)
    print("")
    #print(pessoa2)