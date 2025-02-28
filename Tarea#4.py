
#Ejercicio Elegibilidad para votar
#varianles donde se guarda el ano de nacimiento y el actual
anoNacimiento=int(input('Ingrese su ano de nacimeinto'))
anoActual=int(input('Ingrese la ano actual'))

Vota=anoNacimiento-anoActual#operacion para el si puede o no

if(Vota < 18):#Si es menor de edad
    print('No puedes votar, eres menor de edad')
else:#Si es mayor de edad
    print('Eres mayor de edad, puedes votar')

#Ejercicio del dia de la semana
#Variable para guardar el numero del dia
dia=int(input('Ingrese un numero de 1 al 7'))
#Este if es para escoger el numero que ingreso el usuario
if(dia == 1):
  print('Hoy es Lunes')
elif(dia == 2):
    print('Hoy es Martes')
elif(dia == 3):
    print('Hoy es Miercoles')
elif (dia == 4):
    print('Hoy es Jueves')
elif (dia == 5):
    print('Hoy es Viernes')
elif (dia == 6):
    print('Hoy es Sabado')
elif(dia ==7):
    print('Hoy es Domingo')
else:
    print('Lo siento ponga un numero del 1 al 7')

#Ejercicio del IMC
peso=float(input('Ingrese su peso'))
estatura=float(input('Ingrese su altura'))

imc= peso/(estatura**2)#variable donde guarda el resultado del IMC

if (imc < 18.5):
    print('Su IMC es de: ' + str(imc))
    print('Estas en bajo peso')
elif (18.5<=imc<25):
    print('Su IMC es de: ' + str(imc))
    print('Estas en peso normal')
elif(25<=imc<30):
    print('Su IMC es de: ' + str(imc))
    print('Estas en sobrepeso')
elif (imc >30):
    print('Su IMC es de: ' + str(imc))
    print('Estas en obesidad')
else:
    print('Lo siento su IMC no se pudo medir')