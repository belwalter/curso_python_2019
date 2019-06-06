
#from abc import ABCMeta
import abc

class Forma(metaclass=abc.ABCMeta):

    color = None

    @abc.abstractmethod
    def calcular_area(self):
        pass

    @abc.abstractmethod
    def calcular_perimetro(self):
        pass


class Circulo(Forma):

    def __init__(self, radio, color=None):
        Forma.color = color
        self.radio = radio

    def calcular_area(self):
        return 3.14 * (self.radio**2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio


class Rectangulo(Forma):

    def __init__(self, lado1, lado2, color=None):
        self.lado1 = lado1
        self.lado2 = lado2
        Forma.color = color

    def calcular_area(self):
        return self.lado1 * self.lado2

    def calcular_perimetro(self):
        return (2 * self.lado1) + (2 * self.lado2)

f = Circulo(5, "rojo")
e = Rectangulo(2, 2)

l = [e, f]
for forma in l:
    print(forma.calcular_area(), f.color)
    print(forma.calcular_perimetro())


from random import randint

for i in range(0, 10):
    print(randint(0, 100))


from funciones.operaciones import sumar, restar, producto

print(sumar(1, 2))
print(restar(1, 2))
print(producto(1, 2))
