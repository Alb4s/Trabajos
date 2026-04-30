from colorama import Fore, Style, init

init()







#4

def fibonacci(numero:int)->int:
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    
    return fibonacci(numero - 1) + fibonacci(numero - 2)

numero = int(input("Ingresar un entero al cuál se le calculará Fibonacci: "))

for i in range (numero + 1):
    print(Fore.LIGHTCYAN_EX, fibonacci(i))

'''

numero -> (num - 1) + (num - 2)

'''