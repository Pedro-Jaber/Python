"""
PEDRO HENRIQUE JABER CAVALCANTE
22107003
07/03/2022
"""


class Livro:

    # Inicia o Objeto
    def __init__(self, titulo, autores, paginas=0, preco=0.0):
        print("[Iniciando a classe...]")
        self.titulo  = titulo
        self.autores   = autores
        self.paginas = paginas
        self.preco   = preco
        print("[Classe Iniciada]\n")

    # Printa o Livro
    def __str__(self):
        return f"Titulo:    {self.titulo:20s} |\n" \
               f"Autores:   {self.get_autores()} |\n" \
               f"Paginas:   {self.paginas:<20d} |\n" \
               f"Preço:     R$ {self.preco:<17.2f} |\n" \
               f"Preço\Pag: R$ {self.get_preco_pagina():<17.2f} |\n"

    # /Métodos Get////////////////////////////////

    def get_titulo(self):
        return self.titulo

    def get_autores(self,mode=1):
        # autores_list = self.get_autores()
        if mode == 1:
            return self.autores
        """
        elif mode == 2:
            for autor in autores_list:
                print(autor)
        """

    def get_paginas(self):
        return self.paginas

    def get_preco(self):
        return self.preco

    def get_preco_pagina(self):
        preco = self.get_preco()
        paginas = float(self.get_paginas())

        preco_p_pagina = preco/paginas
        return preco_p_pagina

    # ////////////////////////////////////////////

    # /Métodos Set////////////////////////////////

    def set_titulo(self, titulo_n):
        self.titulo = titulo_n

    def set_autores(self, autores_n):
        invalido = False

        for autor in autores_n:
            if not isinstance(autor, str):  # if type(autor) != str:
                print("[Autor Invalido!]")
                invalido = True
                break

        if invalido == False:
            if isinstance(autores_n, list) and len(autores_n) > 0:
                self.autores = autores_n

    def set_paginas(self, paginas_n):
        self.paginas = paginas_n

    def set_preco(self, preco_n):
        self.preco = preco_n

    # ////////////////////////////////////////////

    # /Métodos Autores////////////////////////////

    def add_autor(self,novo_autor):
        self.autores.append(novo_autor)

    def del_autor(self,autor_del):
        autores_list = self.autores

        if autor_del in autores_list:
            autores_list.remove(autor_del)

        elif not autor_del in autores_list:
            print("[Autor não encontrado]")

    def pes_autor(self,autor_find):
        autores_list = self.autores

        ctt=0
        for autor in autores_list:
             if autor == autor_find:
                 print(f"{autor} - Index[{ctt}]")
             ctt+=1
        if autor_find not in autores_list:
            print("[Autor não encontrado]")

    def atu_autor(self):
        autores_list = self.autores

        self.autores_vert()
        index = int(input("Qual autor deseja Atualizar? \n > "))
        index -= 1
        autor_atu = (input("Novo nome > "))
        autores_list[index] = autor_atu
        print("[Lista Atualizada]\n")
        self.autores_vert()

        """
        ctt = 0
        for autor in autores_list:
            if autor == autor_atu:
                autores_list[ctt] = autor_atu
                print("[Lista Atualizada]")
                print(autores_list)
            ctt += 1
        if autor_atu not in autores_list:
            print("[Autor não encontrado]")
        """

    def autores_vert(self):
        autores_list=self.get_autores()
        print("[-- Autores]")
        ctt = 1
        for autor in autores_list: # for i,autor in enumerate(self.autores):
            print(f"{ctt} - {autor}")
            ctt += 1

    # ////////////////////////////////////////////

    # /Métodos////////////////////////////////////

    def verifica(self):
        pass

    def aumenta_preco(self,n_preco):
        self.set_preco(n_preco)
        print(f"Novo Preço = {n_preco}")

    def desc_pct(self,pct):
        preco = self.get_preco()
        desc_pct = pct/100

        preco_com_desc = preco - (preco*desc_pct)
        self.set_preco(preco_com_desc)

    # ////////////////////////////////////////////

if __name__ == '__main__':
    livro1 = Livro("Harry_Potter", ["ABC"], 250, 25.10)
    livro2 = Livro("ABCDEF", ["apo","ABC"], 120)
    print("///////////////////////////////")

    print(livro1)
    livro1.desc_pct(10)
    print(livro1)

    print("///////////////////////////////")

    livro1.set_autores(["POI","JIBC"])

    print(livro1.get_autores())

    print("///////////////////////////////")
    print(livro2.get_autores())
    livro2.autores_vert()

    livro2.pes_autor("ABCD")
    livro2.atu_autor()


