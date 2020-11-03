import sys

if len(sys.argv) == 2:
     numero = int(sys.argv[1])
     if numero < 0 or numero > 999:
        print ("Error - Numero no es correctos")
        print ("Ejemplo: descomposicion.py [0-999])")
     else:
        #aqui empieza la logica
        cadena = str (numero)
        longitud = len(cadena)
        
        for i in range(longitud):
            print ( "{:04d}". format( int(cadena[longitud-1-i]) *10 ** i))
        
else:
    print ("Error - Argumentos incorrectos")
    print ("Ejemplo: descomposicion.py [0-999])")
