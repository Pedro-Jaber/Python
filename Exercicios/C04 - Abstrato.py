"""
Pedro Henrique Jaber Cavalcante
22107003
21/03/2022
"""
from abc import ABC, abstractmethod
import math

pi = math.pi


class FormaGeometrica(ABC):

    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimetro(self):
        ...

    def test(self):
        print(f"\n/!/Test/!/ [Obj: {self.__class__.__name__}]\n")


class Quadrado(FormaGeometrica):

    def __init__(self, lado=1):
        self.lado = lado

    def __str__(self):
        return f"-[Quadrado]-----\n" \
               f"Lado:      {self.get_lado():5.2f}\n" \
               f"Área:      {self.area():5.2f}\n" \
               f"Perímetro: {self.perimetro():5.2f}\n" \
               f"----------------"

    def get_lado(self):
        return self.lado

    def set_lado(self,n_lado):
        if isinstance(n_lado, float) or isinstance(n_lado, int):
            self.lado = n_lado

    def area(self):
        lado = self.get_lado()
        area = lado**2
        return area

    def perimetro(self):
        lado = self.get_lado()
        perimetro = lado*4
        return perimetro


class Circulo(FormaGeometrica):

    def __init__(self,raio):
        self.raio = raio

    def __str__(self):
        return f"-[Circulo]------\n" \
               f"Raio:      {self.get_raio():5.2f}\n" \
               f"Área:      {self.area():5.2f}\n" \
               f"Perímetro: {self.perimetro():5.2f}\n" \
               f"----------------"

    def get_raio(self):
        return self.raio

    def set_raio(self,n_raio=1):
        if isinstance(n_raio, float) or isinstance(n_raio, int):
            self.lado = n_raio

    def area(self):
        raio = self.get_raio()
        area = pi * (raio**2)
        return area

    def perimetro(self):
        raio = self.get_raio()
        perimetro = 2 * pi * raio
        return perimetro



if __name__ == '__main__':

    # test = FormaGeometrica() # Não pode criar um Obj de uma super Abstrata

    quadrado1 = Quadrado(5)
    circulo1  = Circulo(3)

    print(quadrado1)
    print(circulo1)

    quadrado1.test()
    circulo1.test()
