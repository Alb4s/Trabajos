from colorama import Fore
# Ejercicio 1: Dadas las siguientes listas:
# Nombres =
# ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Anto
# nio", "Eugenia", "Soledad", "Mario", "Mariela"]
# Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
# Desarrollar una función que realice el ordenamiento de las listas por nombre de
# manera ascendente.

from funciones import ordenar_listas, ordenar_listas_2, ordenar_listas_3
from listas import Nombres, Edades, Materias, Puntos, Estudiantes, Apellidos, Nota
print(f"{Fore.GREEN}---------------------------------------Ejercicio 1---------------------------------------{Fore.RESET}")
ejercicio1 = ordenar_listas(Nombres,Edades)
for par in ejercicio1:
    print(par)

print()

# Ejercicio 2: Dadas las siguientes listas:
# Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias
# Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
# "Base de Datos", "Ergonomia", "Naturaleza"]
# Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
# Desarrollar una función que realice el ordenamiento de las listas por nombre de
# manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera
# descendente.

print(f"{Fore.GREEN}---------------------------------------Ejercicio 2---------------------------------------{Fore.RESET}")
ejercicio2 = ordenar_listas_2(Materias, Puntos)
for orden in ejercicio2:
    print(orden)

print()

# Ejercicio 3: Dadas las siguientes listas:
# Estudiantes =
# ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Anto
# nio", "Eugenia", "Soledad", "Mario", "María"]
# Apellidos =
# [“Sosa”,”Gutierrez”,”Alsina”,”Martinez”,”Sosa”,”Ramirez”,”Perez”,”Lopez”,”Arregui”
# ,”Mitre”,”Andrade”,”Loza”,”Antares”,”Roca”,”Perez”]
# Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
# Desarrollar una función que realice el ordenamiento de las listas por apellido de
# manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
# ascendente, si el nombre también es el mismo, debe ordenar por nota de manera
# descendente.

print(f"{Fore.GREEN}---------------------------------------Ejercicio 3---------------------------------------{Fore.RESET}")
ejercicio3 = ordenar_listas_3(Estudiantes, Apellidos, Nota)
for asignatura in ejercicio3:
    print(asignatura)

# Ejercicio 4: Una startup desea analizar las estadísticas de los usuarios de su sitio de
# compras on-line que recientemente han lanzado al mercado, para ello necesita un programa
# que le permita acceder a los datos relevados.