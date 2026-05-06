from Listas import nombres, telefonos,  mails, address, postalZip, region, country, edades

def U_Mexico():
    for i in range(len(nombres)):
        if country[i] == "Mexico":
            print(nombres[i], edades[i], mails[i], telefonos[i])

def U_Brasil():
    for i in range(len(nombres)):
        if country[i] == "Brazil":
            print(nombres[i], mails[i], telefonos[i])

def mas_joven():
    menor = min(edades)
    for i in range(len(edades)):
        if edades[i] == menor:
            print(nombres[i], edades[i])

def promedio_edades():
    print(sum(edades) / len(edades))

def mayor_brasil():
    mayor = -1
    indice = -1

    for i in range(len(edades)):
        if country[i] == "Brazil" and edades[i] > mayor:
            mayor = edades[i]
            indice = i
    
    print(nombres[indice], edades[indice])

def mexico_brasil_PZ():
    for i in range(len(nombres)):
        if (country[i] == "Mexico" or country[i] == "Brazil") and postalZip[i] > 8000:
            print(nombres[i], country[i], postalZip[i])

def italianos_mayores():
    for i in range(len(nombres)):
        if country[i] == "Italy" and edades[i] > 40:
            print(nombres[i], mails[i], telefonos[i])
