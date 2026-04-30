# Enunciado/s:
# Tabla de Posiciones de Torneo de Ping-Pong
# Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.
# Los datos que se cargarán son:
# Nombre del jugador
# Edad (validar)
# Cantidad de puntos (validar-número entero positivo, hasta 60).
# Número de partidos ganados (validar-número entero positivo, hasta 35).
# Tipo de saque ("plano", "liftado", "cortado")
# Categoría ("elite", "experto", "avanzado")
# Se necesita saber
# Tema A:
# 1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
# inclusive.
# 2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
# 3-Porcentaje de jugadores de categoría "experto".
# 4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
# 5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”.

cont_jugadores = 0

cont_elite_plano_19_25 = 0

menor = None
nombre_menor_Edad = ""
categoria_menor_edad = ""

cont_experto = 0

suma_edad_avanzado = 0
cont_avanzado = 0

cont_saque_elite_plano = 0
cont_saque_elite_liftado = 0
cont_saque_elite_cortado = 0

while True:
    
    nombre = input("Nombre del jugador: ")

    edad = int(input("Ingresar edad: "))
    while edad <= 0:
        edad = int(input("Error. Edad invalida. Reingresar: "))
    
    puntos = int(input("Puntos (0 a 60): "))
    while puntos < 0 or puntos > 60:
        puntos = int(input("Error. Puntos fuera de rango. Reingresar: "))
    
    partidos_ganados = int(input("Partidos ganados (0 a 35): "))
    while partidos_ganados < 0 or partidos_ganados > 35:
        partidos_ganados = int(input("Error. cantidad inválida. Reingresar: "))
    
    saque = input("Tipo de saque (Plano/Liftado/Cortado): ").lower().strip()
    while saque not in ["plano", "liftado", "cortado"]:
        saque = input("Error. Fuera de parametro. Reingresar").lower().strip()

    categoria = input("Categoría (Elite/Experto/Avanzado): ").lower().strip()
    while categoria not in ["elite", "experto", "avanzado"]:
        categoria = input("Error. Fuera de parametro. Reingresar").lower().strip()

    
    cont_jugadores += 1



    if categoria == "elite" and saque == "plano" and 19 <= edad <= 25:
        cont_elite_plano_19_25 += 1
    
    if puntos > 50:
        if menor is None or edad < menor:
            menor = edad
            nombre_menor_Edad = nombre
            categoria_menor_edad = categoria
    
    if categoria == "experto":
        cont_experto += 1

    if categoria == "avanzado":
        cont_avanzado += 1
        suma_edad_avanzado += edad
    
    if categoria == "elite":
        if saque == "plano":
            cont_saque_elite_plano += 1
        
        elif saque == "liftado":
            cont_saque_elite_liftado += 1
        
        else:
            cont_saque_elite_cortado += 1
    

    rta = input("¿Continuar? (Si/No): ").lower().strip()
    if rta == "no":
        break



print(
                  "---------Resultados---------","\n",

    f"1) Elite con saque plano entre 19 y 25: {cont_elite_plano_19_25}"
)

if nombre_menor_Edad == "":
    print("2) Jugador menor edad con +50 puntos: No hay Jugadores")
else:
    print(f"2) Jugador menor edad con +50 puntos: {nombre_menor_Edad} - {categoria_menor_edad}")



if cont_jugadores > 0:
    porcentaje_experto = (cont_experto * 100) / cont_jugadores

else:
    porcentaje_experto = 0

print(f"3) Porcentaje expertos: {porcentaje_experto:.2f}%")

if cont_avanzado > 0:
    promedio_avanzado = suma_edad_avanzado / cont_avanzado

else:
    promedio_avanzado = 0

print(f"4) promedio edad avanzado: {promedio_avanzado:.2f}")

max_saque = max(cont_saque_elite_plano, cont_saque_elite_cortado, cont_saque_elite_liftado)

if max_saque == cont_saque_elite_plano:
    print("5) Saque más usado: Plano")
elif max_saque == cont_saque_elite_cortado:
    print("5) Saque más usado: Cortado")
else:
    print("5) Saque más usado: Liftado")