from colorama import Fore, Style, init

init()

# 1. Realizar una función recursiva que calcule la suma de los primeros números naturales:

def naturales_r(n):

    if n == 0:
        return 0
    
    return n + naturales_r(n - 1)

'''
print(naturales_r(10))
'''

# 2. Realizar una función recursiva que calcule la potencia de un número:

def potencia_r(n, e):

    if e == 0:
        return 1
    
    return n * potencia_r(n, e - 1)

'''
num = input("Ingrese un número: ")
while not num.isdigit():
    num = input("Error.Fuera de parámetro. Reingresar: ")
num = int(num)

num2 = input("Ingrese un exponente para número: ")
while not num2.isdigit():
    num2 = input("Error.Fuera de parámetro. Reingresar: ")
num2 = int(num2)


print(potencia_r(num, num2))
'''

# 3. Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

def digitos_r(n):

    if n == 0:
        return 0
    
    return (n % 10) + digitos_r(n // 10)

'''
num = input("Ingresar un número para sumar sus digitos: ")
while not num.isdigit():
    num = input("Error.Fuera de parámetro. Reingresar: ")
num = int(num)

print(digitos_r(num))
'''

#4

def fibonacci(numero:int)->int:
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    
    return fibonacci(numero - 1) + fibonacci(numero - 2)


numero = input("Ingresar un entero al cuál se le calculará Fibonacci: ")
while not numero.isdigit():
    numero = input("Error.Fuera de parámetro. Reingresar: ")
numero = int(numero)

for i in range (numero + 1):
    print(Fore.LIGHTCYAN_EX, fibonacci(i))