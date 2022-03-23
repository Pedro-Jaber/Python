"""
Pedro Henrique Jaber Cavalcante
22107003
28/10/2021
"""


class Veiculo:

    def __init__(self,valor,modelo,km=0):
        self.valor = valor
        self.modelo = modelo
        self.km = km

    def get_valor(self):
        return self.valor

    def set_valor(self,n_valor):
        self.valor = n_valor

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, n_modelo):
        self.modelo = n_modelo

    def get_km(self):
        return self.km

    def set_km(self, n_km):
        self.km = n_km

    def atua_valor(self,valor_n):
        if valor_n > 0:
            self.valor += valor_n
        else:
            print("[Valor Invalido]")

    def atua_valor_pct(self,pct):
        if pct > 0:
            pct /= 100
            n_valor = self.get_valor() + (self.get_valor() * pct)
            self.set_valor(n_valor)
        else:
            print("[Valor Invalido]")

    def ver_status(self):
        if self.get_km() == 0:
            print(f"[{self.__class__.__name__} Zero]")
        elif self.get_km() <= 20000:
            print(f"[{self.__class__.__name__} Seminovo]")
        elif self.get_km() > 20000:
            print(f"[{self.__class__.__name__} Usado]")
        else:
            print("Erro 030")

    def ipva(self):
        pct = 0
        if self.__class__ == Carro:
            pct = 0.03
        elif self.__class__ == Moto:
            pct = 0.02
        else:
            print("[Veiculo Não Especificado]")
            return 0

        return (self.get_valor() * pct) + 100

class Carro(Veiculo):

    def __init__(self,valor,modelo,qtd_portas=4,km=0):
        super().__init__(valor,modelo,km)

        self.qtd_portas = qtd_portas

    def __str__(self):
        return f"Veiculo\n" \
               f"Tipo: {self.__class__.__name__}\n" \
               f"Valor: {self.valor}\n" \
               f"Modelo: {self.modelo}\n" \
               f"Km: {self.km}\n" \
               f"Portas: {self.qtd_portas}\n"

    def ipva(self):
        ipva = (self.get_valor() * 0.03) + 100
        return ipva

class Moto(Veiculo):

    def __init__(self,valor,modelo,cilindradas,km=0):
        super().__init__(valor,modelo,km)

        self.cilindradas = cilindradas

    def __str__(self):
        return f"Veiculo\n" \
               f"Tipo: Moto\n" \
               f"Valor: {self.valor}\n" \
               f"Modelo: {self.modelo}\n" \
               f"Km: {self.km}\n" \
               f"Cilindradas: {self.cilindradas}\n"


if __name__ == '__main__':
    carro1 = Carro(1000,"slakkk",1000,4)
    carro2 = Carro(80000,"slasla",3000)
    carro3 = Carro(67000,"toptop")

    print(carro1)
    print(carro2)
    print(carro3)

    # moto1 = Moto(20000,"vrumvrum",1000,300)
    # moto2 = Moto(16000,"vrum",900)

    # print(vars(carro1))
    # print(vars(moto1))

    # print(carro1.__dict__)

    # moto1.atua_valor(1220)

    # print(moto1)

    carro1.atua_valor_pct(100)

    print(carro1)
    print(carro1.ipva())





















