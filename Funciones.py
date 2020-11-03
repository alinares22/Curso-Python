#funciones

#funciones que no devuelve resultado

def imprimir_tyc(provincia):
    print ("Terminos y condiciones aplican",provincia,"y ademas..")

#funcion que devuelve

def lineal(x):
    '''num -> num
    Devuelve el valor ingresado mas 3
    >>>lineal(3)
    6'''
    return 3 + x

#Aca empieza el programa
resultado = lineal(3)
print ("El resultado es: ",resultado)
print (abs(lineal(6)))

