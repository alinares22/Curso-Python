import random as rm #Se usa AS para abreviar nombre de librerias largos
numeros = list(range(101))
for i in range(len(numeros)):
    numeros[i]= str(numeros[i])
numero = rm.randint (0,100)
contador = 0
juego = True

while juego:
    num = int(input("Ingrese el numero: "))
  

    if num > numero:
              print ("El numero es menor")

    elif num < numero:
        print ("El numero es mayor")

    else:
        print ("Muy bien!! Este es el numero")
        juego = False
    contador +=1

print ("Gracias por jugar, acertaste en", contador,"intentos")
