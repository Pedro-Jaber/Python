





class Carro():

    def __init__(self, modelo, ano = 0, valor = 0):
        self.modelo = modelo
        self.ano    = ano
        self.valor  = float(valor)

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def get_ano(self):
        return self.ano

    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def get_valor(self):
        return self.valor

    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print("Valor Incorreto")

    def aumenta_valor(self,valor_add):
        if valor_add > 0:
            self.valor += valor_add
        else:
            print("Valor Incorreto")



    def mostra_info(self):
        print(f"Modelo: {self.modelo}")
        print(f"Ano:    {self.ano}")
        print(f"Valor:  {self.valor}")

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

        else:
            print("Erro01")

























