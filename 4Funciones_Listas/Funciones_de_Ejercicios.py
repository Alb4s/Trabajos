def U_Mexico(name, age, mail, phone, country):
    for i in range(len(name)):
        if country[i] == "Mexico":
            print(name[i], age[i], mail[i], phone[i])


def U_Brasil(name, mail, phone, country):
    for i in range(len(name)):
        if country[i] == "Brazil":
            print(name[i], mail[i], phone[i])

def mas_joven(name, age):
    menor = min(age)
    for i in range(len(age)):
        if age[i] == menor:
            print(name[i], age[i])

def promedio_edades(age):
    print(sum(age) / len(age))

def mayor_brasil(name, age, country):
    mayor = -1
    indice = -1

    for i in range(len(age)):
        if country[i] == "Brazil" and age[i] > mayor:
            mayor = age[i]
            indice = i
    
    print(name[indice], age[indice])

def mexico_brasil_PZ(name, country, pz):
    for i in range(len(name)):
        if (country[i] == "Mexico" or country[i] == "Brazil") and pz[i] > 8000:
            print(name[i], country[i], pz[i])

def italianos_mayores(name, mail, phone, country, age):
    for i in range(len(name)):
        if country[i] == "Italy" and age[i] > 40:
            print(name[i], mail[i], phone[i])