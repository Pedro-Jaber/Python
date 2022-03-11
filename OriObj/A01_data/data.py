
class Data:

    def __init__(self, dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formadata(self):
        self.dia = f"{self.dia:02d}"
        self.mes = f"{self.mes:02d}"
        self.ano = f"{self.ano[2:]}"

        print(self.dia,self.mes,self.ano, sep="/")