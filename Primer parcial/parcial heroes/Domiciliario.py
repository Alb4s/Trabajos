import funciones
from lista_heroes import lista_heroes

print("Lista de Heroes","\n")

flag = True

while flag == True:
    funciones.menu_heroes()

    op = int(input("Elegir opción: "))
    while op < 1 or op > 8:
        op = int(input("Error.Solo las opciones asignadas: "))

    if op == 1:
        for i in lista_heroes:
            print(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],"\n","----") #se puede remplazar por una función

    elif op == 2:
        nombre = input("Ingrese el nombre del héroe: ").title().strip()
        nombre = funciones.validacion_enblanco(nombre)

        identidad = input("Ingrese la identidad del héroe: ").title().strip()
        identidad = funciones.validacion_enblanco(identidad)
        
        distribuidora = input("Ingrese de que distribuidora es su héroe(Marvel Comics/DC Comics): ").lower().strip()
        while distribuidora != "marvel comics" and distribuidora != "dc comics":
            distribuidora = input("Error.Debe ser de Marvel Comics o DC Comics: ").lower().strip()
        
        peso = float(input("Ingresar peso del héroe: "))
        peso = funciones.validacion_0(peso)

        altura = float(input("Ingresar la altura del héroe: "))
        altura = funciones.validacion_0(altura)

        fuerza = int(input("Ingresar la fuerza del héroe (1-100): "))
        while fuerza < 1 or fuerza > 100:
            fuerza = int(input("Error.Menor a 1 o mayor a 100 no admitidos: "))
        
        genero = input("Ingrese el genero (M/F/NB): ").upper().strip()
        while genero != "M" and genero != "F" and genero != "NB":
            genero = input("Error.Solo se admiten los géneros especificados: ").upper().strip()
        
        ojos = input("Ingrese el color de ojos: ")
        ojos = funciones.validacion_enblanco(ojos)

        pelo = input("Ingrese el color de pelo: ")
        pelo = funciones.validacion_enblanco(pelo)

        inteligencia = input("Ingrese su nivel de inteligencia(low/average/good/high/genius): ").lower().strip()
        while inteligencia != "low" and inteligencia != "average" and inteligencia != "good" and inteligencia != "high" and inteligencia != "genius":
            inteligencia = input("Error.Fuera de los limites de la inteligencia: ").lower().strip()
        
        lista_heroes.append([nombre, identidad, distribuidora, altura, peso, genero, ojos, pelo, fuerza, inteligencia])

        print("Agregado Exitosamente")

    elif op == 3:
        flag2 = True
        while flag2 == True:
            nombre = input("Ingrese el nombre del héroe que quiere eliminar: ").title().strip()
            nombre = funciones.validacion_enblanco(nombre)

            find = False
            x = 0
            while x < len(lista_heroes) and not find:
                if lista_heroes[x][0] == nombre or lista_heroes[x][1] == nombre:
                    lista_heroes.pop(x)
                    find = True
                x += 1
            
            if find == True:
                print("Borrado Exitosamente")
                flag2 = False
            else:
                print("Héroe no Encontrado")

    elif op == 4:
        for i in range(len(lista_heroes)- 1):
            for j in range(i+ 1, len(lista_heroes)):
                if lista_heroes[i][0] > lista_heroes[j][0]:

                    aux = lista_heroes[i]
                    lista_heroes[i] = lista_heroes[j]
                    lista_heroes[j] = aux
        for x in lista_heroes:
            print(x,"\n","----")

    elif op == 5:
        alturas = []
        for i in lista_heroes:
            alturas.append(i[3])
        maximo = max(alturas)
        
        for x in lista_heroes:
            if x[3] == maximo:
                print(x,"\n","----")

    elif op == 6:
        fuerza_lista = []
        for i in lista_heroes:
            fuerza_lista.append(i[8])
        maximo = max(fuerza_lista)
        
        for x in lista_heroes:
            if x[8] == maximo:
                print(x,"\n","----")

    elif op == 7:
        peso_lista = []
        for i in lista_heroes:
            peso_lista.append(-i[4])
        maximo = max(peso_lista)
        
        for x in lista_heroes:
            if -x[4] == maximo:
                print(x,"\n","----")

    elif op == 8:
        flag = False

print("Saliste del menú")