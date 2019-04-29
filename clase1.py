
print("hola mundo")

# texto = input("ingrese una frase")

texto = 'hola'

numero = 220
print(type(numero))

numero = texto
print(type(numero))

# print(type(texto))

# TIPOS DE DATOS entero float string bool
# OPERADORES ARITMETICOS + - * / // % **

print(23 + 4)
print(23 - 4)
print(23 * 4)
print(23 / 4)
print(23 // 4)
print(5 % 2)
print(3 ** 3)
print(2 ** 5)

# ESTRUCTURAS DE control
# OPERADORES DE CONTROL > < >= <= == !=
# OPERADORES LOGICOS AND OR
# if if-else elif

numero = 9

if(numero >= 1 and numero <= 10):
    print("esta comprendido")
else:
    print("no esta comprendido")


if(numero > 10):
    print("es mayor")
elif(numero == 10):
    print("es igual")
else:
    print("es menor")


# CICLOS  for  while

# CONVERTIR int() str() float() bool()

for i in range(1, 6):
    a1 = input("ingrese un numero")
    print(a1)

i = 1
while(i < 6):
    a1 = input("ingrese un numero for while")
    print(a1)
    i += 1


numero = 5
while(numero != "0" and numero != "10"):
    numero = input("ingrese un numero while")
    print(numero)


print("fin")
