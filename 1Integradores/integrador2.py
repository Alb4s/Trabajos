# UTN Technologies, una reconocida software factory se encuentra en la búsqueda
# de ideas para su próximo desarrollo en Python, que promete revolucionar el
# mercado.

# Las posibles aplicaciones son las siguientes:
# ● Inteligencia artificial (IA),
# ● Realidad virtual/aumentada (RV/RA),
# ● Internet de las cosas (IOT)
# Para ello, la empresa realiza entre sus empleados una encuesta, con el
# propósito de conocer ciertas métricas.

# A) Los datos a ingresar por cada empleado encuestado son:
# ● nombre del empleado
# ● edad (no menor a 18)
# ● género (Masculino - Femenino - Otro)
# ● tecnologia (IA, RV/RA, IOT)

# B) Cargar por terminal 10 encuestas.

# C) Determinar:
# 1. Cantidad de empleados de género masculino que votaron por IOT o IA,
# cuya edad esté entre 25 y 50 años inclusive.

# 2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
# género no sea Femenino o su edad se encuentre entre los 33 y 40.

# 3. Nombre y tecnología que votó, de los empleados de género masculino con
# mayor edad de ese género.

cont1 = 0
cont2 = 0

flag_masc = True


for i in range(10):

    nombre = input("Ingresar nombre: ")

    edad = int(input("Ingresar edad (NO MENORES DE EDAD): "))
    while edad < 18:
        edad = int(input("Error. Reingrese edad: "))

    genero = input("Ingresar género (Masculino, Femenino, Otro): ").lower().strip()
    while genero not in ["masculino", "femenino", "otro"]:
        genero = input("Error. Ingrese nuevamente: ")

    tecnologia = input("Tipo de tecnología (IA/RVRA/IOT): ").lower().strip()
    while tecnologia not in ["ia","rvra", "iot"]:
        tecnologia = input("Error. Ingrese nuevamente")

    if genero == "masculino" and (tecnologia == "iot" or tecnologia == "ia") and edad >= 25 and edad <= 50:
        cont1 += 1

    if tecnologia != "ia" and (genero != "femenino" or (edad >= 33 and edad <= 40)):
        cont2 += 1

    if genero == "masculino":

        if flag_masc or edad > mayor_edad:
            mayor_edad = edad
            nombre_mayor = nombre
            tecnologia_mayor = tecnologia
            flag_masc = False


porcentaje = cont2 * 100 / 10

print(
    "Solicitud 1:", cont1,"\n",
    "Solicitud 2:", porcentaje,"%","\n",
    "Solicitud 3:", nombre_mayor, tecnologia_mayor
)
