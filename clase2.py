
# COLECCIONES
# LISTAS DICCIONARIOS TUPLAS CONJUNTOS


l1 = [1, 2, 1.2, 10, 1.34]
l2 = [6, "hola", 4, 10, 0, 5]

l1 = l1 + l2
print(l1)
# l[2] = 4
'''
l.append(8)
l.insert(2, 3)
aux = l.pop(2)
l.remove(1)
l.reverse()
l.sort() # criterio cuando veamos clase

if("hola" in l):
    print("si")
else:
    print("no")


print(len(l))
print(l)
print(l[2])
print(aux)
'''
# for i in range(0, len(l)):
#    print(l[i])

# for elemento in l:
#    print(elemento)

# FUNCIONES


def sumar_y_resta(num1, num2, num3=None, num4=None):
    """Suma dos numeros."""
    print(num1)
    print(num2)
    print(num3)
    print(num4)
    return (num1 + num2), (num1 - num2), (num1 * num2)


s, r, p = sumar_y_resta(4, 6, num4=5)
print(s)
print(r)
print(p)

f = sumar_y_resta(4, 6, num4=5)
print('tipo de dato', type(f))
num = 15

ln = [1, 2, 3, 4]

ln.sort()


def prueba(n):
    n.append(5)


prueba(ln)
print(ln)


"""
a = "Hola"
if(a == "hola"):
    print("si")
else:
    print("no")
"""

# STRING

cad = "hola MunDo DESDE Python"
'''
print(len(cad))

print(cad.find("o"))

print(cad.lower())
print(cad.upper())
print(cad.title())
cad.title()

print(cad.strip())

l = cad.split()
print(l)

cad = "*"
cad = cad.join(l)
print(cad * 3)
'''
