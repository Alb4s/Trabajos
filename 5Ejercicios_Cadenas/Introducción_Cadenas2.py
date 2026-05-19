from colorama import Fore

# 1) Crear una función que reciba como parámetro una cadena y determine la
# cantidad de vocales que hay de cada una (individualmente). La función
# retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
# la cantidad.

def vocales(c):

    matriz = [
        ["a", 0],
        ["e", 0],
        ["i", 0],
        ["o", 0],
        ["u", 0],
    ]

    for letra in (c).lower():
        if letra == "a":
            matriz[0][1] += 1
        
        elif letra == "e":
            matriz[1][1] += 1
        
        elif letra == "i":
            matriz[2][1] += 1
        
        elif letra == "o":
            matriz[3][1] += 1
        
        elif letra == "u":
            matriz[4][1] += 1

    return matriz

'''
cadena = input("Ingrese un texto: ")
permitidos = " .,;:¿?¡!()-@"
valido = True

for caracter in cadena:
    if not (caracter.isalpha() or caracter in permitidos):
        valido = False

while not valido:
    cadena =  input("Error.Sólo texto. Reingresar: ")
    valido = True

    for caracter in cadena:
        if not (caracter.isalpha() or caracter in permitidos):
            valido = False

resultado = vocales(cadena)

for fila in resultado:
    print(fila)
'''

# 2) Crear una función que reciba una cadena y un caracter. La función deberá
# devolver el índice en el que se encuentre la primera incidencia de dicho
# caracter, o -1 en caso de que no esté.


def buscar_caracter(text, char):
    
    for i in range(len(text)):
        
        if text[i] == char:
            return i
        
    return -1

'''
string = input("Ingrese su texto: ").lower()
caracter = input("Ingrese el carácter que desea buscar: ").lower()
while len(caracter) != 1:
    caracter = input(f"{Fore.RED}Error.{Fore.RESET}Ingrese el carácter que desea buscar: ").lower()

print(buscar_caracter(string, caracter))
'''

# 3) Crear una función que reciba como parámetro una cadena y determine si la
# misma es o no un palíndromo. Deberá retornar un valor booleano indicando
# lo sucedido.

def palindromo(chain):

    for i in range(len(chain)):
        
        if chain[i] == chain[-i - 1]:
            pass

        else:
            return False


    return True

'''
cadena = input("Ingrese una palabra: ").lower()

print(palindromo(cadena))
'''

# 4) Crear una función que reciba como parámetro una cadena y suprima los
# caracteres repetidos.
# Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

def suprimir(chain):

    word = ""

    for i in chain:

        if not i in word:
            word += i
    
    return word

'''
cadena = input("Ingrese una palabra con letras repetidas: ").lower().strip()
while not cadena.isalpha():
    cadena = input(f"{Fore.RED}Error.{Fore.RESET}Solo palabras sin números: ").lower().strip()

print(suprimir(cadena))

'''
# 5) Crear una función que reciba una cadena por parámetro y suprima las
# vocales de la misma.
# Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.

def vocales_sup(chain):
    vocales = "aeiou"
    word = ""

    for i in chain:
        if not i in vocales:

            word += i
            
    return word

'''
cadena = input("Ingrese una palabra o texto con vocales: ").lower()
while not cadena.isalpha():
    cadena = input(f"{Fore.RED}Error.{Fore.RESET}Solo texto sin números: ").lower()

print(vocales_sup(cadena))
'''

# 6) Crear una función para contar cuántas veces aparece una subcadena dentro
# de una cadena.
# Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá
# retornar el valor 2.

def subcadena_count(chain,subchain):
    
    return chain.count(subchain)


cadena = input("Ingresar cadena: ").lower()
while not cadena.isalpha():
    cadena = input(f"{Fore.RED}Error.{Fore.RESET}Ingresar cadena: ").lower()

subcadena = input("Ingresar subcadena: ").lower()
while not subcadena.isalpha():
    subcadena = input(f"{Fore.RED}Error.{Fore.RESET}Ingresar cadena: ").lower()

print(subcadena_count(cadena, subcadena))