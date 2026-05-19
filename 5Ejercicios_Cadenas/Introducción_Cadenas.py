
# Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
# Debe retornar las veces que la letra está incluida en el texto.

def letra_cadena(l , c):
    
    cont = 0

    for letra in c:
        if letra == l:
            cont += 1

    return cont

'''
cadena = input("Ingrese un texto: ")
while cadena.isdigit():
    cadena = input("Error.Números no admitidos. Reingresar: ")

letra = input("Ingrese la letra que quiere contar en el texto: ")
while letra.isdigit() or len(letra) != 1:
    letra = input("Error.Fuera de parámetro. Reingresar: ")

print(F"la letra {letra} se ha encontrado: {letra_cadena(letra, cadena)} veces")

'''

# Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.
# Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
# Si las posiciones no son válidas se debe informar.
 
def cadena_2(c, i1, i2):

    if i1 < 0 or i2 > len(c) or i1 >= i2:
        return "Error.Índices inválidos"
    
    return c[i1:i2]

'''
cadena = input("Ingrese un texto: ")
while cadena.isdigit():
    cadena = input("Error.Números no admitidos. Reingresar: ")


indice1 = input("Ingresar el primer índice: ")
while not indice1.isdigit() or int(indice1) < 0 :
    indice1 = input("Error.Fuera de parámetro. Reingresar: ")
indice1 = int(indice1)

indice2 = input("Ingresar el segundo índice: ")
while not indice2.isdigit() or int(indice2) > len(cadena) or int(indice2) <= indice1:
    indice2 = input("Error.Fuera de parámetro. Reingresar: ")
indice2 = int(indice2)

print(cadena_2(cadena, indice1, indice2))
'''

# Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.
# Se debe retornar el caracter en la posición indicada por el número si ésta es válida.


def char_at(c, n1):

    if n1 < 0 or n1 >= len(c):
        return "Error.Fuera de parámetro."
    
    return c[n1]


cadena = input("Ingrese un texto: ")
while cadena.isdigit():
    cadena = input("Error.Fuera de parámetro. Reingresar: ")

num = input("Ingrese la posición numérica del carácter que quiere devolver: ")
while not num.isdigit() or int(num) < 0 or int(num) > len(cadena):
    num = input("Error.Fuera de parámetro. Reingresar: ")
num = int(num)

print(char_at(cadena, num))


# **IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el
# <número de caracteres> - 1.