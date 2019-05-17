

# DICCIONARIOS

dic = {1: ['hola', 2, 3], 2: {}, 100: 'algo', 'a': 2, 'b': "asdasd"}

# print(type(dic))
# print(len(dic))

dic['b'] = 'nuevo valor'
dic['c'] = 1234
# print(dic['c'])
# valor = dic.pop('c')
# print(valor)

if('c' in dic):
    print('si')
else:
    print('no')

for elemento in dic.values():
    print(elemento)

print("CONJUNTOS")
s = set([1, 2, 3])
s1 = set([4, 2, 5])

print(s.difference(s1))
for elemento in s:
    print(elemento) 

print(type(s))

t = (1, 3, 5)
# print(len(t))

# for elemento in t:
#    print(elemento)

# POO clase objeto | metodos atributos
# constructor
# sobrecargar herencia polimorfimo herencia multiple
# clase abstracta


class Persona():
    """Clases persona......"""

    def __init__(self, nombre, apellido, tel):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__tel = tel


    def get_nombre(self):
        """este metodo devuelve el nombre"""
        return self.__nombre

    def get_apellido(self):
        """este metodo devuelve el nombre"""
        return self.__apellido

    def set_nombre(self, nombre):
        self.__nombre = nombre


    def caminar(self):
        print(self.__nombre, "esta caminando")


p1 = Persona('juan', 'zulma', 1234)
p2 = Persona('maria', 'jose', 456)
p3 = Persona('Ana', 'jose', 456)

# print(type(p))
# print(p == p1)
# print(p.nombre, p1.nombre)
# print(p.apellido, p1.apellido)
# p.caminar()
# p1.caminar()
# p.set_nombre("Pepe")
# print(p.get_nombre())

def criterio(elemento):
    return elemento.get_nombre() + elemento.get_apellido()

lista = [p1, p2, p3]
lista.sort(key=criterio)
for per in lista:
    print(per.get_nombre(), per.get_apellido())
