"""
Nome: Pedro Henrique Jaber Cavalcante
RA:   22107003
Data: 20/10/2021
"""
"""
1. Crie uma classe com o método construtor e pelo menos três atributos. E use dois atributos com
valor default (padrão).

2. Crie os métodos gets e sets dos atributos.

3. Crie pelo menos dois métodos funcional.

4. No método main, teste (use) a classe criada, crie pelo menos três objetos dessa classe, um objeto
passando três argumentos, um objeto passando dois argumentos e um objeto passando um
argumento.

5. E teste (use) todos os métodos desenvolvidos na classe.

Prof. Barbosa
"""

class Aviao:

    def __init__(self,nome,empresa,assentos=200,comprimento_m=40.0,envergadura_m=40.0,passageiros=0):
        self.nome          = str(nome)
        self.empresa       = str(empresa)
        self.assentos      = int(assentos)
        self.comprimento_m = float(comprimento_m)
        self.envergadura_m = float(envergadura_m)
        self.passageiros   = int(passageiros)

    def __str__(self):
        return f"\n------------------------\n" \
               f"{self.get_empresa()} - [{self.get_nome()}]\n" \
               f"Num Assentos:    {self.get_assentos():3d}\n" \
               f"Num Passageiros: {self.get_passageiros():3d}\n" \
               f"Comprimento:     {self.get_comprimento_m():6.2f}m\n" \
               f"Envergadura:     {self.get_envergadura_m():6.2f}m\n" \
               f"------------------------\n"

    def set_nome(self, nome_n):
        if type(nome_n) == str:
            self.nome = nome_n
        else:
            print("[Nome Invalido]")

    def get_nome(self):
        return self.nome

    def set_empresa(self, empresa_n):
        if type(empresa_n) == str:
            self.empresa = empresa_n
        else:
            print("[Empresa Invalido]")

    def get_empresa(self):
        return self.empresa

    def set_assentos(self, assentos_n):
        if assentos_n > 0:
            self.assentos = assentos_n
        else:
            print("[Numero Invalido]")

    def get_assentos(self):
        return self.assentos

    def set_comprimento_m(self, comprimento_m_n):
        if comprimento_m_n > 0:
            self.comprimento_m = comprimento_m_n
        else:
            print("[Numero Invalido]")

    def get_comprimento_m(self):
        return self.comprimento_m

    def set_envergadura_m(self, envergadura_m_n):
        if envergadura_m_n > 0:
            self.envergadura_m = envergadura_m_n
        else:
            print("[Numero Invalido]")

    def get_envergadura_m(self):
        return self.envergadura_m

    def set_passageiros(self, passageiros_n):
        if 0 < passageiros_n <= self.get_assentos():
            self.passageiros = passageiros_n
        else:
            print("[Numero Invalido de Passageiros]")
            print(f"[Numero Maximo ({self.get_assentos()})]")

    def get_passageiros(self):
        return self.passageiros

    def add_passageiro(self):
        if self.get_passageiros() < self.get_assentos():
            self.passageiros += 1
        else:
            print("[!!Avião Cheio!!]")

    def troca_empresa(self):
        print(f"\nAtual [{self.get_empresa()}]")
        empresa = input("Digite o nome da empresa \n > ")
        self.set_empresa(empresa)
        print(self)
        print("[Empresa Trocada Com Sucesso]")


if __name__ == '__main__':
    aviao1 = Aviao("A320","Gol",220,37.57,34.10)
    aviao2 = Aviao("Boing 747","Emirates",480,70.6)
    aviao3 = Aviao("A380","Latam",853)
    aviao4 = Aviao("Boing 777X","Azul")

    print("\n~(1)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    print(aviao1)
    print(aviao2)
    print(aviao3)
    print(aviao4)

    print("\n~(2)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    aviao1.set_empresa("Azul")
    aviao1.set_passageiros(300)
    aviao1.set_nome(350)

    aviao2.set_envergadura_m(59.6)

    aviao3.set_comprimento_m(72)
    aviao3.set_envergadura_m(79)

    aviao4.set_assentos(440)
    aviao4.set_comprimento_m(63.7)
    aviao4.set_envergadura_m(60.9)

    print("\n~(3)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    for i in range(0,100):
        aviao1.add_passageiro()

    for i in range(0,430):
        aviao2.add_passageiro()

    for i in range(0,652):
        aviao3.add_passageiro()

    for i in range(0,201):
        aviao4.add_passageiro()

    print("\n~(4)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    aviao1.troca_empresa()
    aviao3.troca_empresa()

    print("\n~(5)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    print(aviao1)
    print(aviao2)
    print(aviao3)
    print(aviao4)
















