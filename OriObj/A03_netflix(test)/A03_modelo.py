#
#
#
#
#

class Programa:
    def __init__(self, nome, ano):
        self._nome  = nome.title()
        self.ano    = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title

    @property
    def likes(self):
        return self._likes

    """@likes.setter
    def likes(self, likes):
        self._likes = likes"""

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f"Nome: {self.nome} \nAno: {self.ano} \nLikes : {self._likes}\n"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self.nome} \nAno: {self.ano} \nDuração: {self.duracao} min\nLikes : {self._likes}\n"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self.nome} \nAno: {self.ano} \nTemporadas: {self.temporadas}\nLikes : {self._likes}\n"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):            #vira um interavel [funcina +- igual a uma list]
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

    # def tamanho(self):
    #     return len(self.programas)



#
#


if __name__ == '__main__':
    vingadores = Filme('vingadores', 2018, 160)
    hilda = Serie('Hilda', 2019, 3)
    tmep = Filme('todo mundo em panico', 1999, 100)
    demolidor = Serie('demolidor', 2016, 2)


    likes = True
    if likes == True:
        demolidor.dar_likes()
        demolidor.dar_likes()
        demolidor.dar_likes()
        demolidor.dar_likes()
        demolidor.dar_likes()
        demolidor.dar_likes()
        demolidor.dar_likes()
        demolidor.dar_likes()
        demolidor.dar_likes()
        demolidor.dar_likes()
        demolidor.dar_likes()
        tmep.dar_likes()
        tmep.dar_likes()
        tmep.dar_likes()
        tmep.dar_likes()
        tmep.dar_likes()
        tmep.dar_likes()
        hilda.dar_likes()
        hilda.dar_likes()
        hilda.dar_likes()
        hilda.dar_likes()
        hilda.dar_likes()
        vingadores.dar_likes()
        vingadores.dar_likes()
        vingadores.dar_likes()
        vingadores.dar_likes()
        vingadores.dar_likes()
        vingadores.dar_likes()
        vingadores.dar_likes()
        vingadores.dar_likes()
        vingadores.dar_likes()

    lista_de_programas = [vingadores, hilda, demolidor, tmep]
    playlist_fim_de_semana = Playlist('fim de semana', lista_de_programas)

    print(f"Tamanho da Playlist: {len(playlist_fim_de_semana)}\n")
    for programa in playlist_fim_de_semana:
        print(programa)

















































