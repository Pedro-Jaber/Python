class Livro:

    def __init__(self, titulo, autor="", paginas=0, preco=0.0):
        print("[Iniciando a classe...]")
        self.titulo  = titulo
        self.autor   = autor
        self.paginas = paginas
        self.preco   = preco
        print("[Classe Iniciada]\n")

    def __str__(self):
        return f"Titulo:    {self.titulo:20s} |\n" \
               f"Autor:     {self.autor:20s} |\n" \
               f"Paginas:   {self.paginas:<20d} |\n" \
               f"Preço:     R$ {self.preco:<17.2f} |\n" \
               f"Preço\Pag: R$ {self.get_preco_pagina():<17.2f} |\n"

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_paginas(self):
        return self.paginas

    def get_preco(self):
        return self.preco

    def get_preco_pagina(self):
        preco = self.get_preco()
        paginas = float(self.get_paginas())

        preco_p_pagina = preco/paginas
        return preco_p_pagina

    def set_titulo(self, titulo_n):
        self.titulo = titulo_n

    def set_autor(self, autor_n):
        self.autor = autor_n

    def set_paginas(self, paginas_n):
        self.paginas = paginas_n

    def set_preco(self, preco_n):
        self.preco = preco_n

    def aumenta_preco(self,n_preco):
        self.set_preco(n_preco)
        print(f"Novo Preço = {n_preco}")

    def desc_pct(self,pct):
        preco = self.get_preco()
        desc_pct = pct/100

        preco_com_desc = preco - (preco*desc_pct)
        self.set_preco(preco_com_desc)

if __name__ == '__main__':
    livro1 = Livro("Harry_Potter", "ABC", 250, 25.10)
    livro2 = Livro("ABCDEF", "apo", 120)

    print(livro1)
    livro1.desc_pct(10)
    print(livro1)


