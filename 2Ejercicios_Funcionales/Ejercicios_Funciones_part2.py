import unicodedata
# 1. Escribir una función que calcule el área de un rectángulo. La función recibe la base y
# la altura y retorna el área.

def area_rectangulo(B, H):
    Area = B * H
    return Area

'''
Base = input("Ingrese un número para Base: ")
while not Base.isdigit():
    Base = input("Error.Fuera de parámetro. Reingresar: ")
Base = int(Base)

Hight = input("Ingrese un número para Altura: ")
while not Hight.isdigit():
    Hight = input("Error. Fuera de parámetro. Reingresar: ")
Hight = int(Hight)

print(f"Área: {area_rectangulo(Base, Hight)}")
'''
# 2. Escribe una función que calcule el área de un círculo. La función debe recibir el radio
# como parámetro y devolver el área.

def area_cirulo(radio):
    pi = 3.1416
    return pi * radio ** 2

'''
radio = input("Ingrese el radio: ")
while not radio.replace('.', '', 1).isdigit():
    radio = input("Error.Fuera de parámetro. Reingresar")
radio = float(radio)

resultado = area_cirulo(radio)
print(f"Área: {resultado:.3f}")
'''
# 3. Crea una función que verifique si un número dado es par o impar. La función debe
# imprimir un mensaje indicando si el número es par o impar.

def par_impar(n):

    resultado = n % 2

    if resultado == 0:
        return "Par"
    else:
        return "Impar"

'''
num = input("Ingresar número: ")
while not num.isdigit():
    num = input("Error.Fuera de parámetro. Reingresar: ")
num = int(num)

print(f"tú numero es {par_impar(num)}")
'''

# 4. Crea una función que verifique si un número dado es par o impar. La función retorna
# True si el número es par, False en caso contrario.

def par_impar2(n):

    resultado = n % 2

    if resultado == 0:
        return True
    else:
        return False

'''
num = input("Ingresar número: ")
while not num.isdigit():
    num = input("Error.Fuera de parámetro. Reingresar: ")
num = int(num)

print(f"¿es tú número par? {par_impar2(num)}")
'''

# 5. Define una función que encuentre el máximo de tres números. La función debe
# aceptar tres argumentos y devolver el número más grande.

def maximo_tres(n1, n2, n3):

 return max(n1, n2, n3)           # if n1 >= n2 and n1 >= n3:
                                #     return n1
                                # elif n2 >= n3:
                                #     return n2
                                # else:
                                #     return n3

def validar_entero(msg):
    num = input(msg)
    while not num.isdigit():
        num = input("Error.Fuera de parámetro. Reingresar: ")
    return int(num)
'''
num1 = validar_entero("Ingresar número 1: ")

num2 = validar_entero("Ingresar número 2: ")

num3 = validar_entero("Ingresar número 3: ")

print(f"El número más grande es: {maximo_tres(num1, num2, num3)}")
'''

# 6. Diseña una función que calcule la potencia de un número. La función debe recibir la
# base y el exponente como argumentos y devolver el resultado.

def exponencial(n1, e1):

    potencia = n1 ** e1

    return potencia

'''
base = validar_entero("Ingresar la base a que hacerle potencia: ")

exponente = validar_entero("Ingresar la potencia: ")

print(f"La potencia de {base}^{exponente} es: {exponencial(base, exponente)}")
'''

# 7. Crear una función que reciba un número y retorne True si el número es primo, False
# en caso contrario.

def primo(n1):

    if n1 <= 1:
        return False
    
    for i in range(2, int(n1 ** 0.5) + 1):
        if n1 % i == 0:
            return False

    return True

'''
num = validar_entero("Ingresa número para saber si es primo: ")

print(f"{num} ¿es primo? {primo(num)}")
'''

# 8. Crear una función que (utilizando la función del punto 11 de la guía de For),
# muestre todos los números primos comprendidos entre entre la unidad y un número
# ingresado como parámetro. La función retorna la cantidad de números primos
# encontrados.

def primos_hasta(n):
    contador = 0

    for num in range(2, n + 1):
        es_primo = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break

        if es_primo == True:
            print(num)
            contador += 1
    
    return contador

'''
num = validar_entero("Ingresar número: ")
cantidad = primos_hasta(num)

print(f"Cantidad de números primos encontrados: {cantidad}")
'''

# 9. Crear una función que imprima la tabla de multiplicar de un número recibido como
# parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir
# el rango de multiplicación. Por defecto es del 1 al 10.

def tabla(n1, inicio = 1, fin = 10):

    for i in range(inicio, fin + 1):
        print(f"{n1} x {i} = {n1 * i}")
    
'''
num = validar_entero("Ingresar un número: ")

rango = input("¿Desea establecer el rango? (Si/No): ").lower().strip()
while rango not in ["si", "no", "s", "n"]:
    rango = input("Error.Fuera de parámetro. Reingresar: ").lower().strip()

if rango in ["si", "s"]:
    inicio = validar_entero("Ingrese el inicio: ")
    fin = validar_entero("Ingresar fin: ")
    tabla(num, inicio, fin)
else:
    tabla(num)
'''

# 10. Crear una función que le solicite al usuario el ingreso de un número entero y lo 
# retorne.

##Arreglo para punto 13.

def p_entero(msg = "Ingrese un número entero: ", minimo = None, maximo = None):

    while True:
        num = input(msg)

        if num.lstrip("-").isdigit():
            num = int(num)
            if (minimo == None or num >= minimo) and (maximo == None or num <= maximo):
                return num
            
        print("Error.Valor inválido.")


'''
numero = p_entero()

print(numero)
'''

# 11. Crear una función que le solicite al usuario el ingreso de un número flotante y lo
# retorne.

##Arreglo para punto 13.

def p_float(msg = "Ingresar un número flotante: ", minimo = None, maximo = None):

    while True:
        try:
            num = float(input(msg))
            if (minimo == None or num >= minimo) and (maximo == None or num <= maximo):
                return num
            
        except ValueError:
            pass
        print("Error.Valor inválido.")
    

'''
numero = p_float()

print(numero)
'''

# 12. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.

##Arreglo para punto 13.

def p_string(msg = "Ingresar una cadena: ", allow_blank = False, allow_space = True):

    while True:
        texto = input(msg)

        if not allow_space and "" in texto:
            print("Error.Sin espacios.")
            continue

        texto = texto.strip()


        if texto != "" or allow_blank:
            return texto

        print("Error.Texto vacío.")
    

'''
cadena = p_string()

print(cadena)
'''

# 13. Especializar las funciones del punto 10, 11, 12 para hacerlas reutilizables. Agregar
# validaciones.

'''

hecho

'''