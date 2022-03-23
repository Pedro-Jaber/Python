





class Produto:
    def __init__(self,nome,vlr_com=0.0,vlr_ven=0.0,qtd_estoque=1,qtd_min=1):
        self.nome = nome.capitalize()
        self.vlr_com = float(vlr_com)
        self.vlr_ven = float(vlr_ven)
        self.qtd_estoque = qtd_estoque
        self.qtd_min = qtd_min

    def __str__(self):
        return f"|{self.get_nome()}|_____________\n" \
               f"|Valor Compra: {self.get_vlr_com():5.2f}|\n" \
               f"|Valor Venda:  {self.get_vlr_ven():5.2f}|\n" \
               f"|-------------------|\n" \
               f"|#####| Lucro: {self.ver_lucro():5.2f}|\n" \
               f"|-------------------|\n" \
               f"|Quantidade:        |\n" \
               f"|-Estoque:     {self.formt_estoque()}|\n" \
               f"|-Minima:       {self.get_qtd_min():4d}|\n"

    def formt_estoque(self):
        if self.alerta_estoque() == False:
            estoque = f"\033[1;32;48m{self.get_qtd_estoque():5d}\033[0;0;48m"
            return estoque
        elif self.alerta_estoque() == True:
            estoque = f"\033[1;31;48m!{self.get_qtd_estoque():4d}\033[0;0;48m"
            return estoque

    def get_nome(self):
        return self.nome

    def set_nome(self, n_nome):
        if type(n_nome) == str :
            self.nome = n_nome.capitalize()
        else:
            print("[Nome Invalido]")

    def get_vlr_com(self):
        return self.vlr_com

    def set_vlr_com(self, n_vlr_com):
        if n_vlr_com > 0:
            self.vlr_com = n_vlr_com
        else:
            print("[Valor Invalido]")

    def get_vlr_ven(self):
        return self.vlr_ven

    def set_vlr_ven(self, n_vlr_ven):
        if n_vlr_ven > self.get_vlr_com():
            self.vlr_ven = n_vlr_ven
        elif 0 < n_vlr_ven < self.get_vlr_com():
            print("[Valor de Venda menor do que de Compra]")
        else:
            print("[Valor Invalido]")

    def get_qtd_estoque(self):
        return self.qtd_estoque

    def set_qtd_estoque(self, n_qtd_estoque):
        if n_qtd_estoque > 0:
            self.qtd_estoque = n_qtd_estoque
        else:
            print("[Quantidade Invalida]")

    def get_qtd_min(self):
        return self.qtd_min

    def set_qtd_min(self, n_qtd_min):
        self.qtd_min = n_qtd_min

    def ver_lucro(self):
        lucro = self.get_vlr_ven() - self.get_vlr_com()
        return lucro

    def alerta_estoque(self):
        alerta = False
        if self.get_qtd_estoque() <= self.get_qtd_min():
            alerta = True
        return alerta

    def atualiza_estq(self, vendido):
        if vendido <= self.get_qtd_estoque():
            self.set_qtd_estoque(self.get_qtd_estoque() - vendido)

            if self.alerta_estoque() == True:
                print("[Estoque Baixo]")

        else:
            print("[Valor Invalido]")

    def repor_estq(self, comprado):
        if comprado > 0:
            self.set_qtd_estoque(self.get_qtd_estoque() + comprado)
        else:
            print("[Valor Invalido]")




if __name__ == '__main__':
    arroz =   Produto("arroz", 15, 19.50, 67, 20)
    batata =  Produto("batata")
    cenoura = Produto("Cenoura", 5)
    farinha = Produto("farinha", qtd_estoque=20)
    print("\n~(Original)~")
    print(arroz)
    print(batata)
    print(cenoura)
    print(farinha)

    print("~(1)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    arroz.set_qtd_min(25)
    print(arroz)

    print("~(2)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    arroz.set_nome(123)
    arroz.set_qtd_estoque(100)

    print(arroz)

    print("~(3)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    arroz.set_vlr_com(-10)  # Invalido
    arroz.set_vlr_com(16)   # Valido

    print(arroz)

    print("~(4)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    arroz.set_vlr_ven(15)     # Invalido
    arroz.set_vlr_ven(0)      # Invalido
    arroz.set_vlr_ven(20.45)  # Valido

    print(arroz)

    print("~(5)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    arroz.atualiza_estq(75)

    print(arroz)












