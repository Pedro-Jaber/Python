from abc import ABC,abstractmethod


class Carro(ABC):

    def __init__(self, modelo, preco_base):
        self.modelo = modelo
        self.preco_base = preco_base

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, n_modelo):
        if isinstance(n_modelo, str):
            self.modelo = n_modelo

    def get_preco_base(self):
        return self.preco_base

    def set_preco_base(self,n_preco):
        if isinstance(n_preco, float) or isinstance(n_preco,int):
            self.preco_base = n_preco

    @abstractmethod
    def preco_diaria(self):
        ...


class Economico(Carro):

    def __init__(self,modelo, preco_base):
        super().__init__(modelo,preco_base)

    def preco_diaria(self):
        preco_base = self.get_preco_base()
        pct = 5

        diaria = preco_base + (preco_base * 0.05)

        return diaria

if __name__ == '__main__':


    carro1 = Economico("123", 100)

    print(carro1.preco_diaria())

