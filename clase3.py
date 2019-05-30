

# DICCIONARIOS

dic = {1: ['hola', 2, 3], 2: {}, 100: 'algo', 'a': 2, 'b': "asdasd"}
dic = {}
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

for claves in dic.keys():
    print(claves)

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


class Persona(object):
    """Clases persona......"""

    def __init__(self, nombre, apellido=None, tel=None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__tel = tel

    @property
    def nombre(self):
        """este metodo devuelve el nombre"""
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        """este metodo devuelve el nombre"""
        return self.__apellido

    @apellido.setter
    def nombre(self, apellido):
        self.__apellido = apellido



    def caminar(self):
        print(self.__nombre, "esta caminando")


class Empleado(Persona):

    def __init__(self, cuit, nombre):
        Persona.__init__(self, nombre)
        self.cuit = cuit

    def trabajar(self):
        print('algo')

e = Empleado(1234, 'walter')
e.nombre = "juan"
e1 = Empleado(1235, 'juan')
e1.nombre = "julian"


p1 = Persona('walter', 'sanchez',789)
p2 = Persona('maria', 'jose', 456)
p3 = Persona('Ana', 'jose', 456)

#p1.nombre= "walter"
#print(p1.nombre)
# print(type(p))
# print(p == p1)
# print(p.nombre, p1.nombre)
# print(p.apellido, p1.apellido)
# p.caminar()
# p1.caminar()
# p.set_nombre("Pepe")
# print(p.get_nombre())

def criterio(elemento):
    return elemento.nombre

lista = [p1, p2, p3, e1, e]
lista.sort(key=criterio)
for per in lista:
    print(per.nombre)
    if(isinstance(per, Empleado)):
        per.trabajar()
