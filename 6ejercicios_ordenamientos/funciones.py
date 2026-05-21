def ordenar_listas(name, age):
    pares = list(zip(name, age))
    ordenamiento = sorted(pares, key=lambda x: x[0])

    return ordenamiento

def ordenar_listas_2(assignature, points):
    orden = list(zip(assignature, points))
    materias = sorted(orden, key=lambda x: (x[0], -x[1]) )
    
    return materias

def ordenar_listas_3(students, lastname, note):
    nombre_completo_nota = list(zip(students,lastname,note))
    ordenar = sorted(nombre_completo_nota, key=lambda x: (x[0], x[1], -x[2]))

    return ordenar

def ordenar_mexico(name, age, phone, mail, count):
    lista = []
    mexico = list(zip(name, age, phone, mail, count))
    for i in mexico:
        if i[4] == "Mexico":
            lista.append(i)
    ordenar = sorted(lista, key=lambda x: (x[0]))

    return ordenar


def ordenar_menor(age, name):
    lista = []
    menor_lista = list(zip(age, name))
    minimo = min(age)

    for i in menor_lista:
        if i[0] == minimo:
            lista.append(i)
    
    ordenar = sorted(lista, key=lambda x: (x[0], x[1]))

    return ordenar

def postal_zip(name, age, country, pz):
    lista = []
    codigo_lista = list(zip(name, age, country, pz))

    for i in codigo_lista:
        if (i[2] == "Mexico" or i[2] == "Brazil") and i[3] > 8000:
            lista.append(i)
    ordenar_codigos = sorted(lista, reverse=True, key=lambda x: (x[0], x[1]))

    return ordenar_codigos