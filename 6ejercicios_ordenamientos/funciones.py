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