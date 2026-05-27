def menu_heroes():
    print(
        " 1. Lista de heroes","\n",
        "2. Agregar heroe","\n",
        "3. Eliminar heroe por nombre","\n",
        "4. Ordenar heroes por nombre","\n",
        "5. Heroe mas alto","\n",
        "6. Heroe mas fuerte","\n",
        "7. Heroe mas delgado","\n",
        "8. Salir del menú"
    )

def validacion_enblanco(x:str)->str:

    while x == "":
        x = input("Error.Fuera de parámetro. Reingresar: ")

    return x

def validacion_0(x:float)->float:

    while x <= 0:
        x = float(input)("Error.Fuera de parámetro. Reingresar: ")
    
    return x

