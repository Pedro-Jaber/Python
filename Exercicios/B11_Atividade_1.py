"""
Pedro Henrique Jaber Cavalcante
16/09/2021
"""


class Empresa:

    def __init__(self, num_funci, nome):
        self.num_funci = num_funci
        self.nome = nome

    def __str__(self):
        return f"Nome: {self.nome} | Numero de Funcionarios {self.num_funci}"

    def set_num_funci(self, num):
        self.num_funci = num

    def get_num_funci(self):
        return self.num_funci

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_nome(self):
        return self.nome

    def maior_empresa(self, empresa2):
        if self.num_funci == empresa2.num_funci:
            print("Numero de funcionarios =")
        elif self.num_funci > empresa2.num_funci:
            print("[Maior empresa]")
            print(self)
        elif self.num_funci < empresa2.num_funci:
            print("[Maior empresa]")
            print(empresa2)

    def juntar_empresa(self, empresa2):
        self.nome = f"{self.nome} - {empresa2.nome}"
        self.num_funci += empresa2.num_funci


if __name__ == '__main__':
    empresa1 = Empresa(5000, "Apple")
    empresa2 = Empresa(6000, "Google")


    print(empresa1.get_nome())
    print(empresa1.get_num_funci(),"\n")
    print(empresa2.get_nome())
    print(empresa2.get_num_funci(),"\n")
    print("")

    empresa1.set_nome("Samsung")
    empresa1.set_num_funci(4500)
    empresa2.set_nome("Microsoft")
    empresa2.set_num_funci(6500)

    print(empresa1)
    print(empresa2)
    print("")


    empresa1.maior_empresa(empresa2)
    print("")


    empresa1.juntar_empresa(empresa2)
    print(empresa1)









