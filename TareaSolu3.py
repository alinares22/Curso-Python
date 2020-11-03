#numeros random
num_pc = []
numeros = 6
import random as rm

for i in range (numeros):
    numero = rm.randint (0,15)
    num_pc.append(numero)
  

#Ingreso de numeros
quini = []

for i in range (numeros):

    num = int(input("Ingrese el numero: "))
    quini.append(num)
    
print (quini)
print ("Gracias por jugar.")      

#Condiciones
aciertos = []

def acierto(quini,num_pc):
    for x in quini:
        for y in num_pc:
            if x == y:
                aciertos.append
            
