# Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe como parámetro.--------------------------------#


def mostrador_n(numero):
    print(numero)

'''
num = int(input("Ingresar número: "))
mostrador_n(num)
'''

# Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne.--------------------------------#


def retornar_n():
    numero = int(input("Ingresar número: "))
    return numero

'''
num = retornar_n()
print(num)
'''

# Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La--------------------------------#
# función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
# programa principal realizando la invocación o llamada.

def par(numero):
    
    if numero % 2 == 0:
        return True
    else:
        return False

'''
num = int(input("Ingrese un número, se determinará si es par: "))
print(par(num))
'''

# Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 para que valide el número en--------------------------------#
# un rango determinado pasado por parámetro “desde”-“hasta”.

def pedir_num(desde, hasta):
    numero = int(input("Ingresar número: "))

    if desde <= numero <= hasta:
        return numero
'''
num = pedir_num(10, 50)
print(num)
'''
# Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la--------------------------------#
# función Restar en sus 4 combinaciones.
#  Restar1(int, int)->int:
#  Restar2()->int:
#  Restar3(int, int):
#  Restar4():

# Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor--------------------------------#
# solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
# dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
# por pantalla. Atención: pueden reutilizarse funciones ya creadas.

# Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2--------------------------------#
# los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la
# variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice
# la operación de dichos valores a través de una función. Mostrar el resultado por
# pantalla.