import random as rm

def quini6(dinero):
    

    quini = []

    numeros = list(range(16))

    for i in range(len(numeros)):
        numeros[i] = str(numeros[i])

    while len(quini) < 6:
        num = input ("Ingrese los numeros: ")

        if num not in numeros:
            print ("Lo que ingresanste no es un numero, es menor a 0 o mayor a 15")

        else:
            num = int(num)
            if num not in quini:
                quini.append(num)

            else:
                print ("Ese numero ya lo elegiste")
                
    print ("Tus numeros elegidos son: ", quini)


    num_pc = []


    while len(num_pc) <6:

        num_rm = rm.randint (0,15)

        if num_rm not in num_pc:
            num_pc.append(num_rm)

    print ("Los numeros ganadores son: ",num_pc)


    #Aciertos

    aciertos = []

    for i in quini:

        if i in num_pc:
            print ("Este numero es ganador: ",i)
            aciertos.append(i)
    print ("Tus aciertos fueron: ", aciertos)

    num_acer = len(aciertos)
    if num_acer == 6:
        print ("Te sacaste la grande!! Eres millonario!!")
        return dinero * 1000000
    elif num_acer == 5:
        print ("5 de 6.. Buen previo se viene!!")
        return dinero * 100000
    elif num_acer == 4 or num_acer == 3:
        print ("Estuviste cerca... Sigue intentado para llegar a la cima!!")
        return dinero * 10000
    elif num_acer == 2:
        print ("Acertaste 2, Recuperas tu apuesta.")
        return dinero * 1
    else:
        print ("Lo siento, perdiste!!")
        return dinero * 0

def bienvenida ():
    nombre = input ("Cual es tu nombre: ")
    global dineroIn #declaracion de variables globales
    dineroIn = int(input("Cuanto dinero quieres apostar: "))
    print ("Bienvenido " +nombre + " a la casa 'Casa del Juego'\nAqui encontras unos juegos divertidos que te permitiran ganar(o perder) dinero,\n"
           "dependiendo de tu habilidad.\n"
           "Para ello, cuentas con $" + str(dineroIn) + " para jugar y divertirte\nBuena suerte.")

#El programa en si mismo empieza aca
bienvenida()
saldo = quini6(dineroIn)
print ("Tu saldo es: ",saldo)

repetir = True
while repetir:
    if saldo > 0:
        pregunta =("Quieres seguir jugando? s/n: ").upper()
        if pregunta == 'S':
            saldo = quini6(saldo)
            print ("Tu saldo es: ", saldo)
        else:
            repetir = False
    else:
        repetir = False

print ("Gracias por jugar, Vuelve pronto")
