from colorama import Fore, Style, init

init()

#1- Calcular el importe total bruto sin descuentos.
#2- Calcular el importe total final con todos los descuentos aplicados.
#3- Informar la venta más cara hecha con tarjeta.
#4- Calcular el promedio de precio unitario de todas las ventas.
#5- Informar cuál fue la forma de pago más utilizada.

ventas = 0

total_bruto = 0
total_unidades = 0
total_final = 0

suma_unitarios = 0

efectivo = 0
tarjeta = 0
transferencia = 0

tarjeta_mayor = 0
tipo_mayor = 0
cantidad_mayor = 0
precio_mayor = 0


while ventas < 25:

    print(f"compra N°",ventas + 1)


    tipo = input(f"Ingrese el tipo de producto, {Fore.LIGHTRED_EX}Alimento{Fore.WHITE}/{Fore.LIGHTYELLOW_EX}Limpieza{Fore.WHITE}/{Fore.LIGHTMAGENTA_EX}Perfumeria{Fore.RESET}: ").lower().strip()
    
    cantidad = int(input("Ingrese la cantidad de unidades (entre 1 y 20) : "))
    
    precio_unidad = float(input("Ingrese el precio por unidad: "))
    
    forma_pago = input(f"Ingrese el método de pago, {Fore.GREEN}Efectivo{Fore.WHITE}/{Fore.BLUE}Tarjeta{Fore.WHITE}/{Fore.CYAN}Transferencia{Fore.RESET}: ").lower().strip()


    if cantidad < 1 or cantidad > 20:
        print("Cantidad inválida")
        continue

    if precio_unidad <= 0:
        print("Error: El precio debe ser mayor a 0")
        continue
    
    if tipo not in ["alimento","limpieza","perfumeria"]:
        print("Tipo de producto inválido")
        continue
    
    if forma_pago not in ["efectivo","tarjeta","transferencia"]:
        print("Forma de pago inválida")
        continue


    importe_venta = cantidad * precio_unidad
    total_bruto += importe_venta

    total_unidades += cantidad
    
    subtotal = importe_venta



    if forma_pago == "efectivo":
        subtotal *= 0.95
        #descuento individual por venta


    if forma_pago == "tarjeta":
        if importe_venta > tarjeta_mayor:

            tarjeta_mayor = importe_venta
            tipo_mayor = tipo
            cantidad_mayor = cantidad
            precio_mayor = precio_unidad


    if forma_pago == "efectivo":
        efectivo += 1
    elif forma_pago == "tarjeta":
        tarjeta += 1
    else:
        transferencia += 1
    

    suma_unitarios += precio_unidad

    total_final += subtotal

    ventas += 1


if total_unidades > 400:
    total_final *= 0.80
    
elif total_unidades > 200:
    total_final *= 0.90


promedio = suma_unitarios / 25

if efectivo > tarjeta and efectivo > transferencia:
    mas_usado = "Efectivo"

elif tarjeta > transferencia:
    mas_usado = "Tarjeta"
else:
    mas_usado = "transferencia"

#en caso de no haber ventas con tarjeta
if tarjeta_mayor == 0:
    print("No hubo ventas con tarjeta")

print(
"Total Bruto", total_bruto, "\n",
"Total Final", total_final, "\n",

"Venta más cara con tarjeta", tarjeta_mayor, "\n",
"Tipo más caro", tipo_mayor, "\n",
"Cantidad", cantidad_mayor, "\n",
"Precio unitario", precio_mayor, "\n",

"Promedio de precios unitarios", promedio, "\n",
"Forma de pago más usada", mas_usado
)