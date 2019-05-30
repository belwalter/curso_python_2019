
def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def producto(n1, n2):
    return n1 * n2

def cuadrado(n1, *otros):
    return n1 * n1

dic_op = {'+': sumar, '-': restar, '*': producto, 'p': cuadrado}

def calc(n1, n2, operador):
    return dic_op[operador](n1, n2)

print(calc(2, 4, 'p'))


class Animal(object):

    def moverse(self):
        print("el animal se mueve")

class Terrestre(Animal):

    def desplazarse(self):
        print("el animal camina")

class Acuatico(Animal):

    def desplazarse(self):
        print("el animal nada")
a = Acuatico()

class Cocodrilo(Acuatico, Terrestre):

    def desplazar(self):
        print('el animal nada o canina dependediendo......')

c = Cocodrilo()
c.desplazarse()

#EXPECIONES
#Clases Abstracta
