def verificar_importado(x:bool)-> bool:

    if x == False:
        print("Error.Primero debes importar la lista","\n")
        return False
    return True

def importar_lista()-> list:
    from lista_pokemon_A import lista_pokemon
    return lista_pokemon

def listar(lista:list)-> list:
    for i in lista:
        print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],"\n", "----")

def validacion_enblanco(x:str)->str:

    while x == "":
        x = input("Error.Fuera de parámetro. Reingresar: ").strip()
    
    return x

def opcion(option)-> int:

    option = validacion_enblanco(option)
    option = int(option)

    while option < 1 or option > 9:
        option = input("Error.Fuera de parámetro.Reingresar opción: ").strip()
        option = int(option)
    
    return option

def dato_1(x:str)->str:
    
    dato = input(x).strip().title()
    dato = validacion_enblanco(dato)
    return dato

def dato_2_int(x:int)-> int:
    
    dato = input(x)
    dato = validacion_enblanco(dato)
    dato = int(dato)

    while dato <= 0:
        dato = int(input("Error.No puede ser menor o igual a 0. Reingresar: "))

    return dato

def dato_2_float(x:float)-> float:
    dato = input(x)
    dato = validacion_enblanco(dato)
    dato = float(dato)

    while dato <= 0:
        dato = float(input("Error.No puede ser menor o igual a 0. Reingresar: "))

    return dato

def dato_3_region(x:str)-> str:
    r = input(x).strip().title()

    while r != "Johto" and r != "Kanto" and r != "Sinnoh" and r != "Hoenn" and r != "Kalos":
        r = input("Error.Fuera de parámetro. Reingresar: ").strip().title()
    return r

def agregar_pokemon()-> list:

    nombre = dato_1("Ingresar nombre del pokémon: ")
    tipo = dato_1("Ingresar su tipo: ")

    altura = dato_2_float("Ingresar altura: ")
    peso = dato_2_float("Ingresar peso: ")
    nivel = dato_2_int("Ingresar nivel: ")
    fuerza = dato_2_int("Ingresar fuerza: ")

    region = dato_3_region("Ingresar region (Debe ser de Johto/Kanto/Sinnoh/Hoenn/Kalos): ")
    
    return [nombre, tipo, altura, peso, nivel, fuerza, region]

def eliminar_pokemon(list:list, name:str)-> bool:

    x = 0
    while x < len(list):
        if list[x][0] == name:
            pokemon = list[x]
            list.pop(x)
            find = True
            return pokemon
        x += 1
    
    return None

def ordenar_pokemones(list:list)-> list:
    for i in range(len(list)- 1):
            for j in range(i+ 1, len(list)):
                if list[i][0] > list[j][0]:

                    aux = list[i]
                    list[i] = list[j]
                    list[j] = aux
    return list

def maximo_poke(lista:list, indice:int, filtro_i:int= None, filtro_j:str= None)-> None:

    valores = []
    for i in lista:
        if filtro_i == None or i[filtro_i] == filtro_j:
            valores.append(i[indice])
    
    maximo = max(valores)
    
    for i in lista:
        if i[indice] == maximo:
            if filtro_i == None or i[filtro_i] == filtro_j:
                listar([i])

def poke_region(list:list)-> None:

    region = dato_3_region("Ingresar región (Johto/Kanto/Sinnoh/Hoenn/Kalos): ")

    for i in list:
        if i[6] == region:
            listar([i])