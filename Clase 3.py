#Ingreso de autores
autores = []

ingresar = True

while ingresar:
    autor = input ("Ingrese el nombre del autor(x para salir): ").upper()
    if autor == "X":
        ingresar = False
    else:
        if autor not in autores:
            autores.append(autor)
        else:
            print ("Ese autor ya fue ingresado")
       

print ("Los autores ingresados son: ",autores)

#Buscador

encontrados = []
buscar = True
while buscar:
    autor = input ("Ingrese el nombre del autor(x para salir): ").upper()
    if autor == "X":
        buscar = False

    else:
        if autor in autores:
            print ("Si a", autor, "lo tengo")
            if autor not in encontrados:
                encontrados.append(autor)
        else:
            print ("No, a",autor,"no lo tengo")

print ("Tus autores encontrados son: ",encontrados)
