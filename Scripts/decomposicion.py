import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print ('Error - Numero es incorrectos')
        print ('Ej: tabla.py [1-9999]')
    else: #aqui va la logica
        cadena = str(numero)
        longitud = len(cadena)
        for i in range(longitud):
            print("{:04d}".format (int(cadena[longitud-1-i]) * 10 ** i) )
        
else:
    print ('Error - Argumentos incorrectos')
    print ('Ej: decomposicion.py [1-9999]')

print ('Estoy probando GIT')