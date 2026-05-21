from colorama import Fore
import sys

from funciones import ordenar_listas, ordenar_listas_2, ordenar_listas_3, ordenar_mexico, ordenar_menor, postal_zip
from listas import Nombres, Edades, Materias, Puntos, Estudiantes, Apellidos, Nota
sys.path.append('4Funciones_Listas')
from Listas_pais import nombres_pais, telefonos,  mails, address, postalZip, region, country, edades_pais


print(f"{Fore.GREEN}---------------------------------------Ejercicio 1---------------------------------------{Fore.RESET}")
ejercicio1 = ordenar_listas(Nombres,Edades)
for par in ejercicio1:
    print(par)

print()


print(f"{Fore.GREEN}---------------------------------------Ejercicio 2---------------------------------------{Fore.RESET}")
ejercicio2 = ordenar_listas_2(Materias, Puntos)
for orden in ejercicio2:
    print(orden)

print()


print(f"{Fore.GREEN}---------------------------------------Ejercicio 3---------------------------------------{Fore.RESET}")
ejercicio3 = ordenar_listas_3(Estudiantes, Apellidos, Nota)
for asignatura in ejercicio3:
    print(asignatura)

print()

# Ejercicio 4: Una startup desea analizar las estadísticas de los usuarios de su sitio de
# compras on-line que recientemente han lanzado al mercado, para ello necesita un programa
# que le permita acceder a los datos relevados.
print(f"{Fore.GREEN}---------------------------------------Ejercicio 4---------------------------------------{Fore.RESET}")
ejercicio4 = ordenar_mexico(nombres_pais, edades_pais, mails, telefonos, country)
for mexico in ejercicio4:
    print(mexico)

print()

ejercicio4_2 = ordenar_menor(edades_pais, nombres_pais)
for menor in ejercicio4_2:
    print(menor)

print()

ejercicio4_3 = postal_zip(nombres_pais, edades_pais, country, postalZip)
for postal in ejercicio4_3:
    print(postal)

#DESARROLLÉ TODO LO QUE FALTA EN LA RECIÉN ACTUALIZADA "4Funciones_Listas"