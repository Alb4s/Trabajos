#1. Mostrar los números ascendentes desde el 1 al 10---------------------------------------------------------------#
for i in range(0,1):
   print(i)

#2. Mostrar los números descendentes desde el 10 al 1--------------------------------------------------------------#
for i in range(10,0,-1):
    print(i)


#3. Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.-------------------------------------#
num = int(input("Ingrese un número: "))

for i in range(num + 1):
    print(i)

#4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:-----#

#5 x 0 = 0
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15 …

num = int(input("Ingrese un número: "))

for i in range(11):
    print(f"{num} x {i} = {num * i}")

#5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.-#
suma = 0
cont = 0

for i in range(10):
    num = int(input("Ingresar un número: "))

    if num == 0:
        break

    suma += num

    cont += 1

if cont > 0:
    print("Suma",suma,"\n",
          "promedio", suma / cont
    )


#6. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)-------------------------------------------------------#
for i in range(1,11):
    if i % 3 == 0:
        print(i)

#7. Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
for i in range(2, 51, 2):
        print(i)
#8. Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:-#
num = int(input("Ingresar número: "))

for i in range(num + 1):
    for j in range(1, i + 1):
        print(j, end = "")

    print()

#9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.-#
num = int(input("Ingresar un número: "))

cont = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        cont += 1

print("Cantidad de divisores", cont)


#10.Ingresar un número. Determinar si el número es primo o no.-------------------------------------------------------#
num = int(input("Ingresar un número: "))

cont = 0

for i in range(1, num + 1):
    if num % i == 0:
        cont += 1

if cont == 2:
    print("Primo")
else:
    print("No primo")


#11.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.-#
num = int(input("Ingresar un número: "))

cont_p = 0

for n in range(2, num + 1):
    divisores = 0

    for i in range (1, n + 1):
        if n % i == 0:
            divisores += 1

    if divisores == 2:
        print(n)
        cont_p += 1

print(f"Se encontraron {cont_p} números primos")