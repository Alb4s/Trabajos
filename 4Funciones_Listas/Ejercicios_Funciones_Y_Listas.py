# Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los
# guarde en una lista y la retorne. El programa principal debe invocar a la función y
# mostrar por pantalla el retorno.

def nombres_s():
    
    lista = list()

    for i in range(10):
        nombre = input("Ingresar nombre: ")
        lista.append(nombre)
    
    return lista

'''
nombres = nombres_s()
print(nombres)
'''

# Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida
# posición y número a guardar al usuario, lo guarde en una lista en la posición
# solicitada aleatoriamente y la retorne. El programa principal debe invocar a la
# función y mostrar por pantalla el retorno.

def lista_0():

    lista = [0] * 10

    posicion = input("Ingresar posición (0-9): ").strip()
    while not posicion.isdigit() or not (0 <= int(posicion) <= 9):
        posicion = input("Error.Fuera de parámetro. Reingresar: ").strip()
    posicion = int(posicion)

    numero = input("Ingresar número: ").strip()
    while not numero.isdigit():
        numero = input("Error.Fuera de parámetro. Reingresar: ").strip()
    numero = int(numero)

    lista[posicion] = numero

    return lista

'''
print(lista_0())
'''

# Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango
# especificado, validar los números solicitados dentro de ese rango, guardar en una
# lista y retornarla. El programa principal debe invocar a la función y mostrar por
# pantalla el retorno.

def lista_1():
    
    lista = []

    minimo = input("Ingresar mínimo: ").strip()
    while not minimo.lstrip('-').isdigit():
        minimo = input("Error.Fuera de parámetro. Reingresar: ").strip()
    minimo = int(minimo)

    maximo = input("Ingresar máximo: ").strip()
    while not maximo.lstrip('-').isdigit() or int(maximo) < minimo:
        maximo = input("Error.Fuera de parámetro. Reingresar: ").strip()
    maximo = int(maximo)

    for i in range(10):
        num = input(f"Ingresar número {i+1}: ").strip()
        while not num.lstrip('-').isdigit() or not (minimo <= int(num) <= maximo):
            num = input(f"Error.Reingresar número {i+1}: ").strip()
        lista.append(int(num))
    
    return lista

'''
print(lista_1())
'''

# Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números
# y un número especificado. La misma debe buscar el número especificado en la lista
# y retornar “True” si existe.

def lista_2(lista, numero):

    for elemento in lista:
        if elemento == numero:
            return True
    
    return False

'''
numeros = [3, 7, 1, 9, 5]

print(lista_2(numeros, 7))
print(lista_2(numeros, 4))
'''

# Ejercicio 5: Dadas las siguientes listas:
# Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
# ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
# edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
# Desarrollar una función que reciba por parámetro la lista de edades, busque a las
# personas de menor edad (puede ser más de una) y las retorne. El programa
# principal deberá mostrar nombre y edad de los menores.

def lista_menores(edades):
    menores = min(edades)
    lista = []

    for i in range(len(edades)):
        if edades[i] == menores:
            lista.append(i)

    return lista

'''
nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]

edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

menor = lista_menores(edades)

for i in menor:
    print(nombres[i], edades[i])
'''

# Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo
# listas_personas.py. Importar los nombres a una lista. Realizar una función que
# muestre los mismos.

from Listas_pais import nombres_pais

def mostrar_nombres(lista):
    for nombre in lista:
        print(nombre)

'''
mostrar_nombres(nombres)
'''

# Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de
# compras on-line recientemente lanzado al mercado para ello necesita un programa
# que le permita acceder a los datos relevados.
# Realizar una función con el siguiente Menú de Opciones:
# 1-Importar listas
# 2-Listar los datos de los usuarios de México
# 3-Listar los nombre, mail y teléfono de los usuarios de Brasil
# 4-Listar los datos del/los usuario/s más joven/es
# 5-Obtener un promedio de edad de los usuarios
# 6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
# 7-Listar los datos de los usuarios de México y Brasil cuyo código postal
# sea mayor a 8000
# 8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40
# años.
import sys
sys.path.append('6ejercicios_ordenamientos')
import funciones
from Listas_pais import nombres_pais, telefonos,  mails, address, postalZip, region, country, edades_pais
import Funciones_de_Ejercicios

def menu():
    print("1. Listar usuarios México")
    print("2. Listar nombre, mail y teléfono de Brasil")
    print("3. Usuario/s más joven/es")
    print("4. Promedio de edad")
    print("5. Mayor edad de Brasil")
    print("6. México y Brasil con PZ > 8000")
    print("7. Italianos mayores a 40")
    print("8. Ordenar México")
    print("9. Ordenar jóvenes")
    print("10. Ordenar Brasil y México con PZ > 8000")
# Ejercicio 8: Crear una función para cada opción de menú. AHORA TAMBIÉN PARA ORDENAMIENTO!!!!!!

menu()
op = input("Elegir opción: ")
while not op.isdigit():
    op = input("Error.Fuera de parámetro. Reingresar: ")
op = int(op)

while op < 1 or op > 10:
    op = int(input("Error.Fuera de parámetro. Reingresar: "))

print()

if op == 1:
    Funciones_de_Ejercicios.U_Mexico(nombres_pais, edades_pais, mails, telefonos, country)

elif op == 2:
    Funciones_de_Ejercicios.U_Brasil(nombres_pais, mails, telefonos, country)

elif op == 3:
    Funciones_de_Ejercicios.mas_joven(nombres_pais, edades_pais)

elif op == 4:
    Funciones_de_Ejercicios.promedio_edades(edades_pais)

elif op == 5:
    Funciones_de_Ejercicios.mayor_brasil(nombres_pais, edades_pais, country)

elif op == 6:
    Funciones_de_Ejercicios.mexico_brasil_PZ(nombres_pais, country, postalZip)

elif op == 7:
    Funciones_de_Ejercicios.italianos_mayores(nombres_pais, mails, telefonos, country, edades_pais)

elif op == 8:
    resultado = funciones.ordenar_mexico(nombres_pais, edades_pais, mails, telefonos, country)
    for i in resultado:
        print(i[0], i[1], i[2], i[3])

elif op == 9:
    resultado = funciones.ordenar_menor(edades_pais, nombres_pais)
    for i in resultado:
        print(i[0], i[1])

elif op == 10:
    resultado = funciones.postal_zip(nombres_pais, edades_pais, country, postalZip)
    for i in resultado:
        print(i[0], i[1], i[2], i[3])

print()
# Ejercicio 9: Desarrollar las funciones en una biblioteca.

#""""""""hecho"""""""""