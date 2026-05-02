import unicodedata

# Ejercicio 1: Registro de internaciones en un hospital
# Un hospital registra una cantidad indeterminada de internaciones en un día.
# Por cada paciente se ingresan los siguientes datos:
# ● Nombre del paciente
# ● Edad (entre 0 y 100)
# ● Tipo de atención (urgencia, control, cirugía)
# ● Cantidad de días internado (entre 1 y 60)
# ● Costo por día (mayor a 0)
# ● Sexo (F, M, NB)
# ● Tiene obra social (sí/no)
# ● Forma de pago (efectivo, tarjeta, transferencia)
# Todos los datos deben ser validados.
# Consideraciones:
# ● Si el paciente tiene obra social, se aplica un descuento del 20% sobre el costo de su
# internación.
# ● Si la cantidad total de días acumulados supera los 500, se aplica un descuento
# general del 10% sobre el total bruto.

# Se pide:
# a. Total bruto recaudado por internaciones. Luego, total final con descuentos aplicados.
# b. Cantidad de pacientes por tipo de atención.
# c. El tipo de atención con mayor cantidad de días acumulados.
# d. El nombre del paciente con mayor costo total de internación.
# e. El promedio de costo por día de todos los pacientes.
# f. Qué forma de pago fue la más utilizada.
# g. Cuántos pacientes tienen más de 10 días de internación.


def Remover_Tíldes(texto):
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

total_bruto = 0
total_dias = 0

cont_urgencia = 0
cont_control = 0
cont_cirugia = 0

dias_urgencia = 0
dias_control = 0
dias_cirugia = 0

max_costo = None
nombre_max = ""

suma_costos = 0
contador_pacientes = 0

cont_efectivo = 0
cont_tarjeta = 0
cont_transferencia = 0

cont_mas_10 = 0

while True:

    Name = input("Ingrese su nombre: ").strip()
    while not Name.replace(" ", "").isalpha():
        Name = input("Error. Solo letras. Reingresar: ").strip()

    Age = input("Ingrese su edad (0-100): ").strip()
    while not Age.isdigit() or int(Age) < 0 or int(Age) > 100:
        Age = input("Error.Valor inválido. Reingresar: ").strip()
    Age = int(Age)

    Tipo_Atencion = input("Ingrese que tipo de atención debe recibir (Urgencia/Control/Cirugía): ").lower().strip()
    Tipo_Atencion = Remover_Tíldes(Tipo_Atencion)
    while Tipo_Atencion not in ["urgencia","control","cirugia"]:
        Tipo_Atencion = input("Error.Tipo inválido. Reingresar: ").lower().strip()
        Tipo_Atencion = Remover_Tíldes(Tipo_Atencion)
    
    Dias = input("Ingrese la cantidad de días que estará internado (1-60): ").strip()
    while not Dias.isdigit() or int(Dias) < 1 or int(Dias) > 60:
        Dias = input("Error.Valor inválido. Reingresar: ").strip()
    Dias = int(Dias)

    Costo_dia = input("Ingresar el costo por día: ").strip()
    while not Costo_dia.isdigit() or int(Costo_dia) <= 0:
        Costo_dia = input("Error.Deberá ser mayor a 0. Reingresar: ").strip()
    Costo_dia = int(Costo_dia)

    Sexo = input("Ingrese su género (F/M/NB): ").lower().strip()
    while Sexo not in ["f","m","nb"]:
        Sexo = input ("Error.Género inválido. Reingresar: ").lower().strip()
    
    Obra_social = input("Tiene obra social (Si/No): ").lower().strip()
    Obra_social = Remover_Tíldes(Obra_social)
    while Obra_social not in ["si","no","s","n"]:
        Obra_social = input("Error.Solo Si/No: ").lower().strip()
        Obra_social = Remover_Tíldes(Obra_social)
    
    if Obra_social == "s":
        Obra_social = "si"
    elif Obra_social == "n":
        Obra_social = "no"
    
    if Dias > 10:
        cont_mas_10 += 1
    
    Forma_pago = input("Ingresar forma de pago (Efectivo/Tarjeta/Transferencia): ").lower().strip()
    Forma_pago = Remover_Tíldes(Forma_pago)
    while Forma_pago not in ["efectivo","tarjeta","transferencia"]:
        Forma_pago = input("Error.Forma de pago inválida. Reingresar: ").lower().strip()
        Forma_pago = Remover_Tíldes(Forma_pago)
    
    if Obra_social == "si":
        Descuento = 0.20
    else:
        Descuento = 0
    
    if Tipo_Atencion == "urgencia":
        cont_urgencia += 1
    elif Tipo_Atencion == "control":
        cont_control += 1
    else:
        cont_cirugia += 1
    
    if Tipo_Atencion == "urgencia":
        dias_urgencia += Dias
    elif Tipo_Atencion == "control":
        dias_control += Dias
    else:
        dias_cirugia += Dias
    
    if Forma_pago == "efectivo":
        cont_efectivo += 1
    elif Forma_pago == "tarjeta":
        cont_tarjeta += 1
    else:
        cont_transferencia += 1


    suma_costos += Costo_dia
    contador_pacientes += 1
    

    costo_total = Dias * Costo_dia * (1 - Descuento)

    if max_costo is None or costo_total > max_costo:
        max_costo = costo_total
        nombre_max = Name

    total_bruto += costo_total
    total_dias += Dias


    ans = input("¿Continuar? (Si/No): ").lower().strip()
    while ans not in ["si","no"]:
        ans = input("Error.Solo Si/No. Reingresar: ").lower().strip()
    
    if ans == "no":
        break

promedio = suma_costos / contador_pacientes

if total_dias > 500:
    total_final = total_bruto * 0.90
else:
    total_final = total_bruto

if cont_efectivo > cont_tarjeta and cont_efectivo > cont_transferencia:
    pago_mas_usado = "efectivo"
elif cont_tarjeta > cont_transferencia:
    pago_mas_usado = "tarjeta"
else:
    pago_mas_usado = "transferencia"

if dias_urgencia > dias_control and dias_urgencia > dias_cirugia:
    tipo_mas_dias = "urgencia"
elif dias_control > dias_cirugia:
    tipo_mas_dias = "control"
else:
    tipo_mas_dias = "cirugia"


print(
    'Total bruto:', total_bruto,"\n",
    'Total final:', total_final,"\n",
    
    '--Pacientes por tipo--',"\n",
    'Urgencias:', cont_urgencia,"\n",
    'Control:', cont_control,"\n",
    'Cirugía:', cont_cirugia,"\n",
    
    'Tipo con más días:', tipo_mas_dias,"\n",
    'Paciente con mayor costo:', nombre_max,"\n",
    'Promedio costo por día:', promedio,"\n",
    'Forma de pago más usada:', pago_mas_usado,"\n",
    'Pacientes con más de 10 días:', cont_mas_10,"\n",
)
#---------------------------------------------------------------------------------------------------------#
# Ejercicio 2: Registro de alquiler de vehículos
# Una empresa registra alquileres de autos durante un período. No se sabe cuántos registros
# habrá.
# Por cada alquiler se ingresan:
# ● Nombre del cliente
# ● Tipo de vehículo (auto, camioneta, moto)
# ● Cantidad de días de alquiler (entre 1 y 30)
# ● Precio por día (mayor a 0)
# ● Kilómetros recorridos (entre 0 y 5000)
# ● Forma de pago (efectivo, tarjeta, transferencia)
# ● Cliente frecuente (sí/no)
# Validar todos los datos.
# Consideraciones:
# ● Si el cliente es frecuente, tiene un descuento del 15% sobre el total del alquiler.
# ● Si el total de kilómetros acumulados supera los 20000 km, se aplica un recargo del
# 10% sobre el total bruto general.
# ● Las camionetas tienen un recargo del 20% sobre su costo individual.

# Se pide:
# a. Calcular el importe total bruto y el total final.
# b. El tipo de vehículo con mayor cantidad de alquileres.
# c. El nombre del cliente que más días alquiló en total.
# d. El promedio de kilómetros recorridos.
# e. Qué tipo de vehículo acumuló más kilómetros.
# f. Cuántos alquileres fueron pagados con tarjeta.
# g. El alquiler de mayor importe (indicar cliente y monto).

total_bruto_general = 0
total_final_general = 0
total_km = 0
contador_alquileres = 0

cont_auto = 0
cont_camioneta = 0
cont_moto = 0
cont_tarjeta = 0

km_auto = 0
km_camioneta = 0
km_moto = 0

max_dias = 0
cliente_max_dias = ""

max_importe = 0
cliente_max_importe = ""

while True:

    name = input("Ingrese su nombre: ").strip()
    while not name.replace(" ", "").isalpha():
        name = input("Error. Solo letras. Reingresar: ").strip()
    
    tipo_vehiculo = input("Tipo de vehículo (Auto/camioneta/moto)").lower().strip()
    while tipo_vehiculo not in ["auto","camioneta","moto"]:
        tipo_vehiculo = input("Error.Vehículo inválido. Reingresar: ").lower().strip()
    
    cantidad_dias = input("Ingrese los días que alquila el vehículo (1-30): ").strip()
    while not cantidad_dias.isdigit() or int(cantidad_dias) < 1 or int(cantidad_dias) > 30:
        cantidad_dias = input("Error.Cantidad inválida. Reingresar: ").strip()
    cantidad_dias = int(cantidad_dias)

    precio_dia = input("Ingrese el precio por día (mayor a 0): ").strip()
    while not precio_dia.isdigit() or int(precio_dia) <= 0:
        precio_dia = input("Error.Valor inválido. Reingresar: ").strip()
    precio_dia = int(precio_dia)

    km = input("Kilómetros recorridos (0-5000): ").strip()
    while not km.isdigit() or int(km) < 0 or int(km) > 5000:
        km = input("Error.Cantidad inválida. Reingresar: ").strip()
    km = int(km)

    forma_pago = input("Ingrese la forma de pago Efectivo/Tarjeta/Transferencia: ").lower().strip()
    forma_pago = Remover_Tíldes(forma_pago)
    while forma_pago not in ["efectivo","tarjeta","transferencia"]:
        forma_pago = input("Error.Forma de pago inválida. Reingresar: ").lower().strip()
        forma_pago = Remover_Tíldes(forma_pago)
    
    frecuente = input("Cliente frecuente (si/no): ").lower().strip()
    while frecuente not in ["si", "no"]:
        frecuente = input("Error. Reingresar: ").lower().strip()

    importe = cantidad_dias * precio_dia

    if tipo_vehiculo == "camioneta":
        importe *= 1.20
        cont_camioneta += 1
        km_camioneta += km
    elif tipo_vehiculo == "auto":
        cont_auto += 1
        km_auto += km
    else:
        cont_moto += 1
        km_moto += km

    if frecuente == "si":
        importe *= 0.85

    total_bruto_general += cantidad_dias * precio_dia
    total_final_general += importe
    total_km += km
    contador_alquileres += 1

    if forma_pago == "tarjeta":
        cont_tarjeta += 1

    if cantidad_dias > max_dias:
        max_dias = cantidad_dias
        cliente_max_dias = name

    if importe > max_importe:
        max_importe = importe
        cliente_max_importe = name

    seguir = input("¿Continuar? (si/no): ").lower().strip()
    if seguir != "si":
        break    

if total_km > 20000:
    total_final_general *= 1.10

if cont_auto > cont_camioneta and cont_auto > cont_moto:
    tipo_mas = "auto"
elif cont_camioneta > cont_moto:
    tipo_mas = "camioneta"
else:
    tipo_mas = "moto"


if contador_alquileres > 0:
    promedio_km = total_km / contador_alquileres
else:
    promedio_km = 0


if km_auto > km_camioneta and km_auto > km_moto:
    tipo_mas_km = "auto"
elif km_camioneta > km_moto:
    tipo_mas_km = "camioneta"
else:
    tipo_mas_km = "moto"

print(
    'Total bruto: ', total_bruto_general,"\n",
    'Total final: ', total_final_general,"\n",
    'Tipo mas alquilado: ',tipo_mas,"\n",
    'Cliente con mas días: ', cliente_max_dias,"\n",
    'Promedio km: ', promedio_km,"\n",
    'Tipo con mas km: ', tipo_mas_km,"\n",
    'Pagos con tarjeta: ', cont_tarjeta,"\n",
    'Mayor alquiler: ', cliente_max_importe, max_importe
)
#---------------------------------------------------------------------------------------------------------#
# Ejercicio 3: Registro de ventas en un gimnasio
# Un gimnasio registra ventas de planes a sus clientes. La cantidad de registros es
# indeterminada.
# Por cada venta se ingresan:
# ● Nombre del cliente
# ● Tipo de plan (mensual, trimestral, anual)
# ● Edad (entre 12 y 80)
# ● Precio del plan (mayor a 0)
# ● Forma de pago (efectivo, tarjeta, transferencia)
# ● Turno elegido (mañana, tarde, noche)
# ● Es alumno nuevo (sí/no)
# Validar todos los datos.

# Consideraciones:
# ● Si es alumno nuevo, tiene un descuento del 10%.
# ● Si se venden más de 50 planes en total, se aplica un descuento general del 5%.
# ● Los planes anuales tienen un recargo del 15%.
# Se pide:
# a. Total bruto y total final con descuentos/recargos.
# b. Cantidad de ventas por tipo de plan.
# c. El turno con más clientes.
# d. El nombre del cliente que pagó el plan más caro.
# e. El promedio de precios de planes vendidos.
# f. Qué forma de pago fue la más utilizada.
# g. Cuántos clientes son menores de 18 años.

total_bruto = 0
total_final = 0
contador_ventas = 0

cont_mensual = 0
cont_trimestral = 0
cont_anual = 0

cont_manana = 0
cont_tarde = 0
cont_noche = 0

cont_efectivo = 0
cont_tarjeta = 0
cont_transferencia = 0

cont_menores = 0

max_importe = 0
cliente_max = ""

while True:

    nombre = input("Nombre: ").strip()
    while not nombre.replace(" ", "").isalpha():
        nombre = input("Error. Reingresar: ").strip()

    plan = input("Plan (mensual/trimestral/anual): ").lower().strip()
    while plan not in ["mensual", "trimestral", "anual"]:
        plan = input("Error. Reingresar: ").lower().strip()

    edad = input("Edad (12-80): ").strip()
    while not edad.isdigit() or int(edad) < 12 or int(edad) > 80:
        edad = input("Error. Reingresar: ").strip()
    edad = int(edad)

    precio = input("Precio (>0): ").strip()
    while not precio.isdigit() or int(precio) <= 0:
        precio = input("Error. Reingresar: ").strip()
    precio = int(precio)

    pago = input("Pago (efectivo/tarjeta/transferencia): ").lower().strip()
    while pago not in ["efectivo", "tarjeta", "transferencia"]:
        pago = input("Error. Reingresar: ").lower().strip()

    turno = input("Turno (mañana/tarde/noche): ").lower().strip()
    while turno not in ["mañana", "tarde", "noche"]:
        turno = input("Error. Reingresar: ").lower().strip()

    nuevo = input("Alumno nuevo (si/no): ").lower().strip()
    while nuevo not in ["si", "no"]:
        nuevo = input("Error. Reingresar: ").lower().strip()

    importe = precio

    if plan == "anual":
        importe *= 1.15
        cont_anual += 1
    elif plan == "mensual":
        cont_mensual += 1
    else:
        cont_trimestral += 1

    if nuevo == "si":
        importe *= 0.90

    total_bruto += precio
    total_final += importe
    contador_ventas += 1

    if turno == "mañana":
        cont_manana += 1
    elif turno == "tarde":
        cont_tarde += 1
    else:
        cont_noche += 1

    if pago == "efectivo":
        cont_efectivo += 1
    elif pago == "tarjeta":
        cont_tarjeta += 1
    else:
        cont_transferencia += 1

    if edad < 18:
        cont_menores += 1

    if importe > max_importe:
        max_importe = importe
        cliente_max = nombre

    seguir = input("¿Continuar? (si/no): ").lower().strip()
    if seguir != "si":
        break

if contador_ventas > 50:
    total_final *= 0.95

if cont_manana > cont_tarde and cont_manana > cont_noche:
    turno_mas = "mañana"
elif cont_tarde > cont_noche:
    turno_mas = "tarde"
else:
    turno_mas = "noche"

if cont_efectivo > cont_tarjeta and cont_efectivo > cont_transferencia:
    pago_mas = "efectivo"
elif cont_tarjeta > cont_transferencia:
    pago_mas = "tarjeta"
else:
    pago_mas = "transferencia"

if contador_ventas > 0:
    promedio = total_bruto / contador_ventas
else:
    promedio = 0

print('Total bruto:', total_bruto,"\n",
'Total final:', total_final,"\n",
'Ventas mensual:', cont_mensual,"\n",
'Ventas trimestral:', cont_trimestral,"\n",
'Ventas anual:', cont_anual,"\n",
'Turno con más clientes:', turno_mas,"\n",
'Cliente plan más caro:', cliente_max,"\n",
'Promedio precios:', promedio,"\n",
'Forma de pago más usada:', pago_mas,"\n",
'Menores de 18:', cont_menores
)