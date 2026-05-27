import funciones
flag = True
importado = False
lista_poke = []

while flag == True:
    print(
    " 1. Importar lista de Pokémones","\n",
    "2. Lista de Pokémones","\n",
    "3. Agregar Pokémon","\n",
    "4. Eliminar Pokémon","\n",
    "5. Ordenar Pokémones","\n",
    "6. Pokémon más pesado tipo agua","\n",
    "7. Pokémon con más fuerza","\n",
    "8. Listar Pokémon por región","\n",
    "9. Salir del menú","\n",)

    op = input("Elija una opción: ").strip()
    op = funciones.opcion(op)

    if op == 1:
        lista_poke = funciones.importar_lista()

        importado = True
        print("Lista importada exitosamente","\n")

    elif op == 2:
        if funciones.verificar_importado(importado) == True:
        
            funciones.listar(lista_poke)
    
    elif op == 3:
        if funciones.verificar_importado(importado) == True:
            
           lista_poke.append(funciones.agregar_pokemon())
           print("Pokémon agregado exitosamente","\n")

    elif op == 4:
        if funciones.verificar_importado(importado) == True:

            bandera = False
            while bandera == False:

                nombre = funciones.dato_1("Ingrese el nombre del pokémon a eliminar: ").strip().title()
                erased = funciones.eliminar_pokemon(lista_poke, nombre)

                if erased != None:
                    print(f"se ha eliminado a {erased[0]} exitosamente","\n")
                    bandera = True
                else:
                    print("Pokémon no encontrado","\n")

    elif op == 5:
        if funciones.verificar_importado(importado) == True:
            ordenar = funciones.ordenar_pokemones(lista_poke)
            
            funciones.listar(ordenar)
    
    elif op == 6:
        if funciones.verificar_importado(importado) == True:
            
            funciones.maximo_poke(lista_poke, 3, 1, "Agua")
    
    elif op == 7:
        if funciones.verificar_importado(importado) == True:
            
            funciones.maximo_poke(lista_poke, 5)

    elif op == 8:
        if funciones.verificar_importado(importado) == True:
            
            funciones.poke_region(lista_poke)

    elif op == 9:
        flag = False

print("Saliste del menú")