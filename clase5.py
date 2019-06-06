
# EXCEPCIONES

numero = "15"
numero2 = 0
lista = [1, 2, 3]

try:
    num = int(numero)
    print(num/numero2)
    print(lista[2])
except ZeroDivisionError:
    print("error de division")
except ValueError:
    print("error de conversion")
except Exception as e: # SOLO SI HAY ERROR
    print(e)
else: # SOLAMENTE SI EL BLOQUE TRY NO TUVO ERROR
    print("else")
finally: # SIEMPRE
    print("finalmente...")


print("fin")

"""

cadena = "15"
numb = 0
lista = []
try:
    print("asdasd")
    num = int(cadena)
    print(num/numb)
    a = lista[5]
except ZeroDivisionError as e:
    print("no se puede ....por 0")
except ValueError:
    print('error de conversion')
except Exception as e:
    print(e.message())
else:
    print("else")
finally:
    print("finalmente...")
"""


class Persona(object):

    def __init__(self, nom=None, ape=None, dni=None):
        self.__dni = dni
        self.__nom = nom
        self.__ape = ape

    @property
    def ape(self):
        return self.__ape

    @ape.setter
    def ape(self, ape):
        self.__ape = ape

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni


class validarError(Exception):

    def __init__(self, campo):
        self.msg = "atributo de clase sin valor"
        self.campo = campo

    def __str__(self):
        return "Error en el campo " + self.campo +" "+self.msg

    def get_campo(self):
        if(self.campo == "apellido"):
            return 0
        elif(self.campo == "nombre"):
            return 1
        elif(self.campo == "dni"):
            return 2
        else:
            return -1

    def get_msg(self):
        return "Error en el campo " + self.campo +" "+ self.msg


def validar(p):
    try:
        if((p.ape is None) or (len(p.ape) == 0)):
            raise validarError("apellido")
        if((p.nom is None) or (len(p.nom) == 0)):
            raise validarError("nombre")
        if((p.dni is None) or (p.dni == 0)):
            raise validarError("dni")
    except validarError as e:
        print(e.get_msg())
        if e.get_campo() == 0:
            p.ape = input('ingrese apellido ')
        elif e.get_campo() == 1:
            p.nom = input('ingrese nombre ')
        elif e.get_campo() == 2:
            try:
                p.dni = int(input('ingrese dni '))
            except ValueError:
                print("el dni debe ser un campo numerico sin punto")
        validar(p)




p = Persona()
validar(p)

print(p.nom)
